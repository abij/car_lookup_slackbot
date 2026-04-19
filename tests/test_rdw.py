from unittest import mock, IsolatedAsyncioTestCase

from slackbot.rdw import RdwOnlineClient, prettify_model, prettify_brand

RDW_API_ROW = {
    'kenteken': 'AB123ZZ',
    'merk': 'BMW',
    'handelsbenaming': '1ER REIHE',
    'catalogusprijs': '12345',
    'vervaldatum_apk': '20191001',
    'bruto_bpm': '2345',
}


class TestRdwOnlineClient(IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls):
        cls.rdw_client = RdwOnlineClient()

    async def test_invalid_too_long(self):
        with self.assertRaises(ValueError) as e:
            await self.rdw_client.get_rdw_details('tooLong')
        assert str(e.exception) == 'Licence plate must be 6 characters (no dashes)'

    @mock.patch('slackbot.rdw.requests.get')
    async def test_getting_success_response(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = [RDW_API_ROW]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        expected = {
            'plate': 'AB123ZZ',
            'brand': 'BMW',
            'model': '1-Serie',
            'price': 12345,
            'apk': '01-10-2019',
            'bpm': 2345,
            'acceleration': None,
        }

        assert await self.rdw_client.get_rdw_details('ab123z') == expected
        assert await self.rdw_client.get_rdw_details('AB123Z') == expected
        assert await self.rdw_client.get_rdw_details('AB-123-Z') == expected

    @mock.patch('slackbot.rdw.requests.get')
    async def test_not_found(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = []
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        details = await self.rdw_client.get_rdw_details('ab123z')
        self.assertIsNone(details)

    def test_prettify_brand(self):
        assert prettify_brand('VOLKSWAGEN') == 'Volkswagen'
        assert prettify_brand('BMW') == 'BMW'
