import os
import logging
import pandas as pd

from slackbot import licence_plate

log = logging.getLogger(__name__)


class CarOwners:
    # Source data:
    # https://intranet.xebia.com/display/XNL/Xebia+Group+Kenteken+Registratie

    def __init__(self, csv_path='/data/car-owners.csv'):
        self.csv_path = csv_path
        self.owners_df = None
        self.load()

    def tag(self, plate, slackid=None, name=None):
        plate = licence_plate.normalize(plate)
        assert len(plate) == 6, 'Length of the licence plate must be 6 (without any dashes)'

        if slackid.startswith('@'):
            slackid = slackid[1:]

        self.load()
        if plate in self.owners_df.index:
            self.owners_df.loc[plate, 'slackid'] = slackid or ''
            self.owners_df.loc[plate, 'name'] = name or ''
        else:
            new_data = pd.Series({'slackid': slackid, 'name': name}, name=plate)
            self.owners_df = self.owners_df.append(new_data)
            self.owners_df = self.owners_df.where((pd.notnull(self.owners_df)), None)
        self.save()

    def untag(self, slackid, plate):
        self.load()
        self.owners_df.drop([plate], inplace=True)
        self.save()

    def lookup(self, plate):
        """
        :return: Dict with 'name' and 'slackid' or None is not found
        """
        plate = licence_plate.normalize(plate)
        assert len(plate) == 6, 'Length of the licence plate must be 6 (without any dashes)'

        self.load()
        if plate not in self.owners_df.index:
            log.info('Owner lookup for %s result: not found.', plate)
            return None

        res = self.owners_df.loc[plate]
        log.info('Owner lookup for %s result: found: %s', plate, res.to_dict())
        return res.to_dict()

    def load(self):
        if not os.path.exists(self.csv_path):
            empty_df = pd.DataFrame(columns=['kenteken', 'slackid', 'name'], dtype=str)
            empty_df.set_index('kenteken', inplace=True)
            self.owners_df = empty_df
        else:
            self.owners_df = pd.read_csv(self.csv_path, header=0, index_col='kenteken', quoting=1, dtype=str)
            self.owners_df = self.owners_df.where((pd.notnull(self.owners_df)), None)

    def save(self):
        self.owners_df.to_csv(self.csv_path, header=True, quoting=1, index_label=["kenteken"])
