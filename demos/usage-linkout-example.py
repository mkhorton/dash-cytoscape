"""
Original Demo: http://js.cytoscape.org/demos/linkout-example/
Original Code: https://github.com/cytoscape/cytoscape.js/blob/master/documentation/demos/linkout-example/

Note: Href Links do not work

"""
import dash_cytoscape
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import json

app = dash.Dash(__name__)
server = app.server

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

elements = [
    {'data': {'id': 'desktop', 'name': 'Cytoscape',
              'href': 'http://cytoscape.org'}},
    {'data': {'id': 'js', 'name': 'Cytoscape.js',
              'href': 'http://js.cytoscape.org'}},
    {'data': {'source': 'desktop', 'target': 'js'}}
]

# App
app.layout = html.Div([
    dash_cytoscape.Cytoscape(
        id='cytoscape',
        elements=elements,
        boxSelectionEnabled=False,
        autounselectify=True,
        layout={
            'name': 'grid',
            'padding': 10
        },
        stylesheet=[{
            'selector': 'node',
            'style': {
                'content': 'data(name)',
                'text-valign': 'center',
                'color': 'white',
                'text-outline-width': 2,
                'text-outline-color': '#888',
                'background-color': '#888'
            }
        }, {
            'selector': ':selected',
            'style': {
                'background-color': 'black',
                'line-color': 'black',
                'target-arrow-color': 'black',
                'source-arrow-color': 'black',
                'text-outline-color': 'black'
            }
        }],
        style={
            'width': '100%',
            'height': '100%',
            'position': 'absolute',
            'left': 0,
            'top': 0
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
