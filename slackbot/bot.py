import asyncio
import logging
import os
import re
from typing import Optional

from slackbot import licence_plate, messages
from slackbot.finnik import FinnikOnlineClient
from slackbot.owners import CarOwners
from slackbot.rdw import RdwOnlineClient

log = logging.getLogger(__name__)


class Bot:
    def __init__(self) -> None:
        self.rdw_client = RdwOnlineClient(os.environ.get("RWD_APPTOKEN"))
        self.car_owners = CarOwners(csv_path=os.environ.get("CAR_OWNERS_FILE", "/tmp/car-owners.csv"))
        self.finnik_client = FinnikOnlineClient()

    async def command_car(self, user_id: str, text: str) -> str:
        stripped = text.lower().strip()
        if not stripped or stripped == "help":
            return messages.command_car_usage

        words = text.strip().split()
        first = words[0]

        if len(words) == 1 and first.lower() in ("tag", "untag"):
            return messages.command_tag_usage

        if len(words) == 1:
            plate = licence_plate.normalize(first)
            if not licence_plate.is_valid(plate):
                return messages.command_invalid_licence_plate(first)

            details = await self.get_licence_plate_details(plate)
            if not details:
                return messages.lookup_no_details_found(plate)
            return messages.found_with_details(plate, details, f"`/car {plate}`")

        sub = first.lower()
        if sub in ("tag", "untag"):
            plate = licence_plate.normalize(words[1])
            if not licence_plate.is_valid(plate):
                return messages.command_invalid_licence_plate(words[1])

            if sub == "tag":
                if len(words) == 2:
                    self.car_owners.tag(plate, slackid=user_id)
                    log.info('Tagged "%s" to %s', plate, user_id)
                    return messages.command_tag_added(plate, user_id=user_id)

                owner = " ".join(words[2:]).strip()
                match_in_quotes = re.match(r'["\u201c](.+?)["\u201d]', owner)
                min_chars, max_chars = 3, 32

                if owner.startswith("@"):
                    slack_id = user_id if owner.lower() == "@me" else owner.lstrip("@")
                    self.car_owners.tag(plate, slackid=slack_id)
                    log.info('Tagged "%s" to %s', plate, slack_id)
                    return messages.command_tag_added(plate, user_id=slack_id)

                if match_in_quotes:
                    owner = match_in_quotes.group(1)
                    if not (min_chars <= len(owner) <= max_chars) or not self._is_valid_owner(owner):
                        return messages.command_invalid_owner(owner, min_chars, max_chars)
                    self.car_owners.tag(plate, name=owner)
                    return messages.command_tag_added(plate, owner=owner)

                return messages.command_invalid_owner(owner, min_chars, max_chars)

            if sub == "untag":
                self.car_owners.untag(user_id, plate)
                return messages.command_untag(plate)

        return messages.command_car_usage

    async def get_licence_plate_details(self, plate: str) -> Optional[dict]:
        plate = licence_plate.normalize(plate)

        owner_result, rdw_result, finnik_result = await asyncio.gather(
            self.car_owners.lookup(plate),
            self.rdw_client.get_rdw_details(plate),
            self.finnik_client.get_car_details(plate),
            return_exceptions=True,
        )

        details: dict = {}

        if isinstance(owner_result, dict):
            details["owner_slackid"] = owner_result.get("slackid")
            details["owner_name"] = owner_result.get("name")
        elif isinstance(owner_result, Exception):
            log.warning("Owner lookup failed: %s", owner_result)

        slow_sources = []

        if isinstance(rdw_result, dict):
            details.update(rdw_result)
        elif isinstance(rdw_result, Exception):
            log.warning("RDW lookup failed: %s", rdw_result)
            slow_sources.append("RDW")

        if isinstance(finnik_result, dict):
            # RDW has preference — only fill missing keys
            for k, v in finnik_result.items():
                if v and details.get(k) is None:
                    details[k] = v
        elif isinstance(finnik_result, Exception):
            log.warning("Finnik lookup failed: %s", finnik_result)
            slow_sources.append("Finnik")

        if slow_sources:
            details["_slow_sources"] = slow_sources

        return details if details else None

    @staticmethod
    def _is_valid_owner(owner: str) -> bool:
        return re.match(r"^[a-zA-Z]+(([',. -]{0,2}[a-zA-Z ])?[a-zA-Z.!?]*)*$", owner) is not None
