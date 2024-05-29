from unittest import TestCase
from slackbot import messages

class TestMessages(TestCase):

    def test_command_car_usage(self):
        assert messages.command_car_usage.startswith("Lookup car details including")

    def test_command_invalid_licence_plate(self):
        assert messages.command_invalid_licence_plate('TOO-LONG') == "Input (TOO-LONG) does not look like a valid licence plate (NL-patterns)"

    def test_lookup_no_details_found(self):
        assert messages.lookup_no_details_found('12AAA4') == "`/car 12AAA4` lookup: No details found..."

    def test_found_with_details(self):
        base_expected = "PREFIX, it's a <https://autorapport.finnik.nl/kenteken/12AAA4|*Tesla Model S*>! _(99.9%)_"

        # Only required fields
        assert (messages.found_with_details("12AAA4",
                                           {'model': 'Model S', 'brand': 'Tesla'},
                                           "PREFIX",
                                           confidence=99.87) ==
                base_expected + "\n:person_shrugging: _(`/car tag` to add the owner)_")

        assert (messages.found_with_details("12AAA4",
                                    {'model': 'Model S', 'brand': 'Tesla', 'owner_name': 'John Doe'},
                                    "PREFIX",
                                    confidence=99.87) ==
                base_expected + "\n:person_raising_hand: John Doe")

        assert (messages.found_with_details("12AAA4",
                                            {'model': 'Model S', 'brand': 'Tesla', 'acceleration': '9'},
                                            "PREFIX",
                                            confidence=99.87) ==
                base_expected +
                "\n:person_shrugging: _(`/car tag` to add the owner)_" +
                "\n0-100: 9.0 sec :red_car:")


