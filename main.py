from pandas import read_csv, merge

data = read_csv("data.csv")
small = read_csv("small.csv")
small.sort_values('pl_name')
new = merge(data, small)
new.to_csv("new.csv")
