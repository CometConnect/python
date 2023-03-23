from pandas import read_csv

df = read_csv('old_csv/mass_fix.csv')

suitable_type = []
for cell in df.iloc:
  if cell['planet_type'] == 'Super Earth':
    suitable_type.append(True)
    continue
  suitable_type.append(False)

df.drop(columns=['Unnamed: 0'], inplace=True)
df['suitable_type'] = suitable_type
df.to_csv("data.csv")