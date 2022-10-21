import os

import yaml


class Configuration:

    def __init__(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        config_file = script_dir + '/config.yaml'
        with (open(config_file)) as f:
            self.config = yaml.safe_load(f)

    def get_isbngenerator_configuration(self, name):
        return self.config['isbngenerator'][name]
