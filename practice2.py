
import pandas as pd
import plotly.express as px

# Sample data preparation
data = {
    'Center': ['ARC', 'ARC', 'GRC', 'GRC', 'LaRC', 'LaRC', 'LaRC', 'LaRC', 'LaRC', 'LaRC', 'LaRC', 'MSFC'],
    'Facility': ['BRC', 'FML', 'AAPL', 'ERB', 'BART', 'FPL', 'HSLD', 'LSWAT', 'PCT', 'SCRAMJET', 'TCT', 'TWT'],
    'CORL': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    'Cost of Operations': [1700000, 300000, 8070627, 22600000, 19556, 0, 1260000, 121218, 0, 2203236, 1293051, 0],
    'Cost of Maintenance': [200000, 120000, 200000, 3821000, 91817, 0, 0, 121281, 0, 157385, 60000, 0],
    'Deferred Maintenance': [0, 0, 2440000, 1755000, 0, 0, 300000, 0, 0, 3000000, 7720000, 0],
}

df = pd.DataFrame(data)

# Adding a new column for total cost
df['Total Cost'] = df['Cost of Operations'] + df['Cost of Maintenance'] + df['Deferred Maintenance']

# Creating the bubble chart
fig_bubble = px.scatter(df, 
                        x='Facility', 
                        y='CORL', 
                        size='Total Cost', 
                        color='Center',
                        hover_name='Facility', 
                        size_max=60, 
                        title='Bubble Chart of Total Costs by Facility and CORL',
                        labels={'CORL': 'CORL Value', 'Total Cost': 'Total Cost ($)'})

fig_bubble.update_yaxes(range=[1,7])

# Show the bubble chart
fig_bubble.show()
