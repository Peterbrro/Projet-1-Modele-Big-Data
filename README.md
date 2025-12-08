# Projet-1-Modele-Big-Data

# Projet Vélib’ — Analyse et Visualisation en Temps Réel

*(MongoDB, Flask, Docker, Visualisation)*

## Objectifs du projet

Ce projet consiste à construire une architecture Big Data permettant de :

* Collecter automatiquement les données en temps réel de l’API Vélib’.
* Les stocker dans une base MongoDB.
* Exposer une API REST avec Flask.
* Visualiser les stations sur une carte interactive.
* Déployer l’ensemble via Docker.

---

# Fonctionnalités principales

### Collecte des données

* Récupération périodique (ex. toutes les 30 secondes)
* Stockage et mise à jour automatique des données
* Conservation optionnelle d’un historique

### Base NoSQL : MongoDB

* Adaptée aux données JSON
* Indexation possible sur les champs utiles (stationCode, coordonnées, disponibilité)
* Structure flexible et évolutive

### API Flask

Endpoints pour :

* Obtenir la liste complète des stations
* Récupérer les informations d’une station précise
* Filtrer selon la disponibilité (vélos, places, électriques, etc.)

### Visualisation

Carte interactive permettant :

* Affichage de toutes les stations
* Détails en cliquant sur un marker
* Filtrage simple
* Mise en couleur des stations selon la disponibilité

### Docker

* Un conteneur pour le collecteur
* Un conteneur pour l’API
* Un conteneur pour MongoDB
* Un conteneur pour le frontend (optionnel)

---

# Architecture du projet

```
velib-project/
├── data_collector/
│   └── collector.py
├── api/
│   └── app.py
├── frontend/
│   └── index.html
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Cloner le projet

```bash
git clone <lien_de_ton_repo>
cd velib-project
```

## 2. Créer un fichier `.env`

```env
MONGO_URI=mongodb://mongo:27017/
VELIB_API_URL=https://transport.data.gouv.fr/gbfs/velib/station_status.json
REFRESH_INTERVAL=30
```

## 3. Lancer le projet avec Docker

```bash
docker-compose up --build
```

## 4. Accès

API : [http://localhost:5000](http://localhost:5000)
Carte : [http://localhost:8080](http://localhost:8080)

---

# Endpoints API

## Obtenir la liste des stations

```
GET /stations
```

## Filtrer les stations (exemple : au moins 5 vélos)

```
GET /stations?min_bikes=5
```

## Détails d’une station

```
GET /stations/<station_id>
```

---

# Exemple de réponse API

```json
{
  "stationCode": "21015",
  "name": "République - Temple",
  "num_bikes_available": 12,
  "num_docks_available": 8,
  "num_ebikes": 3,
  "status": "IN_SERVICE",
  "coordinates": {
    "lat": 48.867,
    "lon": 2.361
  }
}
```

---

# Visualisation

La carte interactive affiche :

* les stations
* le nombre de vélos disponibles
* le nombre de places libres
* des couleurs selon la disponibilité
* une recherche et un zoom rapide

Technologies possibles : Leaflet.js ou Mapbox.

---

# Technologies utilisées

| Composant   | Description                      |
| ----------- | -------------------------------- |
| MongoDB     | stockage NoSQL des données Vélib |
| Flask       | API REST                         |
| Python      | collecte + backend               |
| Leaflet.js  | affichage cartographique         |
| Docker      | conteneurisation                 |
| Cron Python | boucle de collecte               |

---

# Améliorations possibles

* Ajout d’un modèle de prédiction (occupation future)
* Dashboard Power BI ou Grafana
* Historisation complète de toutes les données
* Système d’alertes (stations saturées)
* Index et optimisation MongoDB

---

# Conclusion

Ce projet constitue une architecture Big Data complète et adaptée à un projet scolaire :

* ingestion temps réel
* base NoSQL
* API REST
* visualisation
* déploiement Docker

Il peut être enrichi selon les besoins et évolue facilement.
