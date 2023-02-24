from pandas import read_csv

df = read_csv('data.csv')

def isfloat(x):
  if x.isdigit():
    return True
  if x == ".":
    return True
  return False

goldilock = []
for cell in df.iloc:
  if not cell.notnull()['orbital_radius']:
    goldilock.append(False)
    continue
  raw_o_radius = "".join(filter(isfloat, cell['orbital_radius']))
  if raw_o_radius == "": # Unknown:
    goldilock.append(False)
    continue
  
  o_radius = float(raw_o_radius)
  print("T" if o_radius > .382 and o_radius < 2 else "F", end=' ')
  goldilock.append(
    True
    if o_radius > .382 and o_radius < 2 
    else False
  )

df.drop(columns=['Unnamed: 0'], inplace=True)
df['goldilock'] = goldilock
df.to_csv("data.csv")