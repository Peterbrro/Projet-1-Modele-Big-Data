// Personnages
CREATE (:Person {name:'Eleven'})
CREATE (:Person {name:'Mike'})
CREATE (:Person {name:'Dustin'})
CREATE (:Person {name:'Will'})
CREATE (:Person {name:'Joyce'})
CREATE (:Person {name:'Hopper'})

// Lieux
CREATE (:Location {name:'Hawkins'})
CREATE (:Location {name:'Hawkins Lab'})
CREATE (:Location {name:'Upside Down'})

// Saisons
CREATE (:Season {number:1})
CREATE (:Season {number:2})

// Événements
CREATE (:Event {name:'Disparition de Will'})
CREATE (:Event {name:'Bataille contre le Demogorgon'})

// Relations exemples
MATCH (e:Person {name:'Eleven'}), (s:Season {number:1})
CREATE (e)-[:APPEARS_IN]->(s)

MATCH (p:Person {name:'Will'}), (e:Event {name:'Disparition de Will'})
CREATE (p)-[:INVOLVED_IN]->(e)

MATCH (p:Person {name:'Eleven'}), (p2:Person {name:'Mike'})
CREATE (p)-[:FRIEND_WITH]->(p2)
