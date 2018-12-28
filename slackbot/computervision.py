import subprocess
import json
import logging
from azure.cognitiveservices.vision.computervision import ComputerVisionAPI

log = logging.getLogger(__name__)


class LicenceplaceExtractor:
    def find_licenceplates(self, file_name):
        pass


class AzureCongitiveOCRLicenceplaceExtractor(LicenceplaceExtractor):
    def __init__(self, *args, region='westeurope', key=None, **kwargs):
        super(AzureCongitiveOCRLicenceplaceExtractor, self).__init__(*args, **kwargs)
        self.computer_vision = ComputerVisionAPI(azure_region=region, credentials=key)

    def find_licenceplates(self, file_name):
        # TODO Implement the Azure Cognitive OCR here.
        # Note: URL's must end with .jpg or .png
        # self.computer_vision.recognize_printed_text()
        raise NotImplementedError


class OpenAlprLicenceplaceExtractor(LicenceplaceExtractor):
    def find_licenceplates(self, file_name):
        """
        Take the matches with highest confidence following the NL pattern.

        :param file_name: File to check
        :return: Generator of: [ {'confidence': 95.0374, 'plate': 'ND5222'}, ... ]
        """
        stdout = subprocess.getoutput('alpr --json --topn 10 --country eu --pattern nl ' + file_name)

        # Optional: libdc1394 error: Failed to initialize libdc1394
        # Can be solved with mounting /dev/null to /dev/raw1394. But didn't work for me...
        output = stdout.splitlines()[-1]

        if "alpr: command not found" in output:
            log.warning('Command not found: "alpr", '
                        'are you running inside the OpenALPR container? (skipping file: %s)', file_name)
            return []

        if 'Unknown file type' in output:
            log.error('Unknown file_type: %s', file_name)
            return []

        if 'Image file not found' in output:
            log.error('Cannot find file: %s', file_name)
            return []

        if output.startswith('{'):
            lookup = json.loads(output)
            if not lookup['results']:  # empty array, nothing found...
                log.info('No plate found in image: %s', file_name)
                return []

            for match in lookup['results']:
                yield {'confidence': match['confidence'], 'plate': match['plate']}
        else:
            raise ValueError("Unable to parse result from 'alpr' command: " + output)
