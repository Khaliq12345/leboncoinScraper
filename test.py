from typing import Optional
import requests

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
    "_ScCbts": "%5B%5D",
    "_sctr": "1%7C1759359600000",
    "FPLC": "8nNU0C5f4hoxYeNiflIFiEon0o%2B%2FcVAkyiCsSAHo8m3a7ueYv%2FW8eCKHzIQW3V9gQ0S%2Fgd0WnkMM0R4vX2WBLSgMiNOxa5MFEGddO1rcYX0LyJQvk1QfEEs8KlpVXw%3D%3D",
    "_scid_r": "_KUW8A2nKR2Dg6U2tXAVKRs60nB4zRuYcGgijw",
    "cto_bundle": "sYCV-19FbUVLbFRBR1hoRjVkc0V1UnlqUURPMXRGTVJsckJKaEZ6YWlheXdGYlJRdUF1VTlmU0FoamNsV3pqaVllUUpyRTVaVUFtN3Vnb0tINWxDQ09XQTRKdjJTMVNmWCUyQktTSnNZWFBPWUtRM1hvTnUlMkZkUjhMSU5rNlI2czJDVmpyZVhIb3B1NDlKbCUyRlV5SWE1WjNGQ0JSMk9MTnFFeTIwZ3N4aEtEVVpzbTlCOWMlM0Q",
    "__gads": "ID=aacc7c3b980ef105:T=1754207334:RT=1759828353:S=ALNI_MbkArq2M_cUnYFwLV1ZEZXIAP9Tfw",
    "__gpi": "UID=00001243a1aa4db2:T=1754207334:RT=1759828353:S=ALNI_MYTmGBVUQA82DutdqJJcnE5S1VGcg",
    "__eoi": "ID=6a69744913b00b24:T=1754207334:RT=1759828353:S=AA-AfjZjG2ffcw1fDjRmsFKHAx6I",
    "_ga_Z707449XJ2": "GS2.1.s1759827887$o22$g1$t1759828458$j54$l0$h301494421",
    "datadome": "4T3~mI37V3vBV4KHYU4U0P3F0uDCqIkfDX5Y_HMhR6UQJsR9l01o0FT_MgL7zvon2jkCjx7FST_1qnbuSGSUxIJ1QSIPvyInB~b395dX4YJ6Kh6b6tDrCDPPKEK73k5k",
}

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "api_key": "ba0c2dad52b3ec",
    "content-type": "application/json",
    "origin": "https://www.leboncoin.fr",
    "priority": "u=1, i",
    "referer": "https://www.leboncoin.fr/recherche?category=2&u_car_brand=PEUGEOT&u_car_model=PEUGEOT_2008&vehicle_type=4x4&fuel=1&gearbox=1&page=2",
    "sec-ch-ua": '"Not=A?Brand";v="24", "Chromium";v="140"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "x-lbc-experiment": "eyJ2ZXJzaW9uIjoxLCJyb2xsb3V0X3Zpc2l0b3JfaWQiOiI2Y2VmZDQ3Yy0wZDliLTRjZTctOWJjOS0zNGM5MTNkMGI5MGIifQ==",
}


def get_filtre(
    brand: str,
    model: Optional[str] = None,
    color: Optional[str] = None,
    vehicle_type: Optional[str] = None,
):
    """
    Sends a request to the Leboncoin API to retrieve the list of filters (models, colors, types)
    available for a given brand, model, or color.
    """
    json_data = {
        "filters": {
            "category": {
                "id": "2",
            },
            "enums": {
                "ad_type": [
                    "offer",
                ],
                "u_car_brand": [brand],
                "u_car_model": [model] if model else [],
                "vehicule_color": [color] if color else [],
                "vehicle_type": [vehicle_type] if vehicle_type else [],
            },
            "ranges": {},
        },
        "limit": 0,
        "limit_alu": 0,
        "sort_by": "relevance",
    }
    response = requests.post(
        "https://api.leboncoin.fr/finder/search",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    response.raise_for_status()
    json_data = response.json()
    aggregations = json_data.get("aggregations")
    models = aggregations.get("u_car_model")
    colors = aggregations.get("vehicule_color")
    types = aggregations.get("vehicle_type")
    return {
        "models": models,
        "colors": colors,
        "types": types,
    }

# 🔹 Function placeholder: retrieves the real data for a given filter combination
# ----------------------------------------------------------
# This function should:
# - Send a request to the Leboncoin API using the provided filter.
# - Retrieve all pages of ads (using pagination if necessary).
# - Extract useful information from each ad (title, price, mileage, year, etc.).
# - Store or process this data (e.g., save it in a CSV or database).
# ----------------------------------------------------------

def get_data(filtre: dict) -> None:
    print("-----------------")
    print(filtre)
    pass


def handle_models(brand: str, models: dict):
    """
    Iterates over models and decides whether to go deeper (color level)
    or to retrieve data directly if the total is small enough.
    """
    for model, total_number in models.items():
        print("--------------MODEL-------------------")
        print(f"Model - {model} | Total - {total_number}")

        if total_number < 3000:
            filtre = build_filtre(brand, model=model)
            get_data(filtre)
        else:
            color_filters = get_filtre(brand, model=model)
            handle_colors(brand, model, color_filters["colors"])


def handle_colors(brand: str, model: str, colors: dict):
    """
    Iterates over colors for a given model.
    """
    for color, total_number in colors.items():
        print("--------------COLOR-------------------")
        print(f"Color - {color} | Total - {total_number}")

        if total_number < 3000:
            filtre = build_filtre(brand, model=model, color=color)
            get_data(filtre)
        else:
            type_filters = get_filtre(brand, model=model, color=color)
            handle_types(brand, model, color, type_filters["types"])


def handle_types(brand: str, model: str, color: str, types: dict):
    """
    Iterates over vehicle types for a given model and color.
    """
    for vehicle_type, total_number in types.items():
        print("--------------TYPE-------------------")
        print(f"Type - {vehicle_type} | Total - {total_number}")

        if total_number < 3000:
            filtre = build_filtre(
                brand, model=model, color=color, vehicle_type=vehicle_type
            )
            get_data(filtre)


def build_filtre(
    brand: str, model: str = None, color: str = None, vehicle_type: str = None
) -> dict:
    """
    Dynamically builds the filter dictionary used to request data from the API.
    """
    enums = {"ad_type": ["offer"], "u_car_brand": [brand]}
    if model:
        enums["u_car_model"] = [model]
    if color:
        enums["vehicule_color"] = [color]
    if vehicle_type:
        enums["vehicle_type"] = [vehicle_type]

    return {
        "filters": {"category": {"id": "2"}, "enums": enums},
        "limit": 100,
        "offset": 0,
        "sort_by": "relevance",
        "disable_total": True,
        "listing_source": "pagination",
    }


def main(brand: str):
    """
    Main entry point — starts the model collection process for a given car brand.
    """
    model_filters = get_filtre(brand)
    models = model_filters["models"]
    handle_models(brand, models)


main("PEUGEOT")
