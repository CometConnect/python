from pandas import read_csv
from math import sqrt, pi

df = read_csv('old_csv/mass_fix.csv')

def isfloat(x):
  if x.isdigit():
    return True
  if x == ".":
    return True
  return False

def sqr(x): return x * x

suitable_speed = []
for cell in df.iloc:
  c = cell.notnull()
  if not c['orbital_radius'] or not c['planet_eccentricity'] or not c['planet_orbital_period']:
    suitable_speed.append(False)
    continue

  raw_o_radius = "".join(filter(isfloat, cell['orbital_radius']))
  if raw_o_radius == "": # Unknown:
    suitable_speed.append(False)
    continue
  
  o_radius = float(raw_o_radius)

  e = float(cell['planet_eccentricity'])

  time = float(cell['planet_orbital_period']) * 365 # years -> days
  if time == 0:
    suitable_speed.append(False)
    continue

  min_radius = sqrt(sqr(o_radius)*(1-sqr(e)))
  distance = pi * o_radius * min_radius
  speed = distance * 150_000_000/time
  suitable_speed.append(
    True
    if speed < 200
    else False
  )

df.drop(columns=['Unnamed: 0'], inplace=True)
df['suitable_speed'] = suitable_speed
df.to_csv("data.csv")