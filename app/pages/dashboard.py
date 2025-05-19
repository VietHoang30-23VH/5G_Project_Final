import dash
from dash import html, dcc, dash_table, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
from components.navbar import create_navbar

colors = {
    'primary': '#1e3a8a',
    'secondary': '#64748b',
    'success': '#22c55e',
    'danger': '#ef4444',
    'warning': '#f59e0b',
    'info': '#0ea5e9',
    'light': '#f8fafc',
    'dark': '#334155',
    'white': '#ffffff',
    'background': '#f5f7fa',
}

# Create Network Controls Card
def create_network_controls():
    return dbc.Card([
        dbc.CardHeader(html.H5("Network Controls", className="fw-bold")),
        dbc.CardBody([
            dbc.Form([
                dbc.Row([
                    dbc.Label("Interface", width="5px"),
                    dbc.Col(
                        dbc.Input(
                            id="interface-input",
                            type="text",
                            placeholder="eth0",
                            value="any",
                        ),
                        className="pe-2",
                    ),
                ], className="align-items-center"),
                
                dbc.Row([
                    dbc.Label("Time Range", width="2px"),
                    dbc.Col(
                        dbc.Input(
                            id="time-input",
                            type="text",
                            placeholder="30",
                        ),
                        className="pe-2",
                    ),
                ], className="mb-1 align-items-center"),
                
                dbc.Row([
                    dbc.Col(
                        dbc.Button(
                            "START", 
                            id="start-button", 
                            className="w-15"
                        ),
                        width=6,
                    ),
                    dbc.Col(
                        dbc.Button(
                            "STOP", 
                            id="stop-button", 
                            className="w-100"
                        ),
                        width=6,
                    ),
                ]),
            ]),
        ]),
    ], className="shadow-sm", style={"margin-top": "1rem"})

# Create Packet Summary Card
def create_packet_summary():
    return dbc.Card([
        dbc.CardHeader(html.H5("Packet Summary", className="fw-bold")),
        dbc.CardBody([
            dbc.Row([
                dbc.Col(html.Div("Number Packet Captured:"), width=8),
                dbc.Col(html.Div(id="packet-count", children="0"), width=4, className="text-end fw-bold"),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col(html.Div("Total Bytes:"), width=8),
                dbc.Col(html.Div(id="total-bytes", children="0 KB"), width=4, className="text-end fw-bold"),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col(html.Div("Lost Packets:"), width=8),
                dbc.Col(html.Div(id="lost-packets", children="0"), width=4, className="text-end fw-bold text-danger"),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col(html.Div("Duration:"), width=8),
                dbc.Col(html.Div(id="duration", children="00:00:00"), width=4, className="text-end fw-bold"),
            ], className="mb-2"),
        ]),
    ], className="shadow-sm mt-1")

# Create Detection Results Card
def create_detection_results():
    return dbc.Card([
        dbc.CardHeader(html.H5("Detection Results", className="fw-bold")),
        dbc.CardBody([
            dbc.Alert(
                [
                    html.H6("Alert: DDoS Signature Detected", className="alert-heading"),
                    html.P([
                        html.Span("Attack Type: ", className="fw-bold"),
                        "TCP SYN Flood"
                    ], className="mb-0"),
                    html.P([
                        html.Span("Attack Tool: ", className="fw-bold"),
                        "Hping3"
                    ], className="mb-0"),
                    html.P([
                        html.Span("Timestamp: ", className="fw-bold"),
                        "10:42:35-18/05/2025"
                    ], className="mb-0"),
                ],
                color="danger",
                className="mb-0",
            ),
        ]),
    ], className="shadow-sm mt-1")

