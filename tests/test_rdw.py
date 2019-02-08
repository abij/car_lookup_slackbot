from unittest import mock, TestCase

from slackbot.rdw import RdwOnlineClient
import datetime as dt

SOCRATA_RES_DATA = {
    'catalogusprijs': '12345',
    'kenteken': 'AB123ZZ',
    'vervaldatum_apk': '01/10/2019',
    'voertuigsoort': 'Personenauto',
    'merk': 'BMW',
    'handelsbenaming': '1-SERIE',
    'zuinigheidslabel': 'C'
}


class TestRdwOnlineClient(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rdw_client = RdwOnlineClient()

    def test_invalid_too_long(self):
        with self.assertRaises(AssertionError) as e:
            self.rdw_client.get_rdw_details('tooLong')
        assert str(e.exception) == 'Length of the kenteken must be 6 (without any dashes).'

    @mock.patch('sodapy.Socrata.get')
    def test_getting_success_response(self, mock_socrata_get):
        mock_socrata_get.return_value = [SOCRATA_RES_DATA]

        expected = {'catalogusprijs': 12345,
                    'kenteken': 'AB123ZZ',
                    'vervaldatum_apk': '01-10-2019',
                    'dt_vervaldatum_apk': dt.datetime(2019, 10, 1, 0, 0),
                    'voertuigsoort': 'Personenauto',
                    'merk': 'BMW',
                    'handelsbenaming': '1-SERIE',
                    'zuinigheidslabel': 'C'}

        assert self.rdw_client.get_rdw_details('ab123z') == expected
        assert self.rdw_client.get_rdw_details('AB123Z') == expected
        assert self.rdw_client.get_rdw_details('AB-123-Z') == expected

    @mock.patch('sodapy.Socrata.get')
    def test_not_found(self, mock_socrata_get):
        mock_socrata_get.return_value = []
        details = self.rdw_client.get_rdw_details('ab123z')
        self.assertIsNone(details)
