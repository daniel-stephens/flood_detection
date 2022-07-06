import sqlite3
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import datetime
import dash_bootstrap_components as dbc


app = Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div(children=[
    html.Div(children='DATA ENGINEERING AND PREDICTIVE ANALYTICS LABORATORY'),
    html.Div(children='FLOOD LEVEL INDICATOR'),
    dcc.Graph(id='graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0)
])



@app.callback(Output('graph', 'figure'),
              Input('interval-component', 'n_intervals'))

def update_graph(n):
    data = {
        'frame_number': [],
        'pixils': []
    }
    df = pd.DataFrame(data)
    # 
    con = sqlite3.connect('pixils.db')

    cur = con.cursor()
    print("Successfully Connected to SQlite")

    cur.execute("SELECT * FROM vid_pixils order by id desc limit 3000")

    rows = cur.fetchall()
    for row in rows:
        #print(row)
        dat = pd.DataFrame({
            'frame_number': [row[1]],
            'Pixils':  [int(row[2])]
            })
        df = pd.concat([df, dat], axis=0)
    fig = px.line(df, x="frame_number", y='Pixils')

    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
           FLOOD LEVEL INDICATOR
        '''),

        dcc.Graph(
            id='graph',
            figure=fig
    ),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
    
    con.close()

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