# Create Network Flow Chart
def create_network_flow_chart():
    # Sample data for the line chart
    time_range = pd.date_range(
        start=datetime.now() - timedelta(minutes=30),
        end=datetime.now(),
        freq='1min'
    )
    
    # Create normal traffic pattern
    inbound = [25 + np.random.randint(0, 15) for _ in range(len(time_range))]
    outbound = [20 + np.random.randint(0, 10) for _ in range(len(time_range))]
    
    # Simulate attack spike near the end
    attack_start = len(time_range) - 8
    for i in range(attack_start, len(time_range)):
        severity = (i - attack_start + 1) * 10
        inbound[i] += min(severity, 60)
        outbound[i] += min(severity // 2, 30)
    
    # Create the figure
    fig = go.Figure()
    
    # Add traces
    fig.add_trace(go.Scatter(
        x=time_range, 
        y=inbound,
        mode='lines',
        name='Inbound',
        line=dict(color=colors['info'], width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=time_range, 
        y=outbound,
        mode='lines',
        name='Outbound',
        line=dict(color=colors['danger'], width=2)
    ))
    
    # Update layout
    fig.update_layout(
        title=None,
        margin=dict(l=40, r=20, t=20, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            title=None,
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)'
        ),
        yaxis=dict(
            title='Packets/sec',
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)'
        ),
        plot_bgcolor=colors['white'],
        paper_bgcolor=colors['white'],
    )
    
    return dbc.Card([
        dbc.CardHeader(html.H5("Network Flow", className="fw-bold")),
        dbc.CardBody([
            dcc.Graph(
                id='network-flow-graph',
                figure=fig,
                config={'displayModeBar': False},
                style={'height': '222px'}
            )
        ]),
    ], className="shadow-sm", style={"margin-top": "2rem"})

# Create Initial Traffic Table
def create_initial_traffic_table():
    # Sample data for the table
    df = pd.DataFrame({
        "Proto": ["TCP", "UDP", "TCP", "ICMP", "TCP"],
        "AckDat": ["124ms", "-", "324ms", "-", "296ms"],
        "sHops": [4, 3, 2, 5, 2],
        "Seq": [245, "-", 897, "-", 898],
        "State": ["EST", "-", "SYN", "-", "SYN"],
        "TcpRtt": ["34ms", "-", "178ms", "-", "163ms"],
        "dmeansz": [512, 248, 64, 84, 64],
        "offset": [0, 0, 0, 0, 0],
        "sttl": [64, 128, 32, 255, 32],
        "flgs": ["ACK", "-", "SYN", "-", "SYN"],
        "mean": [128, 64, 32, 42, 32],
        "cause": ["normal", "normal", "attack", "normal", "attack"],
    })
    
    # Style conditional for highlighting attack traffic
    style_data_conditional = [
        {
            'if': {'filter_query': '{cause} = "attack"'},
            'color': colors['danger'],
            'fontWeight': 'bold'
        }
    ]
    
    return dbc.Card([
        dbc.CardHeader(html.H5("Initial Traffic", className="fw-bold")),
        dbc.CardBody([
            dash_table.DataTable(
                id='initial-traffic-table',
                columns=[{"name": i, "id": i} for i in df.columns if i != "cause"],
                data=df.to_dict('records'),
                style_table={'overflowX': 'auto'},
                style_cell={
                    'textAlign': 'left',
                    'padding': '8px',
                    'fontFamily': 'Arial, sans-serif',
                    'fontSize': '13px',
                },
                style_header={
                    'backgroundColor': colors['light'],
                    'fontWeight': 'bold',
                    'color': colors['secondary'],
                    'borderBottom': f'1px solid {colors["secondary"]}',
                },
                style_data_conditional=style_data_conditional,
                page_size=5,
            )
        ]),
    ], className="shadow-sm", style={"margin-top": "0.5rem"})
