import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from .navigators import BasicNavigator

class FrostedGlassDeck(html.Div):

    def __init__(self, *args, background=None, slides=None, resizable=False, id=None, navigation=None, **kwargs):
        content = html.Div(id=f"{id}-div-slide", children=slides[0])
        card_style = {
            "background-color": "rgba(255, 255, 255, 0.9)",
            "backdrop-filter": "blur(10px)",
            "height": "80vh",
            "width": "142vh",
            "position": "relative",
            "margin": "auto",
            "border-radius": "3px"
        }
        if resizable:
            card_style = {
                **card_style, **{
                    "resize": "both",
                    "overflow": "hidden"
                }
            }
        self.id = id
        self.navigator_id = navigation.id
        super(FrostedGlassDeck, self).__init__(
            *args,
            **kwargs,
            children=dbc.Card(
                children=[dbc.CardBody(content, style={"overflow":"scroll"}), dbc.CardFooter(navigation)],
                style=card_style
            ),
            className="d-flex align-items-center",
            style={
                "background-image":f"url({background})",
                "background-size": "cover",
                "background-repeat": "no-repeat",
                "background-attachment": "fixed",
                "position": "fixed",
                "width": "100%",
                "height": "100%",
                "top": "0px",
                "left": "0px"
            }
        )
        self.slides = slides

    def decorate(self, app):
        @app.callback(
            Output(f"{self.id}-div-slide", 'children'),
            [Input(f"{self.navigator_id}-slider-navigation",'value')]
        )
        def nav_using_slider(value):
            return self.slides[value]


        return nav_using_slider