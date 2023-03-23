from pandas import read_csv

df = read_csv('old_csv/mass_fix.csv')

G = 6.674 * pow(10, -11)

def sqr(x): return x * x

def isfloat(x):
  if x.isdigit():
    return True
  if x == ".":
    return True
  return False

gravity = []
for cell in df.iloc:
  c = cell.notnull()
  if not c['mass'] or not c['planet_radius_in_unit']:
    gravity.append(0) # can't be calculated
    continue

  raw_mass = "".join(filter(isfloat, cell['mass']))
  if raw_mass == "": # Unknown
    gravity.append(0)
    continue

  mass = float(raw_mass) * 2 * pow(10, 30)
  radius = cell['planet_radius_in_unit'] * 7 * pow(10, 8)

  gravity.append(G*mass/sqr(radius))

df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'], inplace=True)
df['gravity'] = gravity
df.to_csv("old_csv/with_gravity.csv")