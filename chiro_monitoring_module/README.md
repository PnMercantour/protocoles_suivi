Changer:

```
{
    "__CODE_LIST_INVENTOR": "obsocctax",
    "__CODE_LIST_OBSERVER": "obsocctax",
    "__ID_COMPONENT_TAXONOMY": "100",
    "__ID_DATASET_VISIT": 1
}
```

**CODE_LIST_INVENTOR => liste usershub des qui découvrent des sites
**CODE_LIST_OBSERVER => liste usershub des qui font les observations
**ID_COMPONENT_TAXONOMY => id liste taxhub (100 est toujours existant, chiro est 23 en prod)
**ID_DATASET_VISIT => créer un dataset dans le menu metadata de geonature et utiliser l'id

https://depot-legal-biodiversite.naturefrance.fr/ressources/DEPOBIO_Standard_Fichier_V2_20210104_2.pdf
https://depot-legal-biodiversite.naturefrance.fr/ressources/DEPOBIO_Annexes_V2_20210104.pdf

_Schema du module de monitoring chiro_

**site**

**_id_nomenclature_type_site_**

geonature a défini la nomenclature TYPE_SITE (id_type = 116).
nomenclature.json définit plusieurs types de sites supplémentaires.
Les id 446 à 453 (source GEONATURE 2019) ne sont pas utilisés. Faut-il les supprimer ou sont-ils utilisés par ailleurs (occtax, synthèse)?

**_base_site_description_**

Si on se permet de toucher à la configuration du module :
t_base_sites.base_site_description (attribut commun à tous les modules de monitoring) pourrait recevoir les données de t_site_complements.data --> commentaire (spécifique au module chiro) car ce ne sont que des précisions géographiques.
On peut tout de même garder commentaire pour les saisies liées au protocole.

**_trg_chiro_duplicate_site_geom_**

Un trigger (obsolète?) qui met à jour le schema monitoring_chiro (obsolète?)
Supprimer le trigger avant de supprimer le schema monitoring_chiro.

**_data_**

`id_site_old` est-il utile?

**visites**

L'attribut comments n'est pas proposé dans l'ihm visite.

**_id_nomenclature_tech_collect_campanule_**

(TECHNIQUE_OBS)
http://campanule.mnhn.fr
un code campanule est associé à chaque visite
Actuellement valeur par défaut = code 133 (non renseigné).
Geonature ne l'utilise que dans occtax et ne le reporte pas dans la synthèse.
https://github.com/PnX-SI/GeoNature/issues/1208

Mettre à jour la table visite avec la technique de collecte campanue appropriée lorsqu'elle est connue.

**_id_nomenclature_grp_type_**

type de regroupement : saisi avec valeur NULL dans la visite. Laisser vide en créant l'enregistrement visite pour récupérer la valeur par défaut 'PASS'
ref_nomenclatures.get_id_nomenclature('TYP_GRP'::character varying, 'PASS'::character varying)

**_data_**

`data_source` donne la source des données importées. Cette information n'est pas visible dans l'IHM.

`id_obs_old` et `id_from_import` sont-ils utiles?
`ìd_from_import` n'est pas défini dans visit.json.

`id_nomenclature_chiro_obs` n'apparaît pas dans display_list de visit.json (implicite?)

**observation**

**_cd_nom_**

Signification des cd_nom = 999999999 ?

**_comments_**

Aucun commentaire dans les observations, car les données initiales une visite a été créée pour chaque obs et les commentaires rattachés à la visite.

**_data_**

`id_nomenclature_chiro_status` : Faire le ménage dans la nomenclature, certains mnemoniques ne sont pas explicites.

**synthèse**

**_id_nomenclature_geo_object_nature_**
Nature objet géographique : stationnel ('St')
ref_nomenclatures.get_id_nomenclature('NAT_OBJ_GEO', 'St') AS id_nomenclature_geo_object_nature,

**_id_nomenclature_grp_type_**
ok (après correction de la table visite)

**_id_nomenclature_obs_technique_**

http://standards-sinp.mnhn.fr/nomenclature/14-methodes-dobservation-observationmethode-2018-05-14/

- code 20 (autre) si cadavre
- code 0 si observation directe d'un individu vivant
- code 1 si observation acoustique
- code 3 si Observation acoustique indirecte d'un individu vivant avec matériel spécifique permettant de transduire des ultrasons en sons perceptibles par un humain.
- code 6 si Observation indirecte par les excréments.
  etc

**_id_nomenclature_bio_status_**

http://standards-sinp.mnhn.fr/nomenclature/13-statut-biologique-occurrencestatutbiologique-2018-05-14/

code 3 (reproduction) si code en entrée = RC ou RP.

type information géographique : géoréférencement ('1')

http://standards-sinp.mnhn.fr/nomenclature/23-type-dinformation-geographique-16-08-2016/
