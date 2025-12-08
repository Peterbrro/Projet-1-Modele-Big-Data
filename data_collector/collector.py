import requests
import os
import time
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
VELIB_API_URL = os.getenv(
    "VELIB_API_URL",
    "https://transport.data.gouv.fr/gbfs/velib/station_status.json"
)
REFRESH_INTERVAL = int(os.getenv("REFRESH_INTERVAL", 30))

client = MongoClient(MONGO_URI)
db = client["velib_db"]
stations_collection = db["stations"]

def fetch_data():
    try:
        response = requests.get(VELIB_API_URL)
        data = response.json()["data"]["stations"]
        for station in data:
            stations_collection.update_one(
                {"stationCode": station["station_id"]},
                {"$set": {
                    "stationCode": station["station_id"],
                    "name": station.get("name"),
                    "num_bikes_available": station.get("num_bikes_available"),
                    "num_docks_available": station.get("num_docks_available"),
                    "num_ebikes": station.get("num_ebikes"),
                    "status": station.get("status"),
                    "coordinates": {
                        "lat": station.get("lat"),
                        "lon": station.get("lon")
                    }
                }},
                upsert=True
            )
        print(f"[INFO] {len(data)} stations updated.")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    while True:
        fetch_data()
        time.sleep(REFRESH_INTERVAL)
