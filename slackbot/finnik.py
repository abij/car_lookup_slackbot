"""
Lookup licence plate details on the www.finnik.nl.
"""
import logging
import requests
from bs4 import BeautifulSoup
import datetime as dt
from slackbot import licence_plate

DEFAULT_SERVICE_FAILURE_TIMEOUT_SEC = 15
SERVICE_FAILURE_EXPONENTIAL_MULTIPLIER = 2
SERVICE_FAILURE_MAX_TIMEOUT_SEC = 1800  # 30 minutes


log = logging.getLogger(__name__)


class FinnikOnlineClient:
    last_failure = None
    service_failure_timeout = DEFAULT_SERVICE_FAILURE_TIMEOUT_SEC

    def get_acceleration_details(self, plate):
        plate = licence_plate.normalize(plate)
        assert len(plate) == 6, 'Length of the licenceplate must be 6 (without any dashes).'

        if self.last_failure and (dt.datetime.now() - self.last_failure).total_seconds() < self.service_failure_timeout:
            log.warning("Finnik last request failed less than %s sec ago (skip)", self.service_failure_timeout)
            return None

        res = requests.get('https://autorapport.finnik.nl/kenteken/' + plate, timeout=(5, 5))

        if not res.ok:
            if self.last_failure is not None:
                next_exp_backoff = int(self.service_failure_timeout * SERVICE_FAILURE_EXPONENTIAL_MULTIPLIER)
                self.service_failure_timeout = min(SERVICE_FAILURE_MAX_TIMEOUT_SEC, next_exp_backoff)
            log.warning("Unsuccessful lookup: (%s) %s. Disable service for %s sec.", res.status_code, res.reason, self.service_failure_timeout)
            self.last_failure = dt.datetime.now()
            return None

        # reset after success:
        self.last_failure = None
        self.service_failure_timeout = DEFAULT_SERVICE_FAILURE_TIMEOUT_SEC

        soup = BeautifulSoup(res.content, "html.parser")

        div = soup.find("div", id="summary-new")
        if not div:
            log.warning("Successful response, but element ('div', id='summary-new') not found! Is the site changed? Disable service for %s sec.",
                        self.service_failure_timeout)
            self.last_failure = dt.datetime.now()
            return None

        acceleration_item = div.find(id="value-acceleratie")
        if not acceleration_item:
            log.warning("Successful response, but element (id='value-acceleratie') not found! Is the site changed? Disable service for %s sec.",
                        self.service_failure_timeout)
            self.last_failure = dt.datetime.now()
            return None

        acceleration = acceleration_item.text.replace("seconden", "").strip()
        return acceleration
