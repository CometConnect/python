columns = []
data = {}

with open('mass_fix.csv', 'r') as f:
  for i, row in enumerate(f.readlines()):
    if i == 0:
      columns = row.split(',')
      continue
    cells = row.split(',')
    data.update({ cells[1]: cells })

i1 = columns.index("planet_radius_in_unit")
i2 = columns.index("mass_in_kg")

def i(x, default=0):
  if x == "":
    return default
  return float(x)

def val(v):
  return i(v[i1]), i(v[i2])

def gif(v, i, multiplier=1):
  return [val[i] * multiplier for val in v]

data_set = {}
for k, v in data.items():
  data_set.update({ k: val(v) })
from plotly.express import scatter

vals = list(data_set.values())
fig = scatter(x=gif(vals, 0), y=gif(vals, 1))
fig.show()