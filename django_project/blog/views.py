from django.shortcuts import render
from .models import Post, Hist
from django.contrib.auth.models import User
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components


import plotly.graph_objects as go
import plotly.offline

# ------------------------------------------------
# data = pd.read_csv('blog/hdata.csv')
# data["Date"]=pd.to_datetime(data["Date"])
# data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
# # for col in data.columns:
# #     data[col] = data[col].astype(float)
# def make_float(col):
#     data[col].replace(',','', regex=True, inplace=True)
#     data[col] = data[col].astype(float)
#
# make_float('Open')
# make_float('High')
# make_float('Low')
# make_float('Close')
# make_float('AdjClose')
# make_float('Volume')
# print(data.info())
# for row in range(data['Date'].count()):
#     # for col in range(len(data.columns)):
#     hdata = Hist(
#     Date = data.iloc[row][0],
#     Open = data.iloc[row][1],
#     High = data.iloc[row][2],
#     Low = data.iloc[row][3],
#     Close = data.iloc[row][4],
#     AdjClose = data.iloc[row][5],
#     Volume = data.iloc[row][6]
#     )
#     hdata.save()
#     # Volume = data.iloc[row][6]
#     # print(Volume)
#
# print('done')
#----------------------------------------------------


h_orm = Hist.objects.values()
df = pd.DataFrame(h_orm)

# '2.3.0'


def home(request):
    fig = go.Figure(
        data=[go.Bar(x=['kamis', 'kel'],y=[15, 3])],
        layout_title_text="Measuring personal parts (inches)"
    )

    graph_div = plotly.offline.plot(fig, auto_open=False, output_type="div")

    context = {
        'posts': Post.objects.all(),
        'title': 'Home',
        'graph_div': graph_div
    }



    return render(request, 'blog/home.html', context)

def about(request):


    x = [1,2,3,4,5]
    y = [1, 2, 3, 4, 5]

    plot = figure(title= 'Line Graph', x_axis_label='X-axis', y_axis_label='Y-Axis', plot_width=400, plot_height=400)
    plot.line(x,y,line_width=2)
    script, div = components(plot)


    context = {
        'script': script,
        'div': div,
    }

    return render(request, 'blog/about.html', context)


# Twforsure1