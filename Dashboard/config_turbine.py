"""Dash app to configure a turbine."""

from dash import Dash
from dash.dependencies import Input, State, Output
from .Dash_fun import apply_layout_with_auth, load_object, save_object
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import windesco as we

db = we.db.Database()
url_base = '/dash/config_turbine/'
df = db.turbine_config.get_data(
    cols=["turbine_id", "ts", "yaw_error_adjust_deg"],
    auto_id_index=False,
    auto_ts_index=False,
    auto_turbine_id_multiindex=False,
)

layout = dash_table.DataTable(
    id='turbine-config-table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname=url_base)
    apply_layout_with_auth(app, layout)
    return app.server
