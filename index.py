from dash import html, dcc
from dash.dependencies import Input, Output
from app import app
from eda import univariate_analysis, bivariate_analysis
import os


app.layout = html.Div([
    html.H1("Superstore Marketing Dataset EDA Dashboard", style={'textAlign': 'center', 'color':'white', 'backgroundColor': '#66545e', 'font-weight': 'bold'}),    
    html.H2("Univariate and Bivariate Analysis", style={'textAlign': 'center', 'color':'white', 'backgroundColor':'#a39193', 'font-weight': 'bold'}),
    html.P("By Ariba Khan (17270) and Sumbal Bhayo (29400)", style={'textAlign': 'center', 'color':'white', 'font-weight': 'bold'}),
    html.Br(),
    dcc.Location(id='url'),
    html.Div([dcc.Link("Univariate Analysis", href='/eda/univariate_analysis')], style={'textAlign': 'center', 'font-weight': 'bold'}),
    html.Div([dcc.Link("Bivariate Analysis", href='/eda/bivariate_analysis')], style={'textAlign': 'center', 'font-weight': 'bold'}),
    html.Div(id='page_content')
], style={'backgroundColor': '#66545e'})


@app.callback(
    Output('page_content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/eda/univariate_analysis':
        return univariate_analysis.layout
    elif pathname == '/eda/bivariate_analysis':
        return bivariate_analysis.layout
    else:
        return ("This is the home page.")

if __name__ == '__main__':
    app.run_server(debug=True)
