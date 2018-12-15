import datetime as dt
from sodapy import Socrata


class RdwOnlineClient:
    GEKENTEKENDE_VOERTUIGEN_DATASET_ID = "m9d7-ebf2"

    def __init__(self, app_token=None):
        self.client = Socrata('opendata.rdw.nl', app_token=app_token)

    def get_rdw_details(self, kenteken):
        kenteken = kenteken.strip().replace('-', '').upper()

        assert len(kenteken) == 6, 'Length of the kenteken must be 6 (without any dashes).'
        assert kenteken.isupper(), 'The kenteken must be UPPERCASE'

        # TODO Maybe use async and somekind of timeout
        res = self.client.get(
            self.GEKENTEKENDE_VOERTUIGEN_DATASET_ID, limit=1,
            where='kenteken = "{}"'.format(kenteken),
            select='kenteken, vervaldatum_apk, voertuigsoort, merk, '
                   'handelsbenaming, catalogusprijs, zuinigheidslabel')
        if len(res) == 0:
            print('RWD lookup not found. ({})'.format(kenteken))
            return None

        d = res[0]  # details, first result

        if 'catalogusprijs' in d:
            d['catalogusprijs'] = int(d['catalogusprijs'])

        if 'vervaldatum_apk' in d:
            d['dt_vervaldatum_apk'] = dt.datetime.strptime(d['vervaldatum_apk'], '%d/%m/%Y')
            d['vervaldatum_apk'] = d['dt_vervaldatum_apk'].strftime('%d-%m-%Y')

        # TODO Make the names Snakecase, not upper!
        return d
