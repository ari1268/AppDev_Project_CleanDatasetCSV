import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from scipy.stats import shapiro
import numpy as np
from dash.dependencies import Input, Output
import seaborn as sns 
from app import app, data

# 'Income', 'Recency', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases'
# 'NumStorePurchases', 'NumWebVisitsMonth', 'Age', 'Count_Children', 'Total_Value'

numeric_variable_options = [{'label': "Income", 'value': 'Income'}, {'label': "Age", 'value': 'Age'}, \
                            {'label': "Count_Children", 'value': 'Count_Children'}, \
                            {'label': "NumDealsPurchases", 'value': 'NumDealsPurchases'}, \
                            {'label': "NumCatalogPurchases", 'value': 'NumCatalogPurchases'}, \
                            {'label': "NumStorePurchases", 'value': 'NumStorePurchases'}, \
                            {'label': "NumWebPurchases", 'value': 'NumWebPurchases'}, \
                            {'label': "NumWebVisitsMonth", 'value': 'NumWebVisitsMonth'}, \
                            {'label': "Total_Value", 'value': 'Total_Value'}, \
                            {'label': "Recency", 'value': 'Recency'}]


layout = html.Div([
    html.H2(children = "Univariate Analysis", style={'textAlign': 'center', 'color':'white', 'backgroundColor':'#aa6f73', 'font-weight': 'bold'}),
    html.Hr(),
    html.H3(children = "Numerical Attributes", style={'textAlign': 'center', 'color':'white'}),
    html.Br(),
    html.Div([dcc.Dropdown(id = 'numeric-univariate-analysis',
                 options = numeric_variable_options,
                 value = 'Income'),
    dcc.Graph(id = 'box_plot'),
    dcc.Graph(id = 'kde_plot')], style = {'backgroundColor': '#f6e0b5'}),
    html.Br(),
    html.H3(children = "Categorical Attributes", style={'textAlign': 'center', 'color':'white'}),
    html.Br(),
    html.Div([dcc.Dropdown(id = 'categoric-univariate-analysis',
                 options = [{'label': 'Education', 'value': 'Education'},
                            {'label': 'Marital_Status', 'value': 'Marital_Status'}],
                 value = 'Education'),
    dcc.Graph(id = 'bar_plot'),
    dcc.Graph(id = 'pie_plot')], style = {'backgroundColor': '#f6e0b5'})
])

@app.callback(
    Output(component_id = 'box_plot', component_property = 'figure'),
    Output(component_id = 'kde_plot', component_property = 'figure'),
    Input(component_id = 'numeric-univariate-analysis', component_property = 'value')
)

def update_numeric_plots(selected_variable):
    box_plot = px.box(data, y=selected_variable, title=f'Box Plot for {selected_variable}')
    kde_plot = px.histogram(data, x=selected_variable, marginal='rug', histnorm='probability density')
    kde_plot.update_layout(title_text=f'KDE Plot for {selected_variable}')
    return box_plot, kde_plot

@app.callback(
    Output(component_id = 'bar_plot', component_property = 'figure'),
    Output(component_id = 'pie_plot', component_property = 'figure'),
    Input(component_id = 'categoric-univariate-analysis', component_property = 'value')
)

def update_categorical_plots(selected_variable):
    bar_plot = px.bar(data, x=selected_variable, title=f'Bar Plot for {selected_variable}')
    pie_plot = px.pie(data, names=selected_variable, title=f'Pie Chart for {selected_variable}')
    return bar_plot, pie_plot