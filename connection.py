import sqlite3
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

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
        df = pd.concat([df, {
            'frame_number': [row[0]],
            'Pixils':  [int(row[1])]
            }], axis=0)

    print(df.head())

    fig = px.line(df, x="frame_number", y='Pixils')

    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
    )
])



except con.Error as error:
    print("Error while executing sqlite script", error)


# Create table
# cur.execute('''CREATE TABLE vid_pixils
#                (pixil_number, pixils)''')


finally:
    if con:
        con.close()

# if __name__ == '__main__':
#     app.run_server(debug=True)