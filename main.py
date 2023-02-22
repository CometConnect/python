from math import sqrt, pi
from string import digits

columns = []
data = {}

with open('fix.csv', 'r') as f:
  for i, row in enumerate(f.readlines()):
    if i == 0:
      columns = row.split(',')
      continue
    cells = row.split(',')
    data.update({ cells[1]: cells })

i1 = columns.index("planet_orbital_period")
i2 = columns.index("orbital_radius") # consider this to be the max
i3 = columns.index("planet_eccentricity")

def i(x, default=0):
  if x == "":
    return default
  return float(x)

def sqr(x):
  return x*x

def justNum(x):
  out = ""
  for c in filter(lambda x: x in digits + '.', x):
    out += c
  return out

def val(v):
  # < .382
  # > 2
  max_radius = i(justNum(v[i2])) * 150_000_000 # AU -> km
  min_radius = sqrt(sqr(max_radius)*(1-sqr(i(v[i3]))))

  distance_travelled = pi * max_radius * min_radius
  time_taken = i(v[i1]) * 365 # years -> days
  if time_taken == 0:
    return max_radius, 0, 0
  
  suitable_distance = 1 if max_radius > .382 * 150_000_000 and max_radius < 2 * 150_000_000 else -1

  return max_radius, distance_travelled/time_taken, suitable_distance

def gif(v, i, multiplier=1):
  return [val[i] * multiplier for val in v]

data_set = {}
for k, v in data.items():
  data_set.update({ k: val(v) })

from plotly.express import scatter

vals = list(data_set.values())
fig = scatter(x=gif(vals, 0), y=gif(vals, 1), color=gif(vals, 2))
fig.show()