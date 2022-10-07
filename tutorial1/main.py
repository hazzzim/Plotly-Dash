#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 11:34:11 2022

@author: hazim
"""
#importing plotly necessary libraries


import dash
import dash_core_components as dcc
import dash_html_components as html

# %%

app = dash.Dash()

app.layout = html.Div([
    html.H1("Hellow Dash!"),
    html.Div("Dash- A Data product development from Plotly")
    ])



if __name__ =='__main__':
    app.run_server(port=4050)
    