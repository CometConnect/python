import plotly.express as px
from pandas import read_csv, DataFrame, concat

csv = read_csv("data.csv")
data = DataFrame()

targets = list(map(lambda x: "TRAPPIST-1 " + x, ["f", "e", "d", "c", "b"]))

i = 0

def isfloat(x):
  if x.isdigit():
    return True
  if x == ".":
    return True
  return False

for cell in csv.iloc:
  if cell['name'] not in targets:
    continue

  data = concat([data, DataFrame(
    data={ 'index': i, 'name': cell['name'], 'mass': float("".join(filter(isfloat, cell['mass']))) },
    index=['name']
  )], axis='index')
  i += 1

print(data)
fig = px.bar(data, y='mass', x='name')
fig.show()