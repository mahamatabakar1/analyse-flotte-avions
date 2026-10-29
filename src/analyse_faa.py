from pathlib import Path

import pandas as pd

ANNEE_COURANTE = 2026
DOSSIER_PROJET = Path(__file__).resolve().parent.parent
DOSSIER_FAA = DOSSIER_PROJET / "data" / "faa"


def lire_fichier_faa(nom_fichier, colonnes):
    tableau = pd.read_csv(
        DOSSIER_FAA / nom_fichier,
        dtype=str,
        encoding="utf-8-sig",
        encoding_errors="replace",
        index_col=False,
    )
    tableau.columns = tableau.columns.str.strip()
    tableau = tableau[colonnes]
    return tableau.apply(lambda colonne: colonne.str.strip())


master = lire_fichier_faa(
    "MASTER.txt",
    ["N-NUMBER", "MFR MDL CODE", "YEAR MFR", "NAME", "STATUS CODE"],
)
reference = lire_fichier_faa(
    "ACFTREF.txt",
    ["CODE", "MFR", "MODEL", "NO-SEATS"],
)

avions = master.merge(
    reference, left_on="MFR MDL CODE", right_on="CODE", how="left"
)

valides = avions[avions["STATUS CODE"] == "V"].copy()
valides["annee"] = pd.to_numeric(valides["YEAR MFR"], errors="coerce")
valides["sieges"] = pd.to_numeric(valides["NO-SEATS"], errors="coerce")

print("Lignes dans MASTER :", len(master))
print("Immatriculations valides (statut V) :", len(valides))

valides = valides[(valides["annee"] >= 1940) & (valides["annee"] <= ANNEE_COURANTE)]
print("Valides avec une année de construction plausible :", len(valides))

avions_de_ligne = valides[valides["sieges"] >= 100]
print()
print("Avions de ligne (100 sièges ou plus) :", len(avions_de_ligne))
print("Âge moyen :", round(ANNEE_COURANTE - avions_de_ligne["annee"].mean(), 1), "ans")

print()
print("Top 10 des modèles :")
print(
    avions_de_ligne.groupby(["MFR", "MODEL"])
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print()
print("Top 10 des propriétaires inscrits :")
print(avions_de_ligne["NAME"].value_counts().head(10))

import matplotlib.pyplot as plt

DOSSIER_SORTIE = DOSSIER_PROJET / "output"

top_proprietaires = avions_de_ligne["NAME"].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_proprietaires.sort_values().plot(kind="barh", color="teal")
plt.title("Top 10 des propriétaires inscrits d'avions de ligne (registre FAA)")
plt.xlabel("Nombre d'avions (100 sièges ou plus)")
plt.ylabel("Propriétaire inscrit")
plt.tight_layout()
plt.savefig(DOSSIER_SORTIE / "top_10_proprietaires_faa.png", dpi=150)
print("Graphique enregistré dans le dossier output")
