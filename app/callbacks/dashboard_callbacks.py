from dash import Output, Input, State, no_update 
import subprocess
from io import StringIO
from model.flowcapture import run_capture
from data.fetch_data import load_raw_network_traffic, load_processed_network_traffic, get_packet_summary, load_sample_prediction


def network_flow_callbacks(app):
    from app.pages.dashboard import create_dashboard
    @app.callback(
        [Output("processed-traffic-table", "data"),
         Output('initial-traffic-table', 'data'),
         Output('sample-prediction-table', 'data'),
         Output('packet-count', 'children'),
         Output('total-bytes', 'children'),
         Output('lost-packets', 'children'),
         Output('duration', 'children')],
        [Input("start-button", "n_clicks")],
        [
            State("interface-input", "value"),
            State("time-input", "value"),
            State("session-store", "data"),
        ],
        prevent_initial_call=True
    )
    def handle_network_flow_collection(n_clicks, interface, time_range, session_data):
        
        if n_clicks is None or not interface or not time_range:
            return [no_update] * 6
        
        try:
            time_seconds = int(time_range)
        except ValueError:
            return [no_update] * 6
        
        try:
            run_capture(interface, time_seconds)
            df_processed = load_processed_network_traffic()
            df_raw = load_raw_network_traffic()
            df_sample = load_sample_prediction()

            data = get_packet_summary()
            if not data:
                return [no_update] * 6

            total_flows = data['total_flows']
            total_bytes = data['total_bytes']
            lost = data['lost']
            capture_duration = data['capture_duration']
            
            return (
                df_processed.to_dict('records'),
                df_raw.to_dict('records'),
                df_sample.to_dict('records'),
                str(total_flows),
                total_bytes,
                lost,
                str(capture_duration)
            )
        except Exception:
            print("Error during capture:", e)
            return [no_update] * 6
