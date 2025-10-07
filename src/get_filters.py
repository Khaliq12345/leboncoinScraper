from typing import Optional
import requests
import logging

logging.basicConfig(level=logging.INFO)

COOKIES = {
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
            "cto_bundle": "M67pI19FbUVLbFRBR1hoRjVkc0V1UnlqUURIZGRGVWZlM0ZBUFY2WEwlMkJnVGJBJTJCQ3hBM204ZEMzZGp5YWR1UVBuV2wxRnZDJTJGaXlCSmVZWiUyRm0lMkZTSTk2ZnZZT0hsS21Sa1pwQnpQdHVLczhzZWMxQjlCa0JYaDM4dE5DMzklMkZPUjZlWTh6eCUyRlpJJTJCcVhzTUpBNk9FYXo0emNzU3olMkZtMHRjOVNZd21FM0w3S0Z3UUVzOUklM0Q",
            "_scid_r": "_qUW8A2nKR2Dg6U2tXAVKRs60nB4zRuYcGgigQ",
            "_ga_Z707449XJ2": "GS2.1.s1759846567$o26$g0$t1759846567$j60$l0$h672542517",
            "__gads": "ID=aacc7c3b980ef105:T=1754207334:RT=1759846578:S=ALNI_MbkArq2M_cUnYFwLV1ZEZXIAP9Tfw",
            "__gpi": "UID=00001243a1aa4db2:T=1754207334:RT=1759846578:S=ALNI_MYTmGBVUQA82DutdqJJcnE5S1VGcg",
            "__eoi": "ID=6a69744913b00b24:T=1754207334:RT=1759846578:S=AA-AfjZjG2ffcw1fDjRmsFKHAx6I",
            "datadome": "oByi0lZUHjjWwAhw~trg93VaLF8VHfDi1kjHn6Th2DZeOH3iOR2lUl0V5RquvjNxLqPRXIxQbTS~GV2AAhM3fCeeUBqmTc4hB_oIcsbuGU70YfVXQFfsGozhGyra7~wg",
        }

