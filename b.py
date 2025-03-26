import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px 
import pandas as pd 

app = dash.Dash(__name__)


data = {
    'area' : [100,200,300,400,500,600,700,800,900,850,950],
    'cost' : [50,60,80,55,70,90,800,500,400,600,700]
}


df = pd.DataFrame(data)

app.layout = html.Div([html.H1('My Applaction'),
html.H2('Area & Cost Graph'),
dcc.Dropdown(
    id = 'graph_type',
    options = [
        {'label': 'Line plot','value' : 'line'},
        {'label': 'Bar plot', 'value' : 'bar'},
        {'label': 'Scatter Plot','value' : 'scatter'},
    ]
),
dcc.Graph(id = 'graph')],

style={'textAlign': 'center',
'color':'red',
'backgroundColor':'loghtblue'})

@app.callback(
    Output('graph','figure'),
    [Input('graph_type','value')]
)

def update_graph(graph_type):
    if graph_type == 'line':
        fig = px.line(df, x = 'area', y='cost')
    elif graph_type == 'bar':
        fig = px.bar(df, x = 'area', y='cost')
    else:
        fig = px.scatter(df, x = 'area', y='cost')
    return fig

app.run(debug=True)