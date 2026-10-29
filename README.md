# Analyse de la flotte et des aéroports

Projet Python d'exploration de données d'aviation : aéroports, compagnies aériennes et routes. Premier projet d'un portfolio orienté aviation et leasing d'avions.

## Sources de données

- **OpenFlights** (données de 2017, routes plus anciennes) : `airports.dat`, `airlines.dat`, `routes.dat`
- **OurAirports** (mise à jour quotidienne, fichier téléchargé en juillet 2026) : `ourairports.csv`

Les données OpenFlights sont anciennes. Elles servent à construire la méthode, et OurAirports apporte une vue récente.

## Résultats principaux

- 6162 compagnies dans OpenFlights, dont 1255 actives
- 67 663 routes dans OpenFlights
- 4330 aéroports avec service régulier dans OurAirports
- Le Canada est 2e pays pour les aéroports avec service régulier (297), derrière les États-Unis (699)

Graphiques dans le dossier `output` :
- `top_10_pays.png`
- `top_10_compagnies_routes.png`

## Structure du projet

- `data/` : fichiers de données
- `src/explorer_donnees.py` : script d'analyse
- `output/` : graphiques générés
- `notebooks/` : réservé aux explorations futures

## Lancer le projet

1. Créer un environnement virtuel Python
2. Installer les bibliothèques avec `pip install -r requirements.txt`
3. Lancer `src/explorer_donnees.py`

## Prochaines étapes

- Analyse de la flotte avec une base d'avions récente (âge, modèles, propriétaires)
- Estimation de la valeur et de l'amortissement d'un avion
- Application web de suivi de flotte