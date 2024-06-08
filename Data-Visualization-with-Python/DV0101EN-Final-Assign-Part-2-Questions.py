
import dash
# import more_itertools
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv(r'jupyter-notebooks/Data-Visualization-with-Python/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Automobile Sales Statistics Dashboard"  # Set the title of the Dash application

# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Automobile Sales Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Statistics'}
]

# List of years from 1980 to 2013
year_list = [i for i in range(1980, 2014)]

# Create the layout of the app
app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard", 
            style={'textAlign': 'center', 'color': '#50336', 'font-size': '24px'}),  # Center aligned heading with specific color and font size
    html.Div([
        html.Label("Select Report Type:"),
        dcc.Dropdown(
            id='select-statistics',
            options=dropdown_options,
            value='Yearly Statistics',
            clearable=False,
            style={'width': '50%'}
        )
    ], style={'padding': '20px'}),
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value=year_list[0],
            clearable=False,
            style={'width': '50%'}
        )
    ], style={'padding': '20px'}),
    html.Div(id='output-container', className='output-container', style={'padding': '20px'})
])

# Define the callback function to update the output container based on the selected statistics
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='select-statistics', component_property='value'),
     Input(component_id='select-year', component_property='value')]
)
def update_output_container(selected_statistics, selected_year):
    if selected_statistics == 'Recession Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        # Implement further plotting logic here
        return html.Div("Recession Statistics will be shown here.")
    elif selected_statistics == 'Yearly Statistics':
        # Further logic for Yearly Statistics
        return html.Div("Yearly Statistics will be shown here.")
    else:
        return html.Div("Please select a report type.")



#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
# @app.callback(
#     Output(component_id='...', component_property='...'),
#     [Input(component_id='...', component_property='...'), Input(component_id='...', component_property='...')])


# def update_output_container(....., .....):
#     if ..... == 'Recession Period Statistics':
#         # Filter the data for recession periods
#         recession_data = data[data['Recession'] == 1]
        
# #TASK 2.5: Create and display graphs for Recession Report Statistics

# #Plot 1 Automobile sales fluctuate over Recession Period (year wise)
#         # use groupby to create relevant data for plotting
#         yearly_rec=recession_data.groupby('...')['...'].mean().reset_index()
#         R_chart1 = dcc.Graph(
#             figure=px......(....., 
#                 x='....',
#                 y='......',
#                 title="Average Automobile Sales fluctuation over Recession Period"))

# #Plot 2 Calculate the average number of vehicles sold by vehicle type       
#         # use groupby to create relevant data for plotting
#         average_sales = ...............mean().reset_index()                           
#         R_chart2  = dcc.Graph(figure=px....................
        
# # Plot 3 Pie chart for total expenditure share by vehicle type during recessions
#         # use groupby to create relevant data for plotting
#         exp_rec= ....................
#         R_chart3 = .............

# # Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
#         ................
#         ...................


#         return [
#             html.Div(className='..........', children=[html.Div(children=R_chart1),html.Div(children=.....)],style={.....}),
#             html.Div(className='chart-item', children=[html.Div(children=...........),html.Div(.............)],style={....})
#             ]

# # TASK 2.6: Create and display graphs for Yearly Report Statistics
#  # Yearly Statistic Report Plots                             
#     elif (input_year and selected_statistics=='...............') :
#         yearly_data = data[data['Year'] == ......]
                              
# #TASK 2.5: Creating Graphs Yearly data
                              
# #plot 1 Yearly Automobile sales using line chart for the whole period.
#         yas= data.groupby('Year')['Automobile_Sales'].mean().reset_index()
#         Y_chart1 = dcc.Graph(figure=px.line(.................))
            
# # Plot 2 Total Monthly Automobile sales using line chart.
#         Y_chart2 = dcc.Graph(................)

#             # Plot bar chart for average number of vehicles sold during the given year
#         avr_vdata=yearly_data.groupby........................
#         Y_chart3 = dcc.Graph( figure.................,title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))

#             # Total Advertisement Expenditure for each vehicle using pie chart
#         exp_data=yearly_data.groupby(..................
#         Y_chart4 = dcc.Graph(...............)

# #TASK 2.6: Returning the graphs for displaying Yearly data
#         return [
#                 html.Div(className='.........', children=[html.Div(....,html.Div(....)],style={...}),
#                 html.Div(className='.........', children=[html.Div(....),html.Div(....)],style={...})
#                 ]
        
#     else:
#         return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
