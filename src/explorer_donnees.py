from pathlib import Path

import pandas as pd

DOSSIER_PROJET = Path(__file__).resolve().parent.parent
CHEMIN_AEROPORTS = DOSSIER_PROJET / "data" / "airports.dat"

colonnes = [
    "id", "nom", "ville", "pays", "iata", "icao",
    "latitude", "longitude", "altitude_pieds",
    "fuseau_utc", "heure_ete", "fuseau_tz", "type", "source",
]

aeroports = pd.read_csv(
    CHEMIN_AEROPORTS,
    header=None,
    names=colonnes,
    na_values="\\N",
)

print("Nombre total d'aéroports :", len(aeroports))
print()
print("Aperçu des 5 premières lignes :")
print(aeroports[["nom", "ville", "pays", "iata"]].head())
print()

canada = aeroports[aeroports["pays"] == "Canada"]
print("Aéroports au Canada :", len(canada))
print(canada[["nom", "ville", "iata"]].head(10))

print()
print("Top 10 des pays avec le plus d'aéroports :")
top_pays = aeroports["pays"].value_counts().head(10)
print(top_pays)

import matplotlib.pyplot as plt

DOSSIER_SORTIE = DOSSIER_PROJET / "output"

plt.figure(figsize=(10, 6))
top_pays.sort_values().plot(kind="barh", color="steelblue")
plt.title("Top 10 des pays avec le plus d'aéroports")
plt.xlabel("Nombre d'aéroports")
plt.ylabel("Pays")
plt.tight_layout()
plt.savefig(DOSSIER_SORTIE / "top_10_pays.png", dpi=150)
print("Graphique enregistré dans le dossier output")

CHEMIN_COMPAGNIES = DOSSIER_PROJET / "data" / "airlines.dat"

colonnes_compagnies = [
    "id", "nom", "alias", "iata", "icao",
    "indicatif", "pays", "actif",
]

compagnies = pd.read_csv(
    CHEMIN_COMPAGNIES,
    header=None,
    names=colonnes_compagnies,
    na_values="\\N",
)

actives = compagnies[compagnies["actif"] == "Y"]

print()
print("Nombre total de compagnies :", len(compagnies))
print("Compagnies actives :", len(actives))
print()
print("Top 10 des pays avec le plus de compagnies actives :")
print(actives["pays"].value_counts().head(10))

CHEMIN_ROUTES = DOSSIER_PROJET / "data" / "routes.dat"

colonnes_routes = [
    "compagnie_iata", "compagnie_id", "depart_iata", "depart_id",
    "arrivee_iata", "arrivee_id", "partage_codes", "escales", "appareils",
]

routes = pd.read_csv(
    CHEMIN_ROUTES,
    header=None,
    names=colonnes_routes,
    na_values="\\N",
)

print()
print("Nombre total de routes :", len(routes))
print()
print("Top 10 des compagnies avec le plus de routes :")
top_compagnies = routes["compagnie_iata"].value_counts().head(10)
print(top_compagnies)

plt.figure(figsize=(10, 6))
top_compagnies.sort_values().plot(kind="barh", color="darkorange")
plt.title("Top 10 des compagnies avec le plus de routes (codes IATA)")
plt.xlabel("Nombre de routes")
plt.ylabel("Code IATA de la compagnie")
plt.tight_layout()
plt.savefig(DOSSIER_SORTIE / "top_10_compagnies_routes.png", dpi=150)
print("Graphique enregistré dans le dossier output")

CHEMIN_OURAIRPORTS = DOSSIER_PROJET / "data" / "ourairports.csv"

aeroports_recents = pd.read_csv(CHEMIN_OURAIRPORTS, low_memory=False)

print()
print("=== DONNÉES RÉCENTES (OurAirports) ===")
print("Nombre total d'entrées :", len(aeroports_recents))
print()
print("Répartition par type :")
print(aeroports_recents["type"].value_counts())

commerciaux = aeroports_recents[
    (aeroports_recents["scheduled_service"] == "yes")
    & (aeroports_recents["type"] != "closed")
]
print()
print("Aéroports avec service régulier :", len(commerciaux))
print()
print("Top 10 des pays (codes ISO) avec service régulier :")
print(commerciaux["iso_country"].value_counts().head(10))