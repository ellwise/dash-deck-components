from dash_deck_components import FrostedGlassDeck, BasicNavigator

from app import app
from slides import slides

navigator = BasicNavigator(num_slides=len(slides), id="bn")
deck = FrostedGlassDeck(slides=slides, background="assets/bg.jpg", resizable=True, id="fgd", navigation=navigator)
navigator.decorate(app)
deck.decorate(app)

app.title = "Dash Deck Components Demo"
app.layout = deck
app.config.suppress_callback_exceptions = True # this allows us to place callbacks in their own files

if __name__=="__main__":
    app.run_server(debug=True, host="0.0.0.0", port="8000")