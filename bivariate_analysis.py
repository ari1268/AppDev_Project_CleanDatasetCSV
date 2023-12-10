import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from app import app, data

# Demographic Attributes

def marital_status_response_countplot():
    fig = px.histogram(data, x='Marital_Status', color='Response', barmode='group', title='Marital_Status vs. Response')
    return fig

def education_response_countplot():
    fig = px.histogram(data, x='Education', color='Response', barmode='group', title='Education vs. Response')
    return fig

def income_response_boxplot():
    fig = px.box(data, x='Response', y='Income', title='Income vs. Response')
    return fig

def income_total_value_scatterplot():
    fig = px.scatter(data, x='Income', y='Total_Value', color='Response', title='Income vs. Total_Value')
    return fig

def age_total_value_scatterplot():
    fig = px.scatter(data, x='Age', y='Total_Value', color='Response', title='Age vs. Total_Value')
    return fig

def count_children_response_boxplot():
    fig = px.box(data, x='Response', y='Count_Children', title='Count_Children vs. Response')
    return fig

# fig = px.imshow(z, text_auto=True)

def education_response_heatmap():
    contingency_table = pd.crosstab(data['Education'], data['Response'])
    fig = px.imshow(contingency_table, text_auto=True)
    return fig

def marital_status_response_heatmap():
    contingency_table = pd.crosstab(data['Marital_Status'], data['Response'])
    fig = fig = px.imshow(contingency_table, text_auto=True)
    return fig

# Purchasing Behaviour Attributes

def num_deals_response_boxplot():
    fig = px.box(data, x='Response', y='NumDealsPurchases', title='NumDealsPurchases vs. Response')
    return fig

def num_catalog_response_boxplot():
    fig = px.box(data, x='Response', y='NumCatalogPurchases', title='NumCatalogPurchases vs. Response')
    return fig

def num_web_response_boxplot():
    fig = px.box(data, x='Response', y='NumWebPurchases', title='NumWebPurchases vs. Response')
    return fig

def num_store_response_boxplot():
    fig = px.box(data, x='Response', y='NumStorePurchases', title='NumStorePurchases vs. Response')
    return fig

def num_web_visits_response_boxplot():
    fig = px.box(data, x='Response', y='NumWebVisitsMonth', title='NumWebVisitsMonth vs. Response')
    return fig

def recency_response_boxplot():
    fig = px.box(data, x='Response', y='Recency', title='Recency vs. Response')
    return fig

def total_value_response_boxplot():
    fig = px.box(data, x='Response', y='Total_Value', title='Total_Value vs. Response')
    return fig

# Layout

layout = html.Div([
    html.H2(children="Bivariate Analysis", style={'textAlign': 'center', 'color':'white', 'backgroundColor':'#aa6f73', 'font-weight': 'bold'}),
    html.Hr(),

    html.H3(children="Demographic Attributes", style={'textAlign': 'center', 'color':'white'}),
    html.Br(),

    dcc.Dropdown(id='demographic-chart-selector',
                 options=[
                     {'label': 'Marital_Status vs. Response', 'value': 'marital_status_response_countplot'},
                     {'label': 'Education vs. Response', 'value': 'education_response_countplot'},
                     {'label': 'Income vs. Response', 'value': 'income_response_boxplot'},
                     {'label': 'Income vs. Total_Value', 'value': 'income_total_value_scatterplot'},
                     {'label': 'Age vs. Total_Value', 'value': 'age_total_value_scatterplot'},
                     {'label': 'Count_Children vs. Response', 'value': 'count_children_response_boxplot'},
                     {'label': 'Education vs. Response (Heatmap)', 'value': 'education_response_heatmap'},
                     {'label': 'Marital_Status vs. Response (Heatmap)', 'value': 'marital_status_response_heatmap'},
                 ],
                 value='marital_status_response_countplot'),

    dcc.Graph(id='demographic-chart'),

    html.H3(children="Purchasing Behaviour Attributes", style={'textAlign': 'center', 'color':'white'}),
    html.Br(),

    dcc.Dropdown(id='purchasing-chart-selector',
                 options=[
                     {'label': 'NumDealsPurchases vs. Response', 'value': 'num_deals_response_boxplot'},
                     {'label': 'NumCatalogPurchases vs. Response', 'value': 'num_catalog_response_boxplot'},
                     {'label': 'NumWebPurchases vs. Response', 'value': 'num_web_response_boxplot'},
                     {'label': 'NumStorePurchases vs. Response', 'value': 'num_store_response_boxplot'},
                     {'label': 'NumWebVisitsMonth vs. Response', 'value': 'num_web_visits_response_boxplot'},
                     {'label': 'Recency vs. Response', 'value': 'recency_response_boxplot'},
                     {'label': 'Total_Value vs. Response', 'value': 'total_value_response_boxplot'},
                 ],
                 value='num_deals_response_boxplot'),

    dcc.Graph(id='purchasing-chart')
])

@app.callback(
    Output(component_id='demographic-chart', component_property='figure'),
    Input(component_id='demographic-chart-selector', component_property='value')
)

def update_demographic_chart(selected_chart):
    return globals()[selected_chart]()

@app.callback(
    Output(component_id='purchasing-chart', component_property='figure'),
    Input(component_id='purchasing-chart-selector', component_property='value')
)

def update_purchasing_chart(selected_chart):
    return globals()[selected_chart]()