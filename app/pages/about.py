from dash import html
import dash_bootstrap_components as dbc
from components.navbar import create_navbar

def create_about_layout(username):
    return html.Div([
        create_navbar(username),
        dbc.Container([
            dbc.Row([
                # Cột trái
                dbc.Col([
                    # --- Giới thiệu ---
                    dbc.Card([
                        dbc.CardBody([
                            html.H2("1. Giới thiệu", className="text-primary mb-3 text-center"),
                            html.P(
                                "- 5G Network Dashboard là một hệ thống giám sát và phân tích mạng 5G toàn diện, được thiết kế để cung cấp cái nhìn tổng quan về hiệu suất, bảo mật và hoạt động của hệ thống mạng 5G.",
                            ),
                            html.P(
                                "- Hệ thống cho phép các quản trị viên mạng theo dõi thời gian thực các chỉ số quan trọng, phát hiện và cảnh báo các mối đe dọa bảo mật, cũng như phân tích xu hướng sử dụng mạng."
                            )
                        ])
                    ], className="shadow-sm mb-4"),

                    # --- Tính năng chính ---
                    dbc.Card([
                        dbc.CardBody([
                            html.H2("2. Tính năng chính", className="text-primary text-center mb-4"),
                            dbc.Row([
                                dbc.Col([
                                    html.Div([
                                        html.I(className="fas fa-chart-line fa-2x text-success mb-2"),
                                        html.H6("Giám sát thời gian thực", className="text-primary"),
                                        html.P("Theo dõi lưu lượng mạng, hiệu suất và các chỉ số khác trong thời gian thực.", 
                                              className="small")
                                    ], className="text-center")
                                ], width=4),

                                dbc.Col([
                                    html.Div([
                                        html.I(className="fas fa-shield-alt fa-2x text-warning mb-2"),
                                        html.H6("Cảnh báo bảo mật", className="text-primary"),
                                        html.P("Phát hiện và cảnh báo sớm các mối đe dọa bảo mật và hoạt động bất thường.",
                                              className="small")
                                    ], className="text-center")
                                ], width=4),

                                dbc.Col([
                                    html.Div([
                                        html.I(className="fas fa-chart-area fa-2x text-info mb-2"),
                                        html.H6("Phân tích dữ liệu", className="text-primary"),
                                        html.P("Phân tích xu hướng, tạo báo cáo và cung cấp insights để tối ưu hóa mạng.",
                                              className="small")
                                    ], className="text-center")
                                ], width=4),
                            ])
                        ])
                    ], className="shadow-sm")
                ], width=6),

                dbc.Col([
                    # --- Thông tin kỹ thuật ---
                    dbc.Card([
                        dbc.CardBody([
                            html.H2("3. Công nghệ", className="text-primary text-center mb-4"),
                            dbc.Row([
                                dbc.Col([
                                    html.I(className="fas fa-cloud-meatball fa-2x text-info mb-1 mt-3"),
                                    html.H6("Triển khai", className="text-secondary"),
                                    html.P("Docker, k8s", className="fw-bold")
                                ], width=3),
                                dbc.Col([
                                    html.I(className="fas fa-laptop-code fa-2x text-info mb-1 mt-3"),
                                    html.H6("Framework", className="text-secondary"),
                                    html.P("Python, Dash, Plotly", className="fw-bold")
                                ], width=3),
                                dbc.Col([
                                    html.I(className="fas fa-database fa-2x text-info mb-1 mt-3"),
                                    html.H6("Cơ sở dữ liệu", className="text-secondary"),
                                    html.P("sqlalchemy - SQLite3", className="fw-bold")
                                ], width=3),
                                dbc.Col([
                                    html.I(className="fas fa-sync fa-2x text-info mb-1 mt-3"),
                                    html.H6("Cập nhật lần cuối", className="text-secondary"),
                                    html.P("May 2025", className="fw-bold")
                                ], width=3),
                            ]), 
                        ])
                    ], className="shadow-sm mb-4"),

                    # --- Liên hệ hỗ trợ ---
                    dbc.Card([
                        dbc.CardBody([
                            html.H2("4. Liên hệ", className="text-primary mb-4 text-center"),
                            dbc.Row([
                                dbc.Col([
                                    html.Div([
                                        html.I(className="fas fa-envelope fa-2x text-primary mb-2"),
                                        html.H6("Email"),
                                        html.P("22520471@gm.uit.edu.vn 22520143@gm.uit.edu.vn", className="small"),
                                    ], className="text-center")
                                ], width=4),

                                dbc.Col([
                                    html.Div([
                                        html.I(className="fas fa-phone fa-2x text-primary mb-2"),
                                        html.H6("Hotline"),
                                        html.P("(028) 372 52002", className="small")
                                    ], className="text-center")
                                ], width=4),

                                dbc.Col([
                                    html.Div([
                                        html.I(className="fas fa-globe fa-2x text-primary mb-2"),
                                        html.H6("Website"),
                                        html.P("https://www.uit.edu.vn/", className="small")
                                    ], className="text-center")
                                ], width=4),
                            ])
                        ])
                    ], className="shadow-sm")
                ], width=6)
            ], className="g-4 mt-5"),

            # --- Nút quay về Dashboard ---
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dbc.Button(
                            [html.I(className="fas fa-arrow-left me-2"), "Quay về Dashboard"],
                            href="/dashboard",
                            color="primary",
                            size="lg",
                            className="shadow"
                        )
                    ], className="text-center")
                ], width=5)
            ], className="mt-5 mb-3 justify-content-center")

        ], fluid=True, className="py-3 mt-5 bg-white"),
], style={"height": "100%", "width": "100vw"})