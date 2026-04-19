"""
Lookup licence plate details on the www.finnik.nl.
"""
import asyncio
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

    async def get_car_details(self, plate):
        plate = licence_plate.normalize(plate)
        if len(plate) != 6:
            raise ValueError("Licence plate must be 6 characters (no dashes)")

        if self.last_failure and (dt.datetime.now() - self.last_failure).total_seconds() < self.service_failure_timeout:
            log.warning("Finnik last request failed less than %s sec ago (skip)", self.service_failure_timeout)
            return None

        try:
            url = 'https://finnik.nl/kenteken/' + plate.lower() + '/gratis'
            res = await asyncio.to_thread(requests.get, url, timeout=(2, 2.5), headers={'User-Agent': 'Mozilla/5.0'})
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

        value_divs = section_basic_info.find_all("div", {"class": "value"})
        brand = value_divs[0].text.strip() if len(value_divs) > 0 else None
        model = value_divs[1].text.strip() if len(value_divs) > 1 else None

        acceleration = None
        speed_divs = section_quickcheck.find_all("div", {"class": "speed"})
        div_speed = speed_divs[0] if speed_divs else None
        if div_speed and "0-100" in div_speed.text:
            span = div_speed.find("span")
            if span:
                acceleration = span.text.split()[0].replace(",", ".")

        apk = None
        div_apk = section_quickcheck.find_next("div", {"class": "garage"})
        if div_apk and "APK" in div_apk.text:
            span = div_apk.find("span")
            if span:
                apk = span.text.strip()

        rows = section_value_info.find_all("div", {"class": "row"})

        price = None
        price_raw = [_get_value_text(r) for r in rows if 'nieuwprijs' in _get_label_text(r).lower()]
        if price_raw:
            digits = re.sub(r"\D", '', price_raw[0])
            price = int(digits) if digits else None

        bpm = None
        bpm_raw = [_get_value_text(r) for r in rows if 'bpm' in _get_label_text(r).lower()]
        if bpm_raw and "onbekend" not in bpm_raw[0].lower():
            digits = re.sub(r"\D", '', bpm_raw[0])
            bpm = int(digits) if digits else None

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
