from cgitb import small
import sqlite3
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


small_card = {
         'background-color': '#426793',
        'width': '100%',
        'height':'20%'}

big_card = dbc.CardBody(style={
         'background-color': '#426793',
        'width': '75%',
        'height':'100%',
        'display': 'inline-block'
})



footer =  dbc.CardBody(style={
        'background-color': '#426793',
        'height':'100%',
        'width':'50%'
    })

data = {
    'frame_number': [],
    'pixils': []
}
df = pd.DataFrame(data)
# 
con = sqlite3.connect('C:\\Users\\daste19\\Desktop\\projects\\flood_pred\\database.db')

cur = con.cursor()
print("Successfully Connected to SQlite")

cur.execute("SELECT * FROM vid_pixils order by id desc limit 3000")

rows = cur.fetchall()
for row in rows:
    #print(row)
    dat = pd.DataFrame({
        'frame_number': [row[1]],
        'pixils':  [int(row[2])]
        })
    df = pd.concat([df, dat], axis=0)
    
fig = px.line(df, x="frame_number", y='pixils')
last = df.iloc[-1]
con.close()



app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    html.Br(),
    dbc.Row([
        html.Div(
            html.H3('DATA ENGINEERING AND PREDICTIVE ANALYTICS LAB'),
            style = {
                'text-align': 'center'
            }
        ),
        html.Div(
            html.H4('FLOOD DETECTION DASHBOARD'),
            style = {
                'text-align': 'center'
            }
        )
    ]),
    html.Br(),
    html.Div([html.Br(),
            html.Div([
                dbc.CardBody([html.H5('AVG. WATER VOLUME:'),
                              html.H5(id = 'water_level',children="1214563")],style=small_card),
                dbc.CardBody([html.H5('LOCATION:'),
                              html.H5(id = 'location',children="ELLICOT CITY")],style=small_card),
                dbc.CardBody([html.H5('TIME:'),
                              html.H5(id = 'Time',children="20:21:03")],style=small_card),
                dbc.CardBody([html.H5('DATE:'),
                              html.H5('06/29/2022')],style=small_card)
                    ], style={
                        'background-color': 'black',
                        'width': '22%',
                        'height':'100%',
                        'display':'flex',
                        'flex-direction':'column',
                        'justify-content':'space-between',
                        'padding':'0.5rem',
                        'gap': '0.5rem'
                        
                    }),
            dbc.CardBody([
                dcc.Graph(id ='graph', figure=fig,
                style={
                        # 'background-color': '#426793',
                        'width': '96.5%',
                        'height':'100%'
                    }), 
                dcc.Interval(
                id='interval-component',
                interval=1*1000, # in milliseconds
                n_intervals=0)],
                        style={
                        'background-color': 'black',
                        'width': '75%',
                        'height':'100%'
            })

                
            ], style={
        'background-color': 'yellow',
        'width': '100%',
        'height':'33rem',
        'display':'flex',
        'align-items':'center'
    }),
    html.Footer([footer, footer],style={
        'background-color': 'black',
        'width': '100%',
        'height':'11rem',
        'display':'flex',
        'flex-direction':'row',
        'gap':'0.5rem',
        'padding':'0.5rem'
        
    })
], style={
    'background_color':'black'
})

@app.callback([Output('graph', 'figure'),
                Output('water_level', 'children') ],
              [Input('interval-component', 'n_intervals')])

def update_graph(n):
    data = {
        'frame_number': [],
        'pixils': []
    }
    df = pd.DataFrame(data)
    # 
    con = sqlite3.connect('C:\\Users\\daste19\\Desktop\\projects\\flood_pred\\database.db')

    cur = con.cursor()
    print("Successfully Connected to SQlite")

    cur.execute("SELECT * FROM vid_pixils order by id desc limit 3000")

    rows = cur.fetchall()
    con.close()
    for row in rows:
        #print(row)
        dat = pd.DataFrame({
            'frame_number': [row[1]],
            'pixils':  [int(row[2])]
            })
        df = pd.concat([df, dat], axis=0)
        
    fig = px.line(df, x="frame_number", y='pixils')
    last = df.iloc[-1]
    

    # app.layout = html.Div(children=[
    #     html.H1(children='Sample Dashboard'),

    #     html.Div(children='''
    #        FLOOD LEVEL INDICATOR
    #     '''),

    #         dcc.Graph(
    #             id='graph',
    #             figure=fig
    #         ),
    #     dcc.Interval(
    #         id='interval-component',
    #         interval=1*1000, # in milliseconds
    #         n_intervals=0
    #     )
    # ])



    

    
    

    return (fig, last[1])





if __name__ == '__main__':
    app.run_server(debug=True)
