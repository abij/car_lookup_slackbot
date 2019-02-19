import logging
import datetime as dt
from sodapy import Socrata

log = logging.getLogger(__name__)


class RdwOnlineClient:
    GEKENTEKENDE_VOERTUIGEN_DATASET_ID = "m9d7-ebf2"

    def __init__(self, app_token=None):
        self.client = Socrata('opendata.rdw.nl', app_token=app_token)

    def get_rdw_details(self, kenteken):
        kenteken = kenteken.strip().replace('-', '').upper()
        assert len(kenteken) == 6, 'Length of the kenteken must be 6 (without any dashes).'

        # TODO Maybe use async and somekind of timeout
        res = self.client.get(
            self.GEKENTEKENDE_VOERTUIGEN_DATASET_ID, limit=1,
            where='kenteken = "{}"'.format(kenteken),
            select='kenteken, vervaldatum_apk, voertuigsoort, merk, '
                   'handelsbenaming, catalogusprijs, zuinigheidslabel')
        if len(res) == 0:
            log.info('RWD lookup not found. (%s)', kenteken)
            return None

        d = res[0].copy()  # details, first result only (copy, to reuse mocking the return value)

        if 'catalogusprijs' in d:
            d['catalogusprijs'] = int(d['catalogusprijs'])

        if 'vervaldatum_apk' in d:
            d['dt_vervaldatum_apk'] = dt.datetime.strptime(d['vervaldatum_apk'], '%Y%m%d')
            d['vervaldatum_apk'] = d['dt_vervaldatum_apk'].strftime('%d-%m-%Y')

        # TODO Make the names pretty, not always upper (but BMW is upper...)!
        return d
