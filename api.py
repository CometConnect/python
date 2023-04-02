# Things to show
# Name, Orbital Radius, Gravity, Mass, Distance, Planet Type, Goldilock, Discovery Date, Mass of hoststar
from flask import Flask, jsonify
from pandas import read_csv

app = Flask(__name__)

@app.get("/")
def index():
  data = read_csv("csv/display.csv")
  return data.to_json(orient='records')[1:-1].replace('},{', '} {')

@app.route("/get/<int:i>")
def get_data(i):
  data = read_csv("csv/display.csv")
  return data.iloc[i].to_json(orient='records')[1:-1].replace('},{', '} {')


if __name__ == "__main__":
  app.run()