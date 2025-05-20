from dash import Output, Input, State, no_update 
import subprocess
from io import StringIO
from model.flowcapture import run_capture



def network_flow_callbacks(app):
    from app.pages.dashboard import create_dashboard
    @app.callback(
        Output("start-button", "children"),
        [Input("start-button", "n_clicks")],
        [
            State("interface-input", "value"),
            State("time-input", "value"),
            State("session-store", "data"),
        ],
        prevent_initial_call=True
    )
    def handle_network_flow_collection(n_clicks, interface, time_range, session_data):
        global collection_process, is_collecting
        
        if n_clicks is None:
            return no_update
        
        if not interface:
            return "START"
        
        if not time_range:
            time_range = "30"
        
        try:
            time_seconds = int(time_range)
        except ValueError:
            return "START"
        
        try:
            run_capture(interface, time_seconds)
            print ("test")
            create_dashboard(session_data.get("username", "User"))
            return "STOP"
        except Exception:
            return "START"
