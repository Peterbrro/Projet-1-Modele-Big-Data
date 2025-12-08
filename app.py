from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['velibDB']
collection = db['stations']

@app.route('/')
def index():
    stations_cursor = collection.find()
    stations = []
    for st in stations_cursor:
        stations.append({
            "id": str(st.get("_id")),   # Convert ObjectId en string
            "name": st.get("name"),
            "latitude": st.get("latitude"),
            "longitude": st.get("longitude"),
            "available_bikes": st.get("available_bikes"),
            "capacity": st.get("capacity")
        })
    return render_template('index.html', stations=stations)

if __name__ == '__main__':
    app.run(debug=True)
