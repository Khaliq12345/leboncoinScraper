import requests
import time

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
LIMIT_TO_SAVE = 100
FILE_NAME = f"./outputs/{time.time()}.csv"


def parse_ad(ad: dict) -> dict:
    parsed_ad = {}

    return parsed_ad


def scrape_one_page(offset: int):
    """Scrape and validate all ads from a single page"""
    json_data = {
        "filters": {
            "category": {
                "id": "2",
            },
            "enums": {
                "ad_type": [
                    "offer",
                ],
            },
        },
        "limit": LIMIT,
        "limit_alu": 3,
        "sort_by": "relevance",
        "offset": offset,
        "disable_total": True,
        "pivot": '{"ids_to_display":["3067616489","3067616465","3012611449","3049618246","3067616335","3022136896","3050803884","3067616295","3067616271","3064705084","3067616280","3054062755","3067616107","3054874123","3054085385","3057915347","3031382464","3067616115","3067616141","3002665047","3067616116","3027206868","2919931453","3064680234","3067616068","3067616054","3067616025","3067187181","3067616010","3067616008","3067615986","3067615985","3067615421","3067615990","3064718287"],"es_pivot":"1759389290000|3064718287","reranker_offset":35,"total":738204,"page_number":1}',
        "referrer_id": "9ab05549-28c7-4183-ae80-0e181ddd0fda",
        "extend": True,
        "listing_source": "pagination",
    }

    response = requests.post(
        "https://api.leboncoin.fr/finder/search",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    data = response.json()
    ads = data.get("ads")
    if not ads:
        return None
    print(f"Total ADS - {len(ads)}")
    for ad in ads:
        parsed_ad = parse_ad(ad)


scrape_one_page(3000)
