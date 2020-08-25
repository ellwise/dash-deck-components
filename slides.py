import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

from dash_deck_components import OneContentSlide, TwoContentSlide

slide1 = TwoContentSlide(
    title=html.H1("Headings and emphasis"),
    left=dcc.Markdown(
"""
# H1
## H2
### H3
#### H4
##### H5
###### H6
"""
    ),
    right=dcc.Markdown(
"""
Emphasis (italics) using *asterisks* or _underscores_.

Strong emphasis (bold) using **asterisks** or __underscores__.

Combinations using **asterisks and _underscores_**.

Strikethrough using two tildes: ~~struck through.~~
"""
    )
)

slide2 = OneContentSlide(
    title=html.H1("Lists"),
    content=dcc.Markdown(
"""
1. First item
2. Second item
  * Unordered sub-item
  1. Ordered sub-item

* An unordered list can use asterisks
- or minus symbols
+ or plus symbols
"""
    )
)

slide3 = TwoContentSlide(
    title=html.H1("Sunburst"),
    left=dcc.Markdown(
"""
The following is quoted from the Plotly documentation, which can be accessed [here](https://plotly.com/python/sunburst-charts/).

Sunburst plots visualize hierarchical data spanning outwards radially from root to leaves. The sunburst sector hierarchy is determined by the entries in `labels` (`names` in `px.sunburst`) and in `parents`. The root starts from the center and children are added to the outer rings.

Main arguments:

1. `labels` (`names` in `px.sunburst` since `labels` is reserved for overriding columns names): sets the labels of sunburst sectors.
2. `parents`: sets the parent sectors of sunburst sectors. An empty string `''` is used for the root node in the hierarchy. In this example, the root is "Eve".
3. `values`: sets the values associated with sunburst sectors, determining their width (See the `branchvalues` section below for different modes for setting the width).

"""
    ),
    right=dcc.Graph(
        figure=px.sunburst(
            dict(
                character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
                parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
                value=[10, 14, 12, 10, 2, 6, 6, 4, 4]),
            names='character',
            parents='parent',
            values='value',
            template="none"
        ).update_layout(
            dict(
                margin={"l":0,"r":0,"t":0,"b":0},
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)"
            )
        )
    )
)

slides = [slide1, slide2, slide3]