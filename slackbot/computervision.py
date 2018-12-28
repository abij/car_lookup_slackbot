import subprocess
import json
import logging
from azure.cognitiveservices.vision.computervision import ComputerVisionAPI

log = logging.getLogger()


class LicenceplaceExtractor:
    def find_licenceplates(self, file_name):
        pass


class AzureCongitiveOCRLicenceplaceExtractor(LicenceplaceExtractor):
    def __init__(self, *args, region='westeurope', key=None, **kwargs):
        super(AzureCongitiveOCRLicenceplaceExtractor, self).__init__(*args, **kwargs)
        self.computer_vision = ComputerVisionAPI(azure_region=region, credentials=key)

    def find_licenceplates(self, file_name):
        self.computer_vision.recognize_printed_text()
        pass


class OpenAlprLicenceplaceExtractor(LicenceplaceExtractor):
    def find_licenceplates(self, file_name):
        """
        Take the first match with highest confidence.

       :param file_name: File to check
       :return: {'confidence': 95.0374, 'plate': 'ND5222'} or None
       """
        stdout = subprocess.getoutput('alpr --json --topn 10 --country eu --pattern nl ' + file_name)
        # Optional: libdc1394 error: Failed to initialize libdc1394
        # Can be solved with mounting /dev/null to /dev/raw1394. But didn't work for me...
        output = stdout.splitlines()[-1]

        # Unknown file type
        # Image file not found: test_images/IMG_0015s.JPG

        if "alpr: command not found" in output:
            log.warning('Command not found: "alpr", '
                        'are you running inside the OpenALPR container? (skipping file: %s)', file_name)
            return

        if 'Unknown file type' in output:
            log.error('Unknown file_type: %s', file_name)
            return

        if 'Image file not found' in output:
            log.error('Cannot find file: %s', file_name)
            return

        if output.startswith('{'):
            lookup = json.loads(output)
            if not lookup['results']:  # empty array, nothing found...
                log.info('No plate found in image: %s', file_name)
                return

            # TODO Return more than 1 result, when therre are more cars in the picture!
            match = lookup['results'][0]
            return {'confidence': match['confidence'], 'plate': match['plate']}

        raise ValueError("Unable to parse result from 'alpr' command: " + output)
