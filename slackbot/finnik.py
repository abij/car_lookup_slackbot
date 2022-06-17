"""
Lookup licence plate details on the www.finnik.nl.
"""
import logging
import requests
from bs4 import BeautifulSoup
import datetime as dt
from slackbot import licence_plate
import re

DEFAULT_SERVICE_FAILURE_TIMEOUT_SEC = 15
SERVICE_FAILURE_EXPONENTIAL_MULTIPLIER = 2
SERVICE_FAILURE_MAX_TIMEOUT_SEC = 1800  # 30 minutes


log = logging.getLogger(__name__)


def _get_label_text(row):
    text = row.find_next("div", {"class": "label"}).text
    if text:
        return text.strip()
    return ""


def _get_value_text(row):
    text = row.find_next("div", {"class": "value"}).text
    if text:
        return text.strip()
    return ""


class FinnikOnlineClient:
    last_failure = None
    service_failure_timeout = DEFAULT_SERVICE_FAILURE_TIMEOUT_SEC

    def get_car_details(self, plate):
        plate = licence_plate.normalize(plate)
        assert len(plate) == 6, 'Length of the licenceplate must be 6 (without any dashes).'

        if self.last_failure and (dt.datetime.now() - self.last_failure).total_seconds() < self.service_failure_timeout:
            log.warning("Finnik last request failed less than %s sec ago (skip)", self.service_failure_timeout)
            return None

        try:
            # Slack-commands are synchronous, max timeout 3sec
            # Slack events are asynchronous, than we have enough time.
            res = requests.get('https://autorapport.finnik.nl/kenteken/' + plate, timeout=(3, 3))
            res.raise_for_status()
        except Exception as e:
            self.enable_service_timeout()
            log.warning("Request to Finnik failed, Disable service for %s sec.", self.service_failure_timeout)
            raise e

        self.disable_service_timeout()

        soup = BeautifulSoup(res.content, "html.parser")

        section_basic_info = soup.find('section', {"data-sectiontype": "BasicInformation"})
        section_quickcheck = soup.find('section', {"class": "quickcheck"})
        section_value_info = soup.find('section', {"data-sectiontype": "ValueInformation"})

        if not section_basic_info or not section_quickcheck or not section_value_info:
            log.warning("Successful response, but not all sections (BasicInformation, quickcheck, ValueInformation) not found! "
                        "Is the site changed? Disable service for %s sec.", self.service_failure_timeout)
            self.enable_service_timeout()
            return None

        brand = section_basic_info.find_all("div", {"class": "value"})[0].text
        if brand:
            brand = brand.strip()

        model = section_basic_info.find_all("div", {"class": "value"})[1].text
        if model:
            model = model.strip()

        acceleration = None
        div_speed = section_quickcheck.find_all("div", {"class": "speed"})[0]
        if "0-100" in div_speed.text:
            acceleration_text = div_speed.find("span").text
            acceleration = acceleration_text.split()[0].replace(",",".")

        apk = None
        div_apk = section_quickcheck.find_next("div", {"class": "garage"})
        if "APK" in div_apk.text:
            apk = div_apk.find("span").text.strip()

        rows = section_value_info.find_all("div", {"class": "row"})

        price = None
        price_raw = [_get_value_text(r) for r in rows if 'nieuwprijs' in _get_label_text(r).lower()]
        if price_raw:
            price = int(re.sub(r"\D", '', price_raw[0]))

        bpm = None
        bpm_raw = [_get_value_text(r) for r in rows if 'bpm' in _get_label_text(r).lower()]
        if bpm_raw and "onbekend" not in bpm_raw[0].lower():
            bpm = int(re.sub(r"\D", '', bpm_raw[0]))

        result = {
            'brand': brand,
            'model': model,
            'apk': apk,
            'price': price,
            'bpm': bpm,
            'acceleration': acceleration,
        }
        log.info("Finnik lookup for %s result: %s", plate, result)
        return result


    def enable_service_timeout(self):
        if self.last_failure is not None:
            next_exp_backoff = int(self.service_failure_timeout * SERVICE_FAILURE_EXPONENTIAL_MULTIPLIER)
            self.service_failure_timeout = min(SERVICE_FAILURE_MAX_TIMEOUT_SEC, next_exp_backoff)
        self.last_failure = dt.datetime.now()

    def disable_service_timeout(self):
        self.last_failure = None
        self.service_failure_timeout = DEFAULT_SERVICE_FAILURE_TIMEOUT_SEC
