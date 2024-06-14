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

# Transforming the data for heatmap
heatmap_data = df[['Facility', 'Cost of Operations', 'Cost of Maintenance', 'Deferred Maintenance']]
heatmap_data = heatmap_data.melt(id_vars=['Facility'], var_name='Cost Type', value_name='Cost')

# Creating the heatmap
fig_heatmap = px.density_heatmap(
    heatmap_data, 
    x='Facility', 
    y='Cost Type', 
    z='Cost', 
    title='Heatmap of Costs by Facility',
    color_continuous_scale='Viridis'
)

# Show the heatmap
fig_heatmap.show()
