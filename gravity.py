from pandas import read_csv

df = read_csv('csv/goldilock.csv')

def isfloat(x):
  if x.isdigit():
    return True
  if x == ".":
    return True
  return False

gravity_data = []
for cell in df.iloc:
  try:
    mass = 0
    raw_mass = float("".join(filter(isfloat, cell['mass'])))
    if "Jupiters" in cell['mass']:
      mass = raw_mass * 317.82
    else:
      mass = raw_mass

    radius = cell['planet_radius_in_unit']

    gravity_data.append(
      mass / (radius * radius)
    )
  except:
    gravity_data.append(-1)

df.drop(columns=['Unnamed: 0'], inplace=True)
df['gravity'] = gravity_data
df.to_csv("csv/gravity.csv")