import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

class BasicNavigator(dbc.Container):

    def __init__(self, *args, num_slides=None, id=None, **kwargs):
        nav_slider = html.Div(
            style={"margin-bottom":"-25px"}, # the slider has a hard-coded padding at the bottom, this div wrapper counteracts it
            children=dcc.Slider(
                id=f"{id}-slider-navigation",
                min=0,
                max=num_slides-1,
                step=1,
                value=0,
                marks={j:"" for j in range(num_slides)}
            )
        )
        left_buttons = dbc.ButtonGroup(
            children=[
                dbc.Button(id=f"{id}-first-navigation", color="info", outline=True, size="sm", children="<<"),
                dbc.Button(id=f"{id}-prev-navigation", color="info", outline=True, size="sm", children="<")
            ]
        )
        right_buttons = dbc.ButtonGroup(
            children=[
                dbc.Button(id=f"{id}-next-navigation", color="info", outline=True, size="sm", children=">"),
                dbc.Button(id=f"{id}-last-navigation", color="info", outline=True, size="sm", children=">>")
            ]
        )
        self.id = id
        super(BasicNavigator, self).__init__(
            *args,
            **kwargs,
            children=dbc.Row(
                className="d-flex",
                align="center",
                justify="around",
                children=[
                    dbc.Col(width="auto", children=left_buttons),
                    dbc.Col(width="auto", className="flex-fill", children=nav_slider),
                    dbc.Col(width="auto", children=right_buttons)
                ]
            )
        )

    def decorate(self, app):
        
        @app.callback(
            Output(f"{self.id}-slider-navigation","value"),
            [Input(f"{self.id}-{component}-navigation","n_clicks") for component in ["first","prev","next","last"]],
            [State(f"{self.id}-slider-navigation",prop) for prop in ["value","min","max","step"]]
        )
        def nav_using_buttons(first_press, prev_press, next_press, last_press, val, mn, mx, step):
            if all(press is None for press in [first_press, prev_press, next_press, last_press]):
                raise PreventUpdate
            ctx = dash.callback_context
            triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
            if triggered_id==f"{self.id}-first-navigation":
                return mn
            elif triggered_id==f"{self.id}-prev-navigation":
                return max(mn,val-step)
            elif triggered_id==f"{self.id}-next-navigation":
                return min(mx,val+step)
            elif triggered_id==f"{self.id}-last-navigation":
                return mx

        return nav_using_buttons
