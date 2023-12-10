import dash
import pandas as pd

data = pd.read_csv('/home/appdevproject1727029400/dashapp/clean_dataset2.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets)

