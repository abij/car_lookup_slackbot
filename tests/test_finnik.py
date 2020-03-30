from unittest import mock, TestCase

from slackbot.finnik import FinnikOnlineClient

FINNIK_RES_DATA = """
<html>
<body>
    <div id="base">
        <div id="value-basis-gegevens-merk">BMW</div>
        <div id="value-basis-gegevens-model">3-Serie</div>
    </div>
    <div id="summary-new">
        <li id="value-acceleratie">5,6 seconden</li>
        <li id="value-apk">14-02-2023</li>
        <li id="value-nieuwprijs">€ 1.123.456,-</li>
    </div>
    <div id="value">
        <li id="value-waarde-informatie-bpm">€ 123.456,-</li>
    </div>
</body>
</html>"""


class TestFinnikOnlineClient(TestCase):

    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            json_data=None,
            raise_for_status=None):
        """
        since we typically test a bunch of different
        requests calls for a service, we are going to do
        a lot of mock responses, so its usually a good idea
        to have a helper function that builds these things
        """
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = mock.Mock(
                return_value=json_data
            )
        return mock_resp

    @classmethod
    def setUpClass(cls):
        cls.finnik_client = FinnikOnlineClient()

    def test_invalid_too_long(self):
        with self.assertRaises(AssertionError) as e:
            self.finnik_client.get_car_details('tooLong')
            assert str(e.exception) == 'Length of the licence plate must be 6 (without any dashes).'

    @mock.patch('requests.get')
    def test_getting_success_response(self, mock_requests):
        mock_requests.return_value = self._mock_response(content=FINNIK_RES_DATA)
        assert self.finnik_client.get_car_details('ab123z') == {
            'brand': "BMW",
            'model': "3-Serie",
            'apk': "14-02-2023",
            'price': 1123456,
            'acceleration': "5,6",
            'bpm': 123456
        }
    @mock.patch('requests.get')
    def test_not_found(self, mock_requests):
        mock_requests.return_value = self._mock_response()
        details = self.finnik_client.get_car_details('ab123z')
        self.assertIsNone(details)
