from pandas import read_csv, DataFrame, concat

csv = read_csv("old_csv/mass_fix.csv")
max_planets = max(csv['num_of_planets_in_system'])

systems = DataFrame()

for system in csv.iloc:
  if system['num_of_planets_in_system'] == max_planets:
    systems = concat([systems, system])

print(systems)