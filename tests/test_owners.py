from unittest import TestCase
from slackbot.owners import CarOwners
import os

TEST_CSV = os.path.join(os.path.dirname(__file__), 'dummy_owners.csv')


class TestCarOwners(TestCase):

    @classmethod
    def setUpClass(cls):
        # Make a new file each time
        with open(TEST_CSV, 'w') as f:
            f.writelines(['"kenteken","slackid","name"\n',
                          '"AA123Z","U12345","John Do"\n'])
        cls.car_owners = CarOwners(csv_path=TEST_CSV)

    @classmethod
    def tearDownClass(cls):
        os.remove(TEST_CSV)

    def test_lookup_success(self):
        result = self.car_owners.lookup('AA123Z')
        assert result == {'slackid': 'U12345', 'name': 'John Do'}

    def test_lookup_invalid(self):
        with self.assertRaises(AssertionError) as e:
            self.car_owners.lookup('TOO-LONG')
        assert str(e.exception) == 'Length of the kenteken must be 6 (without any dashes)'

    def test_lookup_not_found(self):
        result = self.car_owners.lookup('BB123B')
        self.assertIsNone(result)

    def test_tag_invalid_kenteken(self):
        with self.assertRaises(AssertionError) as e:
            self.car_owners.tag('U123456', 'TOOLONG')
        assert str(e.exception) == 'Length of the kenteken must be 6 (without any dashes)'

    def test_tag_and_untag(self):
        new_kenteken = 'CC333C'
        self.car_owners.tag('U123456', new_kenteken)

        # New entry should be found, and persisted:
        assert self.car_owners.lookup(new_kenteken) == {'slackid': 'U123456', 'name': None}

        with open(TEST_CSV) as f:
            data = f.readlines()
            line = data[-1].strip()  # strip off the new-line char
        nr_rows = len(data)

        assert line == '"CC333C","U123456",""'

        # Lets remove this entry:
        self.car_owners.untag('U123456', new_kenteken)

        # should not be there anymore (lookup + data-file)
        nr_rows_untagged = sum(1 for _ in open(TEST_CSV))
        assert nr_rows_untagged == (nr_rows - 1)
        self.assertIsNone(self.car_owners.lookup(new_kenteken))
