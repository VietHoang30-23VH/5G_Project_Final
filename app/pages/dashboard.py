from dash import html, dcc
import dash_bootstrap_components as dbc
import dash

def create_dashboard(username):
    return html.Div([
        # Header
        html.Div([
            html.H1("5G Network Security Monitoring Dashboard", className="text-center mb-3"),
            html.Div([
                html.Button("Đăng xuất", id="logout-button", className="btn btn-danger me-2"),
                html.Div(id="welcome-user", children=f"Xin chào, {username}!", 
                        className="fw-bold fs-5 d-flex align-items-center")
            ], className="d-flex justify-content-between align-items-center mb-4"),
        ], className="container-fluid bg-light p-3 shadow-sm"),
        
        # Main content
        html.Div([
            # Monitor control section
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Điều khiển giám sát", className="bg-primary text-white fw-bold"),
                        dbc.CardBody([
                            html.Div([
                                html.Button(
                                    html.Span([
                                        html.I(className="fas fa-play me-2"), 
                                        "Start Monitoring"
                                    ]), 
                                    id="start-monitoring-btn",
                                    className="btn btn-success me-2"
                                ),
                                html.Button(
                                    html.Span([
                                        html.I(className="fas fa-stop me-2"), 
                                        "Stop Monitoring"
                                    ]), 
                                    id="stop-monitoring-btn",
                                    className="btn btn-danger me-2",
                                    disabled=True
                                ),
                                html.Button(
                                    html.Span([
                                        html.I(className="fas fa-download me-2"), 
                                        "Download Results"
                                    ]), 
                                    id="download-results-btn",
                                    className="btn btn-info",
                                    disabled=True
                                ),
                                dcc.Download(id="download-csv")
                            ], className="d-flex")
                        ])
                    ], className="mb-4 shadow-sm")
                ], width=12)
            ]),
            
            # Status cards
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Packets Captured", className="text-center mb-3"),
                            html.Div([
                                html.Div([
                                    html.H2(id="total-packets", children="0", 
                                           className="text-center text-primary mb-0"),
                                    html.P("Total", className="text-center text-muted mb-0")
                                ], className="col text-center"),
                                html.Div([
                                    html.H2(id="total-bytes", children="0 KB", 
                                           className="text-center text-success mb-0"),
                                    html.P("Total Bytes", className="text-center text-muted mb-0")
                                ], className="col text-center"),
                                html.Div([
                                    html.H2(id="lost-packets", children="0", 
                                           className="text-center text-danger mb-0"),
                                    html.P("Lost", className="text-center text-muted mb-0")
                                ], className="col text-center"),
                                html.Div([
                                    html.H2(id="monitoring-duration", children="00:00:00", 
                                           className="text-center text-info mb-0"),
                                    html.P("Duration", className="text-center text-muted mb-0")
                                ], className="col text-center")
                            ], className="row")
                        ])
                    ], className="mb-4 shadow-sm")
                ], width=12)
            ]),
            
            # Charts
            dbc.Row([
                # Network Flow Chart
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Network Flow", className="bg-primary text-white fw-bold"),
                        dbc.CardBody([
                            dcc.Graph(
                                id="network-flow-chart",
                                figure={
                                    "data": [
                                        {
                                            "x": [t for t in range(30)],
                                            "y": [0 for _ in range(30)],
                                            "type": "scatter",
                                            "name": "Packets"
                                        }
                                    ],
                                    "layout": {
                                        "title": "Packet Capture Rate",
                                        "xaxis": {"title": "Time (s)"},
                                        "yaxis": {"title": "Packets/sec"},
                                        "height": 350,
                                        "margin": {"l": 40, "r": 20, "t": 40, "b": 30}
                                    }
                                }
                            )
                        ])
                    ], className="mb-4 shadow-sm")
                ], width=8),
                
                # Attack Types Distribution
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Attack Types Distribution", className="bg-primary text-white fw-bold"),
                        dbc.CardBody([
                            dcc.Graph(
                                id="attack-types-chart",
                                figure={
                                    "data": [
                                        {
                                            "x": ["DoS", "DDoS", "Probe", "U2R", "R2L"],
                                            "y": [0, 0, 0, 0, 0],
                                            "type": "bar",
                                            "marker": {
                                                "color": ["#FF5733", "#33FF57", "#3357FF", "#F033FF", "#FF8C33"]
                                            }
                                        }
                                    ],
                                    "layout": {
                                        "title": "Attack Classification",
                                        "xaxis": {"title": "Attack Type"},
                                        "yaxis": {"title": "Count"},
                                        "height": 350,
                                        "margin": {"l": 40, "r": 20, "t": 40, "b": 30}
                                    }
                                }
                            )
                        ])
                    ], className="mb-4 shadow-sm")
                ], width=4)
            ]),
            
            # Tables
            dbc.Row([
                # Initial Traffic Table
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([
                            html.Span("Initial Traffic", className="fw-bold"),
                            html.Span(
                                html.I(className="fas fa-info-circle ms-2"),
                                id="initial-traffic-info",
                                style={"cursor": "pointer"}
                            )
                        ], className="bg-primary text-white d-flex justify-content-between align-items-center"),
                        dbc.CardBody([
                            dash.dash_table.DataTable(
                                id='initial-traffic-table',
                                columns=[
                                    {"name": i, "id": i} for i in [
                                        "Proto", "AckDat", "sHops", "Seq", "State", "TcpRtt", 
                                        "dmeansz", "offset", "sttl", "flgs", "mean", "cause", 
                                        "stcpb", "dloss", "smeansz", "loss", "dttl", "sbytes", "bytes"
                                    ]
                                ],
                                data=[],
                                page_size=5,
                                style_table={'overflowX': 'auto'},
                                style_cell={
                                    'textAlign': 'center',
                                    'padding': '5px',
                                    'fontSize': '12px',
                                    'fontFamily': 'Arial'
                                },
                                style_header={
                                    'backgroundColor': '#f1f1f1',
                                    'fontWeight': 'bold',
                                    'border': '1px solid #ddd'
                                },
                                style_data_conditional=[
                                    {
                                        'if': {'row_index': 'odd'},
                                        'backgroundColor': '#f9f9f9'
                                    }
                                ]
                            )
                        ])
                    ], className="mb-4 shadow-sm")
                ], width=12),
                
                # Processed Traffic Table
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([
                            html.Span("Processed Traffic", className="fw-bold"),
                            html.Span(
                                html.I(className="fas fa-info-circle ms-2"),
                                id="processed-traffic-info",
                                style={"cursor": "pointer"}
                            )
                        ], className="bg-primary text-white d-flex justify-content-between align-items-center"),
                        dbc.CardBody([
                            dash.dash_table.DataTable(
                                id='processed-traffic-table',
                                columns=[
                                    {"name": i, "id": i} for i in [
                                        'tcp', 'AckDat', 'sHops', 'Seq', 'RST', 'TcpRtt', 'REQ', 
                                        'dMeanPktSz', 'Offset', 'CON', 'FIN', 'sTtl', 'e', 'INT', 
                                        'Mean', 'Status', 'icmp', 'SrcTCPBase', 'e d', 'sMeanPktSz', 
                                        'DstLoss', 'Loss', 'dTtl', 'SrcBytes', 'TotBytes'
                                    ]
                                ],
                                data=[],
                                page_size=5,
                                style_table={'overflowX': 'auto'},
                                style_cell={
                                    'textAlign': 'center',
                                    'padding': '5px',
                                    'fontSize': '12px',
                                    'fontFamily': 'Arial'
                                },
                                style_header={
                                    'backgroundColor': '#f1f1f1',
                                    'fontWeight': 'bold',
                                    'border': '1px solid #ddd'
                                },
                                style_data_conditional=[
                                    {
                                        'if': {'row_index': 'odd'},
                                        'backgroundColor': '#f9f9f9'
                                    }
                                ]
                            )
                        ])
                    ], className="mb-4 shadow-sm")
                ], width=12),
                
                # Attack Detection Table
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([
                            html.Span("Attack Detection", className="fw-bold"),
                            html.Div([
                                html.Button(
                                    html.Span([
                                        html.I(className="fas fa-download me-2"),
                                        "Export CSV"
                                    ]),
                                    id="export-attacks-btn",
                                    className="btn btn-sm btn-light",
                                    disabled=True
                                ),
                                dcc.Download(id="download-attacks-csv")
                            ])
                        ], className="bg-danger text-white d-flex justify-content-between align-items-center"),
                        dbc.CardBody([
                            dash.dash_table.DataTable(
                                id='attack-detection-table',
                                columns=[
                                    {"name": "Time", "id": "time"},
                                    {"name": "Source IP", "id": "src_ip"},
                                    {"name": "Destination IP", "id": "dst_ip"},
                                    {"name": "Attack Type", "id": "attack_type"},
                                    {"name": "Tool", "id": "tool"}
                                ],
                                data=[],
                                page_size=5,
                                style_table={'overflowX': 'auto'},
                                style_cell={
                                    'textAlign': 'center',
                                    'padding': '8px',
                                    'fontFamily': 'Arial'
                                },
                                style_header={
                                    'backgroundColor': '#f8d7da',
                                    'fontWeight': 'bold',
                                    'border': '1px solid #ddd'
                                },
                                style_data_conditional=[
                                    {
                                        'if': {'row_index': 'odd'},
                                        'backgroundColor': '#f9f9f9'
                                    }
                                ]
                            )
                        ])
                    ], className="mb-4 shadow-sm")
                ], width=12),
                
                # Results Table
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([
                            html.Span("Monitoring Results", className="fw-bold"),
                            html.Div([
                                html.Button(
                                    html.Span([
                                        html.I(className="fas fa-download me-2"),
                                        "Export Results"
                                    ]),
                                    id="export-results-btn",
                                    className="btn btn-sm btn-light",
                                    disabled=True
                                ),
                                dcc.Download(id="download-results-csv")
                            ])
                        ], className="bg-info text-white d-flex justify-content-between align-items-center"),
                        dbc.CardBody([
                            dash.dash_table.DataTable(
                                id='results-table',
                                columns=[
                                    {"name": "Sample", "id": "sample"}, 
                                    {"name": "Time", "id": "time"},
                                    {"name": "Label", "id": "label"},
                                    {"name": "Attack Type", "id": "attack_type"},
                                    {"name": "Attack Tool", "id": "tool"}
                                ],
                                data=[],
                                page_size=10,
                                style_table={'overflowX': 'auto'},
                                filter_action="native",
                                sort_action="native",
                                sort_mode="multi",
                                style_cell={
                                    'textAlign': 'center',
                                    'padding': '10px',
                                    'fontFamily': 'Arial'
                                },
                                style_header={
                                    'backgroundColor': '#d1ecf1',
                                    'fontWeight': 'bold',
                                    'border': '1px solid #ddd'
                                },
                                style_data_conditional=[
                                    {
                                        'if': {'row_index': 'odd'},
                                        'backgroundColor': '#f9f9f9'
                                    },
                                    {
                                        'if': {
                                            'filter_query': '{label} = "Malicious"'
                                        },
                                        'backgroundColor': '#ffcccc',
                                        'color': '#990000'
                                    },
                                    {
                                        'if': {
                                            'filter_query': '{label} = "Benign"'
                                        },
                                        'backgroundColor': '#ccffcc',
                                        'color': '#006600'
                                    }
                                ]
                            )
                        ])
                    ], className="mb-4 shadow-sm")
                ], width=12)
            ])
        ], className="container-fluid mt-4"),
        
        # Tooltips
        dbc.Tooltip(
            "Raw traffic data before processing",
            target="initial-traffic-info",
        ),
        dbc.Tooltip(
            "Traffic data after processing and feature extraction",
            target="processed-traffic-info",
        ),
        
        # Modal for monitoring status
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Monitoring Status")),
                dbc.ModalBody(
                    html.Div(id="monitoring-status-content")
                ),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-modal", className="ms-auto", n_clicks=0)
                ),
            ],
            id="monitoring-status-modal",
            size="lg",
            is_open=False,
        ),
        
        # Intervals for updating data
        dcc.Interval(
            id='monitoring-interval',
            interval=1000,  # 1 second
            n_intervals=0,
            disabled=True
        ),
        
        # Store components
        dcc.Store(id='monitoring-data', storage_type='memory'),
        dcc.Store(id='monitoring-state', data={'is_active': False, 'start_time': None}, storage_type='memory')
    ])