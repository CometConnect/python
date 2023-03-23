from pandas import read_csv
from plotly.express import scatter

csv = read_csv("old_csv/with_gravity.csv")

fig = scatter(x=csv['planet_radius_in_unit'], y=csv['mass'], size=csv['gravity'])
fig.show()