# Modèle de données pour les observations de chiroptères

Le modèle de données est structuré sous la forme site/visite/observation proposée par le module de monitoring de geonature.

Chaque type d'objet (site, visite, ou observation) reçoit des attributs qui permettent de le caractériser de façon générique (par exemple l'inventeur d'un site ou la date d'une visite) ou spécifique au module de monitoring chiro.

Bien que les attributs puissent être librement définis, de même que les valeurs admissibles pour chaque attribut, on s'efforce d'utiliser les nomenclatures standard de l'INPN et de n'introduire de nouveaux attributs que lorsque le standard n'est pas exploitable.

https://standards-sinp.mnhn.fr/nomenclature/

A noter que la définition de chaque valeur d'attribut s'affiche automatiquement à l'écran lorsqu'on la survole avec la souris, permettant à l'utilisateur de faire un choix éclairé entre les alternatives proposées.

On s'autorisera à:

- n'utiliser qu'un sous ensemble des valeurs définies dans une nomenclature standard (ce sera souvent le cas ici)

- définir des nomenclatures personnalisées pour les chiroptères, lorsqu'aucun standard ne convient.

On s'interdira par contre d'étendre une nomenclature standard pour les besoins du module chiro. Lorsqu'on serait tenté de le faire, on préfèrera sélectionner l'attribut standard le plus proche (éventuellement une valeur indéfinie) et compléter avec un attribut personnalisé, permettant aux outils communs (exemple : import dans la synthèse geonature) d'interpréter les attributs standard tout en préservant les données plus détaillées interprétables par le seul module chiro.

---

## Site

### Nom du site

Nom attribué au site (pas forcément unique).

### Coordonnées géographiques

Coordonnées de type point.

### Altitude du site

### Description

Description du site (texte libre)

### Descripteur

L'inventeur du site.

### Date description

La date de description du site

### Code du site

Pas utilisé

### Type du site / type de site chiro

Geonature a défini la nomenclature TYPE_SITE avec les valeurs suivantes:

- Arbre
- Rocher
- Site chiroptère
- Grotte
- Mine
- Bâti
- Hors gîte
- Indéterminé

Cette nomenclature a été étendue (PNM - 2020) avec les valeurs suivantes:

- Autre bati
- Batiments religieux
- Batiments habitations
- Batiments ruraux
- Carriere
- Pont
- Tunnel
- Cavite naturelle
- Cavite artificielle
- Non-défini
- Autre site (non-gîte)
- Blockhaus

La question mérite un éclaircissement. En effet, le type de site est un attribut imposé par l'application monitoring (et forcément pris dans la nomenclature TYPE_SITE). D'autre part, le site peut en théorie être utilisé par plusieurs modules de monitoring (même si l'interface utilisateur de l'application ne permet pas d'inclure un site existant dans un nouveau module, en base de données c'est possible).

Proposition :

- forcer l'attribut type de site à la valeur `Indéterminé`, masquer cette valeur dans l'interface utilisateur,
- ajouter un attribut `type_site_chiro` propre au module de monitoring chiro et dont les valeurs possibles sont à définir en s'inspirant des deux listes ci-dessus et en évitant les doublons.

### Accessibilité du site

Accessibilité du site (pour les agents)
https://standards-sinp.mnhn.fr/nomenclature/27-niveau-daccessibilite-18-08-2016/

### ACC2

Raison de niveau d'accessibilité
https://standards-sinp.mnhn.fr/nomenclature/26-raison-de-niveau-daccessibilite-17-08-2016/

### AUTPREAL

Autorisation préalable pour accès
https://standards-sinp.mnhn.fr/nomenclature/28-autorisation-prealable-pour-acces-18-08-2016/

### Fréquentation

Fréquentation du site par le public.

Attribut personnalisé qui prend les valeurs suivantes:

- Importante : accès facile, proximité GR, bâti remarquable souvent visité
- Moyenne : accessibilité à pied, proximité PR
- Faible : site peu accessible, peu connu
- Nulle : pas de pénétrations enthropiques

---

## Visite

Chaque visite est associée à un jeu de données, qui décrit la méthodologie de recueil.
On propose d'utiliser a minima deux jeux de données, l'un pour les observations directes, l'autre pour les observations indirectes par analyse acoustique. D'autres jeux de données pourront être créés si besoin. Voir la section consacrée aux [jeux de données](#Jeux-de-données).

Les observateurs, de même que la date d'observation, sont des attributs de la visite.

Un commentaire peut être associé à la visite.

### Modification du site

Cet attribut personnalisé consigne les modifications du site depuis la visite précédente. C'est en quelque sorte l'historique du site. Les valeurs proposées pour cet attribut sont:

- Aménagement chiroptière
- Aménagement nichoir
- Mise en protection
- Autre aménagement favorable
- Modification du milieu
- Dégradation (Réfection du site)
- Traitement chimique proche
- Dérangement direct
- Destruction

---

## Observation

### Espèce

Le sous-arbre taxonomique des Chiroptera. Permet de saisir une espèce, un genre, ou simplement l'ordre Chiroptera (à utiliser par exemple lorsqu'aucun individu n'a été observé).

### Commentaire

Commentaire relatif à l'observation.

### Statut d'observation

https://standards-sinp.mnhn.fr/nomenclature/18-statut-dobservation-statutobservation-16-08-2016/

Présent ou non observé. Indiquer non observé lorsque la visite est infructueuse.

### Méthode d'observation

Sous ensemble (à définir) du standard
https://standards-sinp.mnhn.fr/nomenclature/14-methodes-dobservation-observationmethode-2018-05-14/

### Statut biologique

Sous ensemble (à définir) du standard
https://standards-sinp.mnhn.fr/nomenclature/13-statut-biologique-occurrencestatutbiologique-2018-05-14/
Certaines valeurs ont été gelées et déplacées dans la nomenclature décrivant le comportement.

### Comportement des occurrences observées

Sous ensemble (à définir) du standard
https://standards-sinp.mnhn.fr/nomenclature/110-comportement-des-occurrences-observees-2018-05-14/

### Stade de vie: stade de développement du sujet

Sous ensemble (à définir) du standard
https://standards-sinp.mnhn.fr/nomenclature/10-stade-de-vie-stade-de-developpement-du-sujet-occurrencestadedevie-2018-05-14/

### Sexe

Sous ensemble (à définir) du standard
https://standards-sinp.mnhn.fr/nomenclature/9-sexe-occurrencesexe-23-06-2016/

### Nombre d'individus observés

En lien avec le nombre d'individus (un entier), le SINP a défini l'attribut `type de dénombrement` https://standards-sinp.mnhn.fr/nomenclature/21-type-de-denombrement-16-08-2016/ qu'il est possible d'ajouter si besoin.

---

## Jeux de données

Plusieurs jeux de données doiivent être définis correspondant aux différents protocoles et méthodologies de recueil.

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

_Pu - donnée publique_

### id_nomenclature_source_status (STATUT_SOURCE)

https://standards-sinp.mnhn.fr/nomenclature/19-statut-de-la-source-16-08-2016/

_Te - données Terrain_

### id_nomenclature_resource_type (RESOURCE_TYP)

Pas trouvé dans la nomenclature SINP

_1 - dataset_

---

## Cadre d'acquisition

### Création

Créer un ou plusieurs cadres d'acquisition
_par exemple : Suivi des chiroptères_

### acteurs

Renseigner

### Objectifs du cadre d'acquisition

https://standards-sinp.mnhn.fr/nomenclature/85-objectifs-du-cadre-dacquisition-2019-03-27/

_9 : surveillance dans le temps_

### Volet SINP

_1 : Terre_
