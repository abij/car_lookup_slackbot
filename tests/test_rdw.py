from unittest import mock, TestCase

from slackbot.rdw import RdwOnlineClient, prettify_model, prettify_brand

SOCRATA_RES_DATA = {
    'kenteken': 'AB123ZZ',
    'merk': 'BMW',
    'handelsbenaming': '1ER REIHE',
    'catalogusprijs': '12345',
    #'vervaldatum_apk': '01/10/2019', update from opendata.rdw.nl on mid Februari
    'vervaldatum_apk': '20191001',
    'bruto_bpm': '2345',
}


class TestRdwOnlineClient(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rdw_client = RdwOnlineClient()

    async def test_invalid_too_long(self):
        with self.assertRaises(AssertionError) as e:
            await self.rdw_client.get_rdw_details('tooLong')
        assert str(e.exception) == 'Length of the licence plate must be 6 (without any dashes).'

    @mock.patch('sodapy.Socrata.get')
    async def test_getting_success_response(self, mock_socrata_get):
        mock_socrata_get.return_value = [SOCRATA_RES_DATA]

        expected = {'plate': 'AB123ZZ',
                    'brand': 'BMW',
                    'model': '1-Serie',
                    'price': 12345,
                    'apk': '01-10-2019',
                    'bpm': 2345,
                    'acceleration': None
                    }

        assert await self.rdw_client.get_rdw_details('ab123z') == expected
        assert await self.rdw_client.get_rdw_details('AB123Z') == expected
        assert await self.rdw_client.get_rdw_details('AB-123-Z') == expected

    @mock.patch('sodapy.Socrata.get')
    async def test_not_found(self, mock_socrata_get):
        mock_socrata_get.return_value = []
        details = await self.rdw_client.get_rdw_details('ab123z')
        self.assertIsNone(details)

    def test_prettify_brand(self):
        assert prettify_brand("VOLKSWAGEN") == "Volkswagen"
        assert prettify_brand("BMW") == "BMW"
