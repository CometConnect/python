from pandas import read_csv

df1 = read_csv('filtered.csv')
df2 = read_csv('mass_fix.csv')

fixed_mass  =df2['mass']
df1['mass'] = fixed_mass

df1.to_csv("fix.csv")