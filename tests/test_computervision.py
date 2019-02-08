from unittest import mock, TestCase
from slackbot.computervision import OpenAlprLicenceplaceExtractor


class TestOpenAlprLicenceplaceExtractor(TestCase):

    json_result_1_car = """libdc1394 error: Failed to initialize libdc1394
{"version":2,"data_type":"alpr_results","epoch_time":1549623852465,"img_width":978,"img_height":550,"processing_time_ms":140.426605,"regions_of_interest":[{"x":0,"y":0,"width":978,"height":550}],"results":[{"plate":"28ZTP6","confidence":91.048470,"matches_template":1,"plate_index":0,"region":"nl","region_confidence":0,"processing_time_ms":21.577200,"requested_topn":3,"coordinates":[{"x":401,"y":341},{"x":507,"y":336},{"x":508,"y":357},{"x":403,"y":362}],"candidates":[{"plate":"28ZTP6","confidence":91.048470,"matches_template":1},{"plate":"Z8ZTP6","confidence":81.835892,"matches_template":0},{"plate":"2BZTP6","confidence":80.385742,"matches_template":0}]}]}"""

    json_result_3_cars = """{"version":2,"data_type":"alpr_results","epoch_time":1549622221313,"img_width":4032,"img_height":3024,"processing_time_ms":882.581421,"regions_of_interest":[{"x":0,"y":0,"width":4032,"height":3024}],"results":[{"plate":"AA123B","confidence":87.118919,"matches_template":0,"plate_index":0,"region":"nl","region_confidence":0,"processing_time_ms":20.389700,"requested_topn":3,"coordinates":[{"x":3089,"y":1269},{"x":3315,"y":1250},{"x":3316,"y":1295},{"x":3088,"y":1315}],"candidates":[{"plate":"AA123B","confidence":87.118919,"matches_template":0},{"plate":"NH5I0G","confidence":84.773361,"matches_template":0},{"plate":"JNH5IOG","confidence":83.143814,"matches_template":0}]},{"plate":"BB123B","confidence":92.664085,"matches_template":1,"plate_index":1,"region":"nl","region_confidence":0,"processing_time_ms":15.931700,"requested_topn":3,"coordinates":[{"x":760,"y":1414},{"x":1035,"y":1390},{"x":1040,"y":1440},{"x":766,"y":1465}],"candidates":[{"plate":"BB123B","confidence":92.664085,"matches_template":1},{"plate":"PX27ZS","confidence":89.320732,"matches_template":1},{"plate":"PXZ72S","confidence":83.934135,"matches_template":1}]},{"plate":"CC555C","confidence":90.570259,"matches_template":1,"plate_index":2,"region":"nl","region_confidence":0,"processing_time_ms":16.831499,"requested_topn":3,"coordinates":[{"x":2149,"y":1299},{"x":2373,"y":1275},{"x":2379,"y":1325},{"x":2155,"y":1350}],"candidates":[{"plate":"CC555C","confidence":90.570259,"matches_template":1},{"plate":"TX5S5G","confidence":81.609406,"matches_template":0},{"plate":"TXS55G","confidence":81.413521,"matches_template":1}]}]}\n"""

    file_out_found = "libdc1394 error: Failed to initialize libdc1394\nImage file not found: 3sdfsdf.jpg"

    unknown_type = "libdc1394 error: Failed to initialize libdc1394\nUnknown file type"

    @classmethod
    def setUpClass(cls):
        cls.computervision = OpenAlprLicenceplaceExtractor()

    @mock.patch('subprocess.getoutput', return_value=json_result_1_car)
    def test_find_licenceplates_one(self, mock_alpr):
        # generator:
        finder = self.computervision.find_licenceplates('MyFile.jpg')
        results = list(finder)

        assert len(results) == 1
        assert results[0] == {'confidence': 91.04847, 'plate': '28ZTP6', 'valid_nl_pattern': True}
        # Validate call to system process:
        mock_alpr.assert_called_with('alpr --json --topn 10 --country eu --pattern nl MyFile.jpg')

    @mock.patch('subprocess.getoutput', return_value=json_result_3_cars)
    def test_find_licenceplates_multiple(self, mock_openalpr):
        # generator:
        finder = self.computervision.find_licenceplates('MyFile.jpg')

        results = list(finder)

        assert len(results) == 3
        assert results[0] == {'confidence': 87.118919, 'plate': 'AA123B', 'valid_nl_pattern': False}
        assert results[1] == {'confidence': 92.664085, 'plate': 'BB123B', 'valid_nl_pattern': True}
        assert results[2] == {'confidence': 90.570259, 'plate': 'CC555C', 'valid_nl_pattern': True}
        # Validate call to system process:
        mock_openalpr.assert_called_with('alpr --json --topn 10 --country eu --pattern nl MyFile.jpg')

    @mock.patch('subprocess.getoutput', return_value=file_out_found)
    def test_find_licenceplates_not_found(self, mock_alpr):
        results = list(self.computervision.find_licenceplates('3sdfsdf.jpg'))
        assert len(results) == 0

    @mock.patch('subprocess.getoutput', return_value=unknown_type)
    def test_find_licenceplates_invalid_filetype(self, mock_alpr):
        results = list(self.computervision.find_licenceplates('file.csv'))
        assert len(results) == 0