HEADERS = {
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


class GetFilters:
    def __init__(self):
        """
        Initialize the scraper with two lists:
        - self.filters : filters with < 3000 ads
        - self.over_3000_filters : filters with > 3000 ads
        """
        self.filters: list[dict] = []
        self.over_3000_filters: list[dict] = []

    # =====================================================
    # Retrieve available filters from Leboncoin API
    # =====================================================
    def get_filtre(
        self,
        brand: str,
        model: Optional[str] = None,
        color: Optional[str] = None,
        vehicle_type: Optional[str] = None,
        fuel: Optional[str] = None,
        gearbox: Optional[str] = None,
        owner_type: Optional[str] = None,
    ):
        """
        Send a POST request to retrieve available filters according to hierarchy.
        Returns a dictionary with models, colors, types, fuels, gearboxes, and owner types.
        """
        logging.info(f"Starting get_filtre for brand={brand}, model={model}, color={color}")

        json_data = {
            "filters": {
                "category": {"id": "2"},
                "enums": {
                    "ad_type": ["offer"],
                    "u_car_brand": [brand],
                    "u_car_model": [model] if model else [],
                    "vehicule_color": [color] if color else [],
                    "vehicle_type": [vehicle_type] if vehicle_type else [],
                    "fuel": [fuel] if fuel else [],
                    "gearbox": [gearbox] if gearbox else [],
                    "owner_type": [owner_type] if owner_type else [],
                },
                "ranges": {},
            },
            "limit": 0,
            "limit_alu": 0,
            "sort_by": "relevance",
        }

        try:
            response = requests.post(
                "https://api.leboncoin.fr/finder/search",
                cookies=COOKIES,
                headers=HEADERS,
                json=json_data,
            )
            response.raise_for_status()  # Check HTTP status
            data = response.json()       # Parse JSON
            logging.info("Request successful")
        except requests.HTTPError as e:
            logging.info("HTTP Error: %s", e)
            return {}
        except ValueError:
            logging.info("Invalid JSON for filter: %s", json_data)
            return {}
        except requests.RequestException as e:
            logging.info("Request exception: %s", e)
            return {}

        aggregations = data.get("aggregations", {})
        return {
            "models": aggregations.get("u_car_model", {}),
            "colors": aggregations.get("vehicule_color", {}),
            "types": aggregations.get("vehicle_type", {}),
            "fuels": aggregations.get("fuel", {}),
            "gearboxes": aggregations.get("gearbox", {}),
            "owner_types": aggregations.get("owner_type", {}),
        }

    # =====================================================
    # Build a single filter for a request
    # =====================================================
    def build_filtre(
        self,
        brand: str,
        model: Optional[str] = None,
        color: Optional[str] = None,
        vehicle_type: Optional[str] = None,
        fuel: Optional[str] = None,
        gearbox: Optional[str] = None,
        owner_type: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict:
        """
        Build the JSON structure to retrieve ads according to the given criteria.
        """
        logging.info(f"Building filter: brand={brand}, model={model}, color={color}, type={vehicle_type}")
        enums = {"ad_type": ["offer"], "u_car_brand": [brand]}
        if model:
            enums["u_car_model"] = [model]
        if color:
            enums["vehicule_color"] = [color]
        if vehicle_type:
            enums["vehicle_type"] = [vehicle_type]
        if fuel:
            enums["fuel"] = [fuel]
        if gearbox:
            enums["gearbox"] = [gearbox]
        if owner_type:
            enums["owner_type"] = [owner_type]

        return {
            "filters": {"category": {"id": "2"}, "enums": enums},
            "limit": limit,
            "offset": offset,
            "sort_by": "relevance",
            "disable_total": True,
            "listing_source": "pagination",
        }

    # =====================================================
    # Hierarchical handling methods
    # =====================================================
    def handle_models(self, brand: str, models: dict) -> None:
        logging.info(f"Handling models for brand={brand}")
        for model, total_number in models.items():
            if "_model_all" in model:
                logging.info(f"Ignoring model: {model}")
                continue
            if total_number < 3000:
                logging.info(f"Adding filter for model {model} (<3000 ads)")
                filtre = self.build_filtre(brand, model=model)
                self.filters.append(filtre)
            else:
                logging.info(f"Model {model} exceeds 3000 ads, drilling down to colors")
                color_filters = self.get_filtre(brand, model=model)
                self.handle_colors(brand, model, color_filters["colors"])

    def handle_colors(self, brand: str, model: str, colors: dict) -> None:
        logging.info(f"Handling colors for model={model}")
        for color, total_number in colors.items():
            if total_number < 3000:
                logging.info(f"Adding filter for color {color} (<3000 ads)")
                filtre = self.build_filtre(brand, model=model, color=color)
                self.filters.append(filtre)
            else:
                logging.info(f"Color {color} exceeds 3000 ads, drilling down to types")
                type_filters = self.get_filtre(brand, model=model, color=color)
                self.handle_types(brand, model, color, type_filters["types"])

    def handle_types(self, brand: str, model: str, color: str, types: dict) -> None:
        logging.info(f"Handling types for color={color}")
        for vehicle_type, total_number in types.items():
            if total_number < 3000:
                logging.info(f"Adding filter for type {vehicle_type} (<3000 ads)")
                filtre = self.build_filtre(brand, model=model, color=color, vehicle_type=vehicle_type)
                self.filters.append(filtre)
            else:
                logging.info(f"Type {vehicle_type} exceeds 3000 ads, drilling down to fuels")
                fuel_filters = self.get_filtre(brand, model=model, color=color, vehicle_type=vehicle_type)
                self.handle_fuels(brand, model, color, vehicle_type, fuel_filters["fuels"])

    def handle_fuels(self, brand, model, color, vehicle_type, fuels) -> None:
        logging.info(f"Handling fuels for type={vehicle_type}")
        for fuel, total_number in fuels.items():
            if total_number < 3000:
                logging.info(f"Adding filter for fuel {fuel} (<3000 ads)")
                filtre = self.build_filtre(brand, model=model, color=color, vehicle_type=vehicle_type, fuel=fuel)
                self.filters.append(filtre)
            else:
                logging.info(f"Fuel {fuel} exceeds 3000 ads, drilling down to gearboxes")
                gearbox_filters = self.get_filtre(brand, model=model, color=color, vehicle_type=vehicle_type, fuel=fuel)
                self.handle_gearboxes(brand, model, color, vehicle_type, fuel, gearbox_filters["gearboxes"])

    def handle_gearboxes(self, brand, model, color, vehicle_type, fuel, gearboxes) -> None:
        logging.info(f"Handling gearboxes for fuel={fuel}")
        for gearbox, total_number in gearboxes.items():
            if total_number < 3000:
                logging.info(f"Adding filter for gearbox {gearbox} (<3000 ads)")
                self.filters.append(self.build_filtre(brand, model=model, color=color, vehicle_type=vehicle_type, fuel=fuel, gearbox=gearbox))
            else:
                logging.info(f"Gearbox {gearbox} exceeds 3000 ads, drilling down to owner types")
                owner_filters = self.get_filtre(brand, model=model, color=color, vehicle_type=vehicle_type, fuel=fuel, gearbox=gearbox)
                self.handle_owner_types(brand, model, color, vehicle_type, fuel, gearbox, owner_filters["owner_types"])

    def handle_owner_types(self, brand, model, color, vehicle_type, fuel, gearbox, owner_types) -> None:
        logging.info(f"Handling owner types for gearbox={gearbox}")
        for owner_type, total_number in owner_types.items():
            if total_number < 3000:
                logging.info(f"Adding filter for owner type {owner_type} (<3000 ads)")
                self.filters.append(self.build_filtre(brand, model=model, color=color, vehicle_type=vehicle_type, fuel=fuel, gearbox=gearbox, owner_type=owner_type))
            else:
                logging.info(f"Owner type {owner_type} exceeds 3000 ads, adding to over_3000_filters")
                self.over_3000_filters.append({
                    "brand": brand,
                    "model": model,
                    "color": color,
                    "type": vehicle_type,
                    "fuel": fuel,
                    "gearbox": gearbox,
                    "owner_type": owner_type,
                    "total": total_number,
                })

    # =====================================================
    # Main execution method
    # =====================================================
    def run(self, brand: str) -> None:
        logging.info(f"Starting scraping process for brand={brand}")
        model_filters = self.get_filtre(brand)
        self.handle_models(brand, model_filters["models"])

        logging.info("Scraping finished")
        logging.info("Collected filters (<3000 ads): %d", len(self.filters))
        logging.info("Filters exceeding 3000 ads: %d", len(self.over_3000_filters))
        print(self.filters)


if __name__ == "__main__":
    scraper = GetFilters()
    scraper.run("RENAULT")
