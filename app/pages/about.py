from dash import html
import dash_bootstrap_components as dbc

# Navbar (reused from dashboard.py)
navbar = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("5G Dashboard", className="ms-2"),
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Workplace", href="/")),
            dbc.NavItem(dbc.NavLink("Data Overview", href="/data-overview")),
            dbc.NavItem(dbc.NavLink("About", href="/about")),
            dbc.Button(dbc.NavLink("Logout", href="/logout"), id="logout-button", className="btn btn-danger me-2"),
        ], className="ml-auto", navbar=True)
    ]),
    className="navbar-custom mb-4"
)

about_layout = html.Div([
    navbar,
    dbc.Container([
        html.H1("About", className="text-center mb-4"),
        html.P("This is a 5G Network Security Monitoring Dashboard.", className="text-center"),
        html.P("Developed to monitor and analyze network traffic for security threats.", className="text-center"),
        html.P("Version 1.0 | Contact: support@example.com", className="text-center text-muted"),
        dbc.Button("Back to Dashboard", href="/", className="btn btn-primary mt-3")
    ], className="mt-4")
])