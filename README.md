
# Projet Vélib’ — Analyse et Visualisation en Temps Réel

*(MongoDB + Flask + Visualisation)*

---

## Objectifs du projet

Ce projet a pour but de :  

- Collecter les données en temps réel des stations Vélib’ via MongoDB.  
- Les stocker dans une base locale MongoDB.  
- Visualiser les stations et leurs disponibilités sur un dashboard interactif.  
- Fournir des statistiques et graphiques utiles pour comprendre la disponibilité des vélos à Paris.  

---

## Fonctionnalités principales

### Base NoSQL : MongoDB

- Stockage des données JSON des stations.  
- Structure flexible : `name`, `latitude`, `longitude`, `available_bikes`, `capacity`.  
- Possibilité d’indexer les champs les plus utilisés pour améliorer les requêtes.  

### API Flask

Endpoints principaux :  

- `/` : dashboard web affichant la carte et les graphiques.  
- Possibilité d’ajouter d’autres endpoints pour filtrer ou récupérer des stations spécifiques.  

### Dashboard Interactif

Le frontend (HTML + JS + Leaflet + Chart.js) offre :  

- **Carte interactive** affichant toutes les stations.  
- **Markers colorés** selon la disponibilité :  
  - Vert : assez de vélos  
  - Orange : peu de vélos  
  - Rouge : station vide  
- **Statistiques globales** en haut de page :  
  - Nombre total de stations  
  - Nombre total de vélos disponibles  
  - Nombre de stations vides  
- **Filtre interactif** : toutes les stations / stations vides / stations avec peu de vélos.  
- **Graphique Chart.js** pour visualiser les top stations par vélos disponibles.  
- **Heatmap** pour visualiser les zones avec forte concentration de vélos.  

---

## Architecture du projet

```

Projet-1-Modele-Big-Data/
├── app.py           # Application Flask
├── templates/
│   └── index.html   # Dashboard
├── requirements.txt # Librairies Python
└── README.md

````

---

## Installation et utilisation

### 1. Cloner le projet

```bash
git clone https://github.com/Peterbrro/Projet-1-Modele-Big-Data.git
cd Projet-1-Modele-Big-Data
````

### 2. Installer les dépendances

Si vous n’avez pas encore les packages Python :

```bash
pip install -r requirements.txt
```

Assurez-vous que `requirements.txt` contient au minimum :

```
Flask
pymongo
```

### 3. Configurer MongoDB

* Installer MongoDB localement.
* Créer une base `velibDB` et une collection `stations`.
* Insérer vos données (soit via script Python, soit import JSON).

### 4. Lancer l’application

```bash
python app.py
```

* Le dashboard est accessible à : [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Notes sur le dashboard

* Les **stats globales** et les **markers colorés** permettent une lecture rapide de la disponibilité des vélos.
* Le **filtre interactif** facilite la visualisation des stations critiques.
* Le **graphique Chart.js** met en avant les stations les plus fournies ou les plus vides.
* La **heatmap** aide à repérer les zones où les vélos sont concentrés ou rares.

---

```
