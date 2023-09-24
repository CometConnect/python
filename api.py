# Things to show
# Name, Orbital Radius, Gravity, Mass, Distance, Planet Type, Goldilock, Discovery Date, Mass of hoststar
from flask import Flask, jsonify, make_response
from pandas import read_csv

app = Flask(__name__)

data = read_csv("csv/display.csv")

@app.get("/")
def index():
  to_send = []
  i = 1
  while True:
    res = get_data(i)
    if res[0] == False:
      break
    to_send.append(res[1])
    i += 1
  return cors(jsonify(to_send))

@app.route("/home")
def get_home():
  to_send = []
  columns = data.columns[1:]
  columns_to_share = ["name", "planet_type"]
  i = 0
  while True:
    try:
      planet_data = {}
      response = data.iloc[i].to_json(orient='records')[1:-1].split(",")[1:]
      for j, item in enumerate(response):
        if columns[j] in columns_to_share:
          planet_data.update({ columns[j]: item.replace("\"", "").replace("\"", "") })
      planet_data.update({ "index": i })
      to_send.append(planet_data)
    except:
      break
    i += 1
  return to_send


@app.route("/get/<int:i>")
def get_data_end_point(i):
  return cors(jsonify(get_data(i)))

def get_data(i):
  try:
    to_send = {}
    columns = data.columns[1:]
    response = data.iloc[i].to_json(orient='records')[1:-1].split(",")[1:]
    for j, item in enumerate(response):
      to_send.update({ columns[j]: item.replace("\"", "").replace("\"", "") })
    return [True, to_send]
  except:
    return [False, {}]


def cors(res):
  res.headers.add("Access-Control-Allow-Origin", "*")
  return res

if __name__ == "__main__":
  app.run()