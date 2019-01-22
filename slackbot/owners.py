import os
import logging
import pandas as pd

log = logging.getLogger(__name__)


class CarOwners:
    # Source data:
    # https://intranet.xebia.com/display/XNL/Xebia+Group+Kenteken+Registratie

    def __init__(self, csv_path='/data/car-owners.csv'):
        super(CarOwners, self).__init__()
        self.csv_path = csv_path
        self.owners_df = None
        self.load()

    def tag(self, slackid, kenteken, name=''):
        self.load()
        if kenteken in self.owners_df.index:
            self.owners_df.loc[kenteken, 'slackid'] = slackid
        else:
            new_data = pd.Series({'slackid': slackid, 'name': name}, name=kenteken)
            self.owners_df = self.owners_df.append(new_data)
            self.owners_df = self.owners_df.where((pd.notnull(self.owners_df)), None)
        self.save()

    def untag(self, slackid, kenteken):
        self.load()
        self.owners_df.drop([kenteken], inplace=True)
        self.save()

    def lookup(self, kenteken):
        """
        :return: Dict with 'name' and 'slackid' or None is not found
        """
        kenteken = kenteken.strip().replace('-', '').upper()

        assert len(kenteken) == 6, 'Length of the kenteken must be 6 (without any dashes)'
        assert kenteken.isupper(), 'The kenteken must be UPPERCASE'

        self.load()
        if kenteken not in self.owners_df.index:
            log.info('Owner lookup for %s result: not found.', kenteken)
            return None

        res = self.owners_df.loc[kenteken]
        log.info('Owner lookup for %s result: found: %s', kenteken, res.to_dict())
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
