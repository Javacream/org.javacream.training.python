import os

import yaml


class Configuration:

    def __init__(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        config_file = script_dir + '/config.yaml'
        with (open(config_file)) as f:
            self.config = yaml.safe_load(f)

    def get_isbngenerator_configuration(self):
        return self.config['isbngenerator']
    def get_database_configuration(self):
        return self.config['database']
    def get_configuration(self, config_name):
        return self.config[config_name]
