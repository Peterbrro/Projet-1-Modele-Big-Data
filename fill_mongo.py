from pymongo import MongoClient
import requests

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['velibDB']        # Nom de ta base
collection = db['stations']   # Nom de ta collection

# Récupération des données depuis l'API
url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&rows=1000"
response = requests.get(url)
data = response.json()

# Insertion dans MongoDB
for record in data['records']:
    lat = record['fields']['coordonnees_geo'][0]
    lon = record['fields']['coordonnees_geo'][1]

    collection.update_one(
        {"station_id": record['fields']['stationcode']},
        {"$set": {
            "name": record['fields']['name'],
            "latitude": lat,
            "longitude": lon,
            "available_bikes": record['fields']['numbikesavailable'],
            "capacity": record['fields']['capacity'],
            "location": {                 # Pour la carte GeoJSON
                "type": "Point",
                "coordinates": [lon, lat]
            }
        }},
        upsert=True
    )

print("✅ Import terminé !")
