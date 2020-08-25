import dash_bootstrap_components as dbc

# how do I remove the children argument ignore the children argument
def slide_children_error(class_name, **kwargs):
    if "children" in kwargs.keys():
        raise TypeError(
"""The `{class_name}` component received an unexpected keyword argument: `children`
Allowed arguments: align, left, right, className, form, id, justify, key, loading_state, no_gutters, style"""
            )

class OneContentSlide(dbc.Container):
    def __init__(self, *args, title=None, content=None, **kwargs):
        slide_children_error("OneContentSlide", **kwargs)
        super(OneContentSlide, self).__init__(
            *args,
            **kwargs,
            children=[
                dbc.Row(dbc.Col(title)),
                dbc.Row(dbc.Col(content))
            ],
            style={"overflow":"scroll"}
        )

class TwoContentSlide(dbc.Container):
    def __init__(self, *args, title=None, left=None, right=None, **kwargs):
        slide_children_error("TwoContentSlide", **kwargs)
        super(TwoContentSlide, self).__init__(
            *args,
            **kwargs,
            children=[
                dbc.Row(dbc.Col(title)),
                dbc.Row([
                    dbc.Col(width=6, children=left),
                    dbc.Col(width=6, children=right)
                ])
            ]
        )