import asyncio
import datetime as dt
import logging
import re

import requests

log = logging.getLogger(__name__)

special_brand_mapping = {
    "MERCEDES-BENZ": "Mercedes-Benz",
    "BMW": "BMW",
}

special_name_mapping = {
    "1ER REIHE": "1-Serie",
    "3ER REIHE": "3-Series",
    "5ER REIHE": "5-Series",
    "7ER REIHE": "7-Series",
    "Z REIHE": "Z",
    "X REIHE": "X",
    "VX 50": "VX 50",
    "MINI": "Mini",
    "ASTRA+": "Astra+",
    "CADDY SDI 51 KW BESTEL": "Caddy",
    "PARTNER 170C 1.9D": "Partner",
}


def capitalize_words(s: str) -> str:
    return re.sub(r"\w+", lambda m: m.group(0).capitalize(), s)


def prettify_brand(brand: str) -> str:
    if brand in special_brand_mapping:
        return special_brand_mapping[brand]
    return capitalize_words(brand.lower())


def prettify_model(brand: str, model: str) -> str:
    if model in special_name_mapping:
        return special_name_mapping[model]
    model = model.replace(brand, "").replace(brand.replace(" ", ""), "").strip()
    if len(model) <= 6 and not model.isalpha():
        return model
    return capitalize_words(model.lower())


class RdwOnlineClient:
    _URL = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"

    def __init__(self, app_token: str | None = None) -> None:
        self.app_token = app_token

    async def get_rdw_details(self, plate: str) -> dict | None:
        plate = plate.strip().replace("-", "").upper()
        if len(plate) != 6:
            raise ValueError("Licence plate must be 6 characters (no dashes)")

        headers = {"X-App-Token": self.app_token} if self.app_token else {}
        params = {
            "$limit": 1,
            "$where": f'kenteken = "{plate}"',
            "$select": "kenteken,merk,handelsbenaming,catalogusprijs,bruto_bpm,vervaldatum_apk",
        }

        res = await asyncio.to_thread(requests.get, self._URL, params=params, headers=headers, timeout=2.5)
        res.raise_for_status()
        data = res.json()
        log.info("RDW lookup for %s: %s", plate, data)

        if not data:
            log.info("RDW lookup not found for %s", plate)
            return None

        d = data[0]
        price = int(d.get("catalogusprijs") or 0) or None
        bpm = int(d.get("bruto_bpm") or 0) or None

        apk = None
        if "vervaldatum_apk" in d:
            try:
                apk = dt.datetime.strptime(d["vervaldatum_apk"], "%Y%m%d").strftime("%d-%m-%Y")
            except ValueError:
                log.warning("Unexpected APK date format: %s", d["vervaldatum_apk"])

        return {
            "plate": d["kenteken"],
            "brand": prettify_brand(d["merk"]),
            "model": prettify_model(d["merk"], d["handelsbenaming"]),
            "apk": apk,
            "price": price,
            "bpm": bpm,
            "acceleration": None,
        }
