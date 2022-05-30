import glob
import pandas as pd
import numpy as np
import cv2
import plotly.graph_objects as go
import os


# initialise dataframe and figure
df = pd.DataFrame({"frame_number":[], "pixils":[]})
fig = go.Figure(data=go.Line(x=df.frame_number,
                                y=df.pixils))

def update_graphs(i, fig):
    global df
    images = sorted(glob.glob(f"{os.getcwd()}\\background\\*jpg"), key=len)
    roi = (40, 5, 180, 159)
    n = 0

    for image in images:
        img_raw = cv2.imread(image)
        #Crop selected roi from raw image
        roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
        num = np.sum(roi_cropped)
        df = pd.concat([df, pd.DataFrame({"frame_number": n, 'pixils' : num})])
        n+=1

        return go.Figure(fig).update_traces(go.Line(x=df.frame_number, y=df.pixils))
 

def update_graph(image, n, fig):
    global df
    
