from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
db = client["velib_db"]
stations_collection = db["stations"]

@app.route("/stations", methods=["GET"])
def get_stations():
    min_bikes = int(request.args.get("min_bikes", 0))
    query = {"num_bikes_available": {"$gte": min_bikes}}
    stations = list(stations_collection.find(query, {"_id": 0}))
    return jsonify(stations)

@app.route("/stations/<station_id>", methods=["GET"])
def get_station(station_id):
    station = stations_collection.find_one({"stationCode": station_id}, {"_id": 0})
    if station:
        return jsonify(station)
    return jsonify({"error": "Station not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
