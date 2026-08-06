import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX launch data
spacex_df = pd.read_csv("datasets/dataset_part_2.csv")
max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Dropdown for Launch Site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
        ],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    html.Br(),

    # TASK 2: Pie chart for success count
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    
    # TASK 3: Range Slider for Payload selection
    dcc.RangeSlider(
        id='payload-slider',
        min=0, max=10000, step=1000,
        marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
        value=[min_payload, max_payload]
    ),

    # TASK 4: Scatter plot for Payload vs. Success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2 Callback: Pie Chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='Class', 
                     names='LaunchSite', 
                     title='Total Successful Launches By Site')
        return fig
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
        fig = px.pie(filtered_df, names='Class', 
                     title=f'Total Success vs Failure Launches for site {entered_site}')
        return fig

# TASK 4 Callback: Scatter Plot
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_plot(entered_site, payload_range):
    low, high = payload_range
    mask = (spacex_df['PayloadMass'] >= low) & (spacex_df['PayloadMass'] <= high)
    filtered_df = spacex_df[mask]
    
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='PayloadMass', y='Class', 
                         color='BoosterVersion',
                         title='Correlation between Payload and Success for All Sites')
        return fig
    else:
        site_filtered = filtered_df[filtered_df['LaunchSite'] == entered_site]
        fig = px.scatter(site_filtered, x='PayloadMass', y='Class', 
                         color='BoosterVersion',
                         title=f'Correlation between Payload and Success for site {entered_site}')
        return fig

if __name__ == '__main__':
    app.run_server(debug=True)
