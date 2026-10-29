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

## Analyse du registre FAA (avions immatriculés aux États-Unis)

Source : registre officiel de la FAA, fichiers `MASTER.txt` et `ACFTREF.txt`, téléchargés le 29 octobre 2026 sur https://registry.faa.gov/database/ReleasableAircraft.zip

Ces fichiers pèsent plus de 200 Mo et ne sont pas dans le dépôt. Pour refaire l'analyse, les décompresser dans `data/faa/`, puis lancer `src/analyse_faa.py`.

Résultats (avions de ligne : 100 sièges ou plus) :

- 318 110 lignes dans MASTER, dont 311 306 immatriculations valides
- 6 351 avions de ligne, d'âge moyen 16,6 ans (calculé sur ceux dont l'année de construction est renseignée)
- Modèles les plus fréquents : Boeing 737-8, Boeing 737-823, Airbus A321-231
- Propriétaires inscrits les plus nombreux : United, Delta, Southwest. Trois banques fiduciaires figurent aussi dans le top 10 (Bank of Utah, UMB Bank, Wilmington Trust)

Limites :

- Le registre ne couvre que les avions immatriculés aux États-Unis
- Le propriétaire inscrit est souvent une fiducie : le registre ne dit pas qui est le bailleur ni la compagnie exploitante
- Les noms de fabricants et de modèles ont des variantes d'écriture (par exemple AIRBUS, AIRBUS S A S, AIRBUS CANADA LP) qu'il faudra regrouper

Graphique : `output/top_10_proprietaires_faa.png`