import string
import unicodedata
import json

trans_table = str.maketrans(string.punctuation, len(string.punctuation) * " ")


def remove_accents(text):
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def normalize(text):
    return remove_accents(text).translate(trans_table)


def make_mnemonique(text):
    return "_".join(text.strip().split()).upper()


data = []

sites = """6	Blockhaus
10	Pont
11	Tunnel
2	Autre bati
4	Batiments religieux
3	Batiments habitations
5	Batiments ruraux
7	Carriere
9	Cavite naturelle
8	Cavite artificielle
999	Non-défini
99	Autre site (non-gîte)"""


for line in sites.split("\n"):
    id_, name = line.split(maxsplit=1)
    mnemonique = make_mnemonique(normalize(name))
    data.append(
        {
            "type": "TYPE_SITE",
            "cd_nomenclature": str(id_),
            "mnemonique": mnemonique,
            "label_default": name,
            "definition_default": name,
        }
    )


type_obs = """2	Cadavre / Animal blessé
3	Capteur
4	Filet
5	Gite
6	Spontané / occasionnelle"""


for line in type_obs.split("\n"):

    id_, name = line.split(maxsplit=1)
    mnemonique = make_mnemonique(normalize(name))

    data.append(
        {
            "type": "TYPE_OBS_CHIRO",
            "cd_nomenclature": str(id_),
            "mnemonique": mnemonique,
            "label_default": name,
            "definition_default": name,
        }
    )


status = """1	Actifs
2	Allaitante
3	Estivant
4	G1
5	G1E0
6	Hivernant
7	Lethargie
8	multipare
9	primipare?
10	Repro
11	Reproducteur"""


for line in status.split("\n"):

    id_, name = line.split(maxsplit=1)
    mnemonique = make_mnemonique(normalize(name))

    data.append(
        {
            "type": "CHIRO_STATUS",
            "cd_nomenclature": str(id_),
            "mnemonique": mnemonique,
            "label_default": name,
            "definition_default": name,
        }
    )

print(json.dumps(data, ensure_ascii=False))
