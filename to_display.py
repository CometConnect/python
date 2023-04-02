from pandas import read_csv

data = read_csv("csv/gravity.csv")
# Name, Orbital Radius, Gravity, Mass, Distance, Planet Type, Goldilock, Discovery Date, Mass of hoststar
columns_keep = [
  'name', 'planet_radius_in_unit', 'gravity', 'mass', 'distance', 'planet_type', 'goldilock', 'discovery_date', 'mass_of_hoststar.1'
]

columns_to_drop = []
for item in data.columns:
  if item in columns_keep:
    continue
  columns_to_drop.append(item)
data = data.drop(columns=columns_to_drop)
data.to_csv("csv/display.csv")