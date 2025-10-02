import requests
import time
import json
import unicodedata
import re
import os
import csv

def normalize_key(key):
    """Supprime accents, espaces et caractères spéciaux, met en minuscules."""
    if not key:
        return None
    key = (
        unicodedata.normalize("NFKD", key)
        .encode("ASCII", "ignore")
        .decode("ASCII")
    )
    key = re.sub(r"[ '\-()]", "_", key)
    key = re.sub(r"_+", "_", key)  # éviter les double _
    key = key.strip("_")
    return key.lower()


PROGRESS_FILE = "progress.txt"

PROGRESS_FILE = "progress.txt"

def get_progress():
    """Lit l’offset depuis progress.txt, retourne 0 si absent"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0

def save_progress(offset):
    """Sauvegarde l’offset dans progress.txt"""
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(offset))


# Champs à récupérer depuis attributes
ATTR_FIELDS = [
    "Marque",
    "Modèle",
    "Année modèle",
    "Kilométrage",
    "Énergie",
    "Boîte de vitesse",
    "Nombre de portes",
    "Nombre de place(s)",
    "Version Constructeur",
    "Date de première mise en circulation",
    "Type de véhicule",
    "Couleur",
    "Crit'Air",
    "Puissance fiscale",
    "Puissance DIN",
    "Permis",
    "Référence",
    "Durée de disponibilité des pièces détachées",
]

# Mapping des champs location en français
LOCATION_MAPPING_FR = {
    "country_id": "pays",
    "region_id": "id_region",
    "region_name": "region",
    "department_id": "id_departement",
    "department_name": "departement",
    "city_label": "ville_affichee",
    "city": "ville",
    "zipcode": "code_postal",
    "lat": "latitude",
    "lng": "longitude",
    "source": "source",
    "provider": "fournisseur",
    "is_shape": "forme_existante",
}


cookies = {
    "__Secure-Install": "36ae2011-5d35-4273-9d08-d42eb458331f",
    "cnfdVisitorId": "6cefd47c-0d9b-4ce7-9bc9-34c913d0b90b",
    "didomi_token": "eyJ1c2VyX2lkIjoiMTk4NmE1ZmYtNjUzNi02OGEyLWJlMDEtNTBlOGQ5OWVhNjA1IiwiY3JlYXRlZCI6IjIwMjUtMDgtMDJUMTA6NDI6MTAuNjQzWiIsInVwZGF0ZWQiOiIyMDI1LTA4LTAyVDEwOjQyOjEyLjg3M1oiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpsYmNmcmFuY2UiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiIsImM6cHVycG9zZWxhLTN3NFpmS0tEIiwiYzptNnB1YmxpY2ktdFhUWUROQWMiLCJjOmFmZmlsaW5ldCIsImM6c3BvbmdlY2VsbC1ueXliQUtIMiIsImM6dGlrdG9rLXJLQVlEZ2JIIiwiYzp6YW5veC1hWVl6NnpXNCIsImM6cGludGVyZXN0IiwiYzpwcmViaWRvcmctSGlqaXJZZGIiLCJjOmlnbml0aW9uby1MVkFNWmRuaiIsImM6ZGlkb21pIiwiYzpsYmNmcmFuY2UtSHkza1lNOUYiXX0sInB1cnBvc2VzIjp7ImVuYWJsZWQiOlsiZXhwZXJpZW5jZXV0aWxpc2F0ZXVyIiwibWVzdXJlYXVkaWVuY2UiLCJwZXJzb25uYWxpc2F0aW9ubWFya2V0aW5nIiwicHJpeCIsImRldmljZV9jaGFyYWN0ZXJpc3RpY3MiLCJjb21wYXJhaXNvLVkzWnkzVUV4IiwiZ2VvbG9jYXRpb25fZGF0YSJdfSwidmVuZG9yc19saSI6eyJlbmFibGVkIjpbImdvb2dsZSIsImM6cHVycG9zZWxhLTN3NFpmS0tEIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkRDS0FnQUZrQTl3Q1N3SWtnUlRBNmNDQmdFVkFKclFVR0FvUkJYT0N3WUZ0NExsZ1lSQUEuRENLQWdBRmtBOXdDU3dJa2dSVEE2Y0NCZ0VWQUpyUVVHQW9SQlhPQ3dZRnQ0TGxnWVJBQSJ9",
    "euconsent-v2": "CQVhVIAQVhVIAAHABBENB1FsAP_gAELgAAAAKENB7CfdQSFiUbJlAOtAYQxP4BAiogAABgABgwwBCBLAMIwEhGAIIADAAAACGBAAICBAAQBlCADAAAAAIAAAACAEAAAAARAAJiAAAEAAAmBICABICYAAAQAQgkiEAAEAgAIAAAogSEgAAAAAHAAAAAAAAAAAAAAAAAEAAAAAAAAAAgAAAAAACAAAAAAEAFAAAAAAAAAAAAAAAAAMAAAAAAAABBQiBeAAsAB4AFQAOAAeABAACQAFQAMoAaABqADwAIYATAAoQBcAF0AMQAfAA_ACEAEdAMoAywBogDnAHcAP2Ag4CEAEWAIxARwBHQDRAGvANoAj0BNoCj4FNAU2ArIBbAC8wGSAMnAZZA1cDWAIAgQvAjsBQgAMUABgACC2gwADAAEFtCAAGAAILaAA.f_wACFwAAAAA",
    "_ga": "GA1.1.1570886354.1754131333",
    "FPID": "FPID2.2.ON2v7dK1aWcr2RhsSQNJeFJAO8dDHLq0N%2BgXlbs1oWM%3D.1754131333",
    "FPAU": "1.2.1929399324.1754131334",
    "deviceId": "e7475994-8fbe-4025-8fb5-384271b1796f",
    "_gcl_au": "1.1.357828164.1754131338",
    "_hjSessionUser_2783207": "eyJpZCI6ImE5MDM1OTM1LTVmMzAtNTNhOS05NDBhLWQ2Njk3OWQ0NTU1MCIsImNyZWF0ZWQiOjE3NTQxMzEzMzQ2NTgsImV4aXN0aW5nIjp0cnVlfQ==",
    "_pcid": "%7B%22browserId%22%3A%22mdvdqyefgoxu2yfe%22%2C%22_t%22%3A%22mtjsohqa%7Cmdvdr0ea%22%7D",
    "_pctx": "%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbfACsIlABYBHAEYAffqwBurGAAYoUkAF8gA",
    "__gsas": "ID=663b8f9af9388491:T=1754207327:RT=1754207327:S=ALNI_MZs4JO4EEVJDS7sEm59bJIadUdcEA",
    "ry_ry-l3b0nco_realytics": "eyJpZCI6InJ5X0VGOTAzQ0U2LTFFQzktNDYzOS04MzNBLUY1NzZFNjVCQTlCRSIsImNpZCI6bnVsbCwiZXhwIjoxNzg1NjY3MzM4NDA1LCJjcyI6MX0%3D",
    "_fbp": "fb.1.1754207399461.156474195924338493",
    "_scid": "6iUW8A2nKR2Dg6U2tXAVKRs60nB4zRuY",
    "lg": "9",
    "FPLC": "l3Az%2FUuNvhDIBLCb4FftzI%2FrvcGf0l3gRbcVOvhbH%2FR%2FLaFdbjzkzhlCnUTFFig%2FY7exKRaMHPgMXZmSTI2lOvQtXNXhDJGhVNCLrOoAquB3G0mB2GxEXfLqNSbW6w%3D%3D",
    "_ScCbts": "%5B%5D",
    "_sctr": "1%7C1759359600000",
    "_scid_r": "-6UW8A2nKR2Dg6U2tXAVKRs60nB4zRuYcGgifw",
    "cto_bundle": "Svc2R19FbUVLbFRBR1hoRjVkc0V1UnlqUUROWWFFalVNbEVyc2tIdkphUlFpQjBZRE1RNVZSSVIlMkJpRUF3QXBjOFdMd084cUlwTDBFJTJCNXM1Z0pJRGNRNG1KN1RQbnUxcjl2WTBtclJoJTJCT3glMkJaJTJGVzUlMkJ3c2FDSXhRdzhJUkVRQUgwWXFsVGxoMnNNcW5OMEpmaEpqcGdiWVRzVDdxa29oa29wRWVic2xzMUEzMFE5bnclM0Q",
    "ry_ry-l3b0nco_so_realytics": "eyJpZCI6InJ5X0VGOTAzQ0U2LTFFQzktNDYzOS04MzNBLUY1NzZFNjVCQTlCRSIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjp0cnVlLCJzYyI6Im9rIiwic3AiOm51bGx9",
    "__gads": "ID=aacc7c3b980ef105:T=1754207334:RT=1759389818:S=ALNI_MbkArq2M_cUnYFwLV1ZEZXIAP9Tfw",
    "__gpi": "UID=00001243a1aa4db2:T=1754207334:RT=1759389818:S=ALNI_MYTmGBVUQA82DutdqJJcnE5S1VGcg",
    "__eoi": "ID=6a69744913b00b24:T=1754207334:RT=1759389818:S=AA-AfjZjG2ffcw1fDjRmsFKHAx6I",
    "datadome": "xAGn2evbgPaalmaWkenmjtDauYEs81yMiE6j3Xd9Y_TQ~pnAKBJl~kilB6OQJYEDAZna9ZlV630XWG2XV8aW9xP1oUCD4HpOOATA0oCpBQ_1A5QFVW9pGFD2NSiYX7Nr",
    "_ga_Z707449XJ2": "GS2.1.s1759389296$o17$g1$t1759389825$j50$l0$h152971888",
}


headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "api_key": "ba0c2dad52b3ec",
    "content-type": "application/json",
    "origin": "https://www.leboncoin.fr",
    "priority": "u=1, i",
    "referer": "https://www.leboncoin.fr/c/voitures",
    "sec-ch-ua": '"Not=A?Brand";v="24", "Chromium";v="140"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "x-lbc-experiment": "eyJ2ZXJzaW9uIjoxLCJyb2xsb3V0X3Zpc2l0b3JfaWQiOiI2Y2VmZDQ3Yy0wZDliLTRjZTctOWJjOS0zNGM5MTNkMGI5MGIifQ==",
}

LIMIT = 100
FILE_NAME = f"./outputs/leboncoin_scraping.csv"

def save_to_csv(filename, rows, fieldnames):
    """Écrit les données dans un CSV unique"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    mode = "a" if os.path.exists(filename) else "w"
    with open(filename, mode, newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if mode == "w":  # écrire l'en-tête seulement si nouveau fichier
            writer.writeheader()
        writer.writerows(rows)

def extract_ad_data(ad: dict) -> dict:
    ad_info = {}

    # Champs directs
    ad_info["url"] = ad.get("url")
    ad_info["first_publication_date"] = ad.get("first_publication_date")
    ad_info["index_date"] = ad.get("index_date")
    ad_info["price"] = ad.get("price", [None])[0] if ad.get("price") else None

    # Attributes
    attr_dict = {normalize_key(f): None for f in ATTR_FIELDS}
    for attr in ad.get("attributes", []):
        key_label = attr.get("key_label")
        value_label = attr.get("value_label")
        norm_key = normalize_key(key_label)
        if norm_key in attr_dict:
            if value_label is not None:
                attr_dict[norm_key] = value_label
            else:
                values_label = attr.get("values_label", [])
                attr_dict[norm_key] = values_label[0] if values_label else None
    ad_info.update(attr_dict)

    # Location
    location = ad.get("location", {})
    loc_dict = {
        normalize_key(new_key): location.get(orig_key, None)
        for orig_key, new_key in LOCATION_MAPPING_FR.items()
        if orig_key != "feature"
    }
    ad_info.update(loc_dict)
    return ad_info

def scrape_one_page(offset: int):
    """Scrape une page et retourne les annonces parsées"""
    json_data = {
        "filters": {
            "category": {"id": "2"},
            "enums": {"ad_type": ["offer"]},
        },
        "limit": LIMIT,
        "offset": offset,
        "sort_by": "relevance",
        "disable_total": True,
        "listing_source": "pagination",
    }

    response = requests.post(
        "https://api.leboncoin.fr/finder/search",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    try:
        data = response.json()
    except Exception:
        print("Réponse non JSON :", response.text[:300])
        return None

    ads = data.get("ads")
    if not ads:
        return None

    print(f"Page offset={offset} → {len(ads)} annonces")
    return [extract_ad_data(ad) for ad in ads]

def scrape_all():
    offset = get_progress()
    print(f"Reprise depuis offset {offset}")
    fieldnames = None

    while True:
        ads_data = scrape_one_page(offset)
        if not ads_data:
            print("Fin du scraping, plus d’annonces.")
            break

        if not fieldnames:
            fieldnames = list(ads_data[0].keys())

        save_to_csv(FILE_NAME, ads_data, fieldnames)
        save_progress(offset + LIMIT) 

        offset += LIMIT

        # Si tu veux le rendre automatique → commente ce bloc

        cont = input("Voulez-vous continuer ? (o/n) : ").strip().lower()
        if cont != "o":
            print("⏹ Arrêt du scraping par l’utilisateur.")
            break

if __name__ == "__main__":
    scrape_all()