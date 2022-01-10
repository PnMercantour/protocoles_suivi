# Création et paramétrage d'un module de suivi

## Cadre d'acquisition

### Création

Créer un cadre d'acquisition pour chaque sous-module (ou partager le même CA entre sous-modules dont la finalité est voisine)
_par exemple : Suivi des chiroptères_

### acteurs

Renseigner

### Objectifs du cadre d'acquisition

CA_OBJECTIFS (id_type gn 108)

https://standards-sinp.mnhn.fr/nomenclature/85-objectifs-du-cadre-dacquisition-2019-03-27/

9 : surveillance dans le temps

### Volet SINP

1 : Terre

---

## Jeu de données

Plusieurs jeux de données correspondant aux différents protocoles et méthodologies de recueil.

### Création d'un jeu de données

### id_nomenclature_data_type (DATA_TYP)

Nomenclature des types de données pour un jeu de données
https://standards-sinp.mnhn.fr/nomenclature/94-type-des-donnees-2018-05-14/
Choisir le code "1" (Occurences de taxons)

### id_nomenclature_dataset_objectif (JDD_OBJECTIFS)

https://standards-sinp.mnhn.fr/nomenclature/92-objectifs-du-jeu-de-donnees-2018-05-14/
Pour les chiros, prendre le code 5.2 (surveillance temporelle d'espèces)

### id_nomenclature_collecting_method (METHO_RECUEIL)

https://standards-sinp.mnhn.fr/nomenclature/91-methode-de-recueil-2018-05-14/

- 1 observation directe

- 3 détection d'ultrasons

### id_nomenclature_data_origin (DS_PUBLIQUE)

https://standards-sinp.mnhn.fr/nomenclature/2-code-dorigine-de-la-donnee-2018-05-14/
Pu - donnée publique

### id_nomenclature_source_status (STATUT_SOURCE)

https://standards-sinp.mnhn.fr/nomenclature/19-statut-de-la-source-16-08-2016/

_Te - données Terrain_

### id_nomenclature_resource_type (RESOURCE_TYP)

Pas trouvé dans la nomenclature SINP

_1 - dataset_

### Références

https://github.com/PnX-SI/GeoNature/issues/516

---

## Site

### id_inventor

### id_digitiser

### id_nomenclature_type_site (TYPE_SITE)

Le type de site est défini par geonature.
Il a été étendu (PNM) pour les sites chiro.
Il est envisageable de créer une typologie spécifique ou de filtrer la liste des types proposés.

### CHI_FREQUENTATION

Fréquentation du site (par le public)

### ACC

Accessibilité du site (pour les agents)

### ACC2

Raison de niveau d'accessibilité

### AUTPREAL

Autorisation préalable pour accès

### Nom

### Description

### Type de site

### Descripteur

### Date de description du site

---

## Visite

### site_event

---

## Observation

### OCC_COMPORTEMENT

conforme à l'original sauf couvaison (24) qui a été ajouté à la liste.

https://standards-sinp.mnhn.fr/nomenclature/110-comportement-des-occurrences-observees-2018-05-14/

_valeur par défaut : Non renseigné_

https://github.com/PnX-SI/GeoNature/issues/566

### ETA_BIO

_valeur par défaut : Non renseigné_

### METH_OBS

https://standards-sinp.mnhn.fr/nomenclature/14-methodes-dobservation-observationmethode-2018-05-14/
conforme à l'original sauf CADAVRE qui a été ajouté à la liste (monitoring_chiro)

_valeur par défaut : Vu et entendu_

### STATUT_OBS

https://standards-sinp.mnhn.fr/nomenclature/18-statut-dobservation-statutobservation-16-08-2016/

L'option NSP n'est pas proposée dans notre instance de geonature.
