import logging
import datetime as dt
import re
from sodapy import Socrata

log = logging.getLogger(__name__)


special_brand_mapping = {
    "MERCEDES-BENZ": "Mercedes-Benz",
    "BMW": "BMW"
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
    "PARTNER 170C 1.9D": "Partner"
}


def capitalize_words(s):
    return re.sub(r'\w+', lambda m:m.group(0).capitalize(), s)


def prettify_brand(brand):
    if brand in special_brand_mapping:
        return special_brand_mapping[brand]
    # default: uppercase first letter.
    return capitalize_words(brand.lower())


def prettify_model(brand, model):
    if model in special_name_mapping:
        return special_name_mapping[model]

    model = model.replace(brand, "").replace(brand.replace(" ", ""), "").strip()

    # Its probably a code like: IX35 / DS3 / CX-5
    if len(model) <= 6 and not model.isalpha():
        return model

    # default: uppercase first letter.
    return capitalize_words(model.lower())


class RdwOnlineClient:
    GEKENTEKENDE_VOERTUIGEN_DATASET_ID = "m9d7-ebf2"

    def __init__(self, app_token=None):
        self.client = Socrata('opendata.rdw.nl', app_token=app_token)

    def get_rdw_details(self, plate):
        plate = plate.strip().replace('-', '').upper()
        assert len(plate) == 6, 'Length of the licence plate must be 6 (without any dashes).'

        # TODO Maybe use async and somekind of timeout
        res = self.client.get(
            self.GEKENTEKENDE_VOERTUIGEN_DATASET_ID, limit=1,
            where='kenteken = "{}"'.format(plate),
            select='kenteken, merk, handelsbenaming, catalogusprijs, vervaldatum_apk')
        if len(res) == 0:
            log.info('RWD lookup not found. (%s)', plate)
            return None

        d = res[0].copy()  # details, first result only (copy, to reuse mocking the return value)

        if 'catalogusprijs' in d:
            d['catalogusprijs'] = int(d['catalogusprijs'])

        if 'vervaldatum_apk' in d:
            d['dt_vervaldatum_apk'] = dt.datetime.strptime(d['vervaldatum_apk'], '%Y%m%d')
            d['vervaldatum_apk'] = d['dt_vervaldatum_apk'].strftime('%d-%m-%Y')

        return {
            'plate': d['kenteken'],
            'brand': prettify_brand(d['merk']),
            'model': prettify_model(d['merk'], d['handelsbenaming']),
            'apk': d['vervaldatum_apk'],
            'price': d['catalogusprijs'],
            'acceleration': None
        }
