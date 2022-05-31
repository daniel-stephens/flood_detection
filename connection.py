import sqlite3
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import datetime

app = Dash(__name__)
df = pd.DataFrame({
    "frame_number": [],
    "Pixils": []
})

try:

    con = sqlite3.connect('pixils.db')

    cur = con.cursor()
    print("Successfully Connected to SQlite")

    cur.execute("SELECT * FROM vid_pixils order by id desc limit 500")

    rows = cur.fetchall()
    

    for row in rows:
        #print(row)
        df = pd.concat([df, pd.DataFrame({
            'frame_number': [row[1]],
            'Pixils':  [int(row[2])]
            })], axis=0)

    print(df.head())

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



except con.Error as error:
    print("Error while executing sqlite script", error)


@app.callback(Output('graph', 'figure'),
              Input('interval-component', 'n_interval'))

def update_graph(n):
    data = {
        'frame_number': [],
        'pixils': []
    }
    # 
    con = sqlite3.connect('pixils.db')

    cur = con.cursor()
    print("Successfully Connected to SQlite")

    cur.execute("SELECT * FROM vid_pixils order by id desc limit 500")

    rows = cur.fetchall()
    for row in rows:
        #print(row)
        df = pd.concat([df, pd.DataFrame({
            'frame_number': [row[1]],
            'Pixils':  [int(row[2])]
            })], axis=0)
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



# finally:
#     if con:
#         con.close()

if __name__ == '__main__':
    app.run_server(debug=True)