# Create Processed Traffic Table
def create_processed_traffic_table():
    # Sample data for the table
    df = pd.DataFrame({
        "tcp": [1, 0, 1, 0, 1],
        "AckDat": ["124ms", "-", "324ms", "-", "296ms"],
        "sHops": [4, 3, 2, 5, 2],
        "Seq": [245, "-", 897, "-", 898],
        "RST": [0, 0, 0, 0, 0],
        "TcpRtt": ["34ms", "-", "178ms", "-", "163ms"],
        "REQ": ["GET", "-", "SYN", "-", "SYN"],
        "dMeanPktSz": [512, 248, 64, 84, 64],
        "Offset": [0, 0, 0, 0, 0],
        "CON": [1, 0, 0, 0, 0],
        "FIN": [0, 0, 0, 0, 0],
        "sTtl": [64, 128, 32, 255, 32],
        "INT": [0, 1, 0, 0, 0],
        "Mean": [128, 64, 32, 42, 32],
        "Status": ["normal", "normal", "attack", "normal", "attack"],
    })
    
    # Style conditional for highlighting attack traffic
    style_data_conditional = [
        {
            'if': {'filter_query': '{Status} = "attack"'},
            'color': colors['danger'],
            'fontWeight': 'bold'
        }
    ]
    
    return dbc.Card([
        dbc.CardHeader(html.H5("Processed Traffic",className="fw-bold")),
        dbc.CardBody([
            dash_table.DataTable(
                id='processed-traffic-table',
                columns=[{"name": i, "id": i} for i in df.columns if i != "Status"],
                data=df.to_dict('records'),
                style_table={'overflowX': 'auto'},
                style_cell={
                    'textAlign': 'left',
                    'padding': '8px',
                    'fontFamily': 'Arial, sans-serif',
                    'fontSize': '13px',
                },
                style_header={
                    'backgroundColor': colors['light'],
                    'fontWeight': 'bold',
                    'color': colors['secondary'],
                    'borderBottom': f'1px solid {colors["secondary"]}',
                },
                style_data_conditional=style_data_conditional,
                page_size=5,
            )
        ]),
    ], className="shadow-sm", style={"margin-top": "1.2rem"})
# Create Sample Data Processing Info
def create_sample_data_info():
    return dbc.Card([
        dbc.CardBody([
            html.P([
                html.Span("Mẫu 274 with [10:42:35-18/05/2025]:", className="fw-bold"),
                html.Br(),
                html.Span("- Label: "), "Malicious",
                html.Br(),
                html.Span("- Attack Type: "), "TCP SYN Flood",
                html.Br(),
                html.Span("- Attack Tool: "), "Hping3"
            ], className="mt-1 text-info"),
        ]),
    ], className="shadow-sm mt-3 border-info border-start border-4")

# Main layout function
def create_dashboard(username):
    return html.Div([
        # Navigation Bar
        html.Div([
            create_navbar(username)
        ], className="sticky-top shadow-sm"),
        
        # Main Content
        dbc.Container([
            # First Row - Network Controls and Network Flow
            dbc.Row([
                # Left Column - Network Controls
                dbc.Col([
                    create_network_controls(),
                    create_packet_summary(),
                    create_detection_results(),
                    create_sample_data_info(),
                ], width=3, style={"margin-top": "1rem"}),
                
                # Right Column - Network Flow Chart
                dbc.Col([
                    create_network_flow_chart(),
                    create_initial_traffic_table(),
                    create_processed_traffic_table(),
                ], width=9),
            ]),
        ], fluid=True, className="py-3 mt-5"),
], style={"backgroundColor": colors['background'], "height": "100vh", "width": "100vw"})

# # Callback for updating packet stats when monitoring starts
# # @app.callback(
# #     [
# #         Output("packet-count", "children"),
# #         Output("total-bytes", "children"),
# #         Output("lost-packets", "children"),
# #         Output("duration", "children"),
# #     ],
# #     [Input("start-button", "n_clicks")],
# #     [
# #         State("interface-input", "value"),
# #         State("time-input", "value"),
# #         State("time-unit", "value"),
# #     ],
# #     prevent_initial_call=True
# # )
def update_packet_stats(n_clicks, interface, time_value, time_unit):
    if n_clicks is None:
        return "0", "0 KB", "0", "00:00:00"
    
    # Simulate packet statistics (in a real application, this would come from actual monitoring)
    packet_count = 45872
    total_bytes = "27.5 MB"
    lost_packets = 127
    duration = "00:31:45"
    
    return str(packet_count), total_bytes, str(lost_packets), duration