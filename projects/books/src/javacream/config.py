import yaml
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
def read_yaml_file():
    with open(dir_path + '/config.yaml', "r") as f:
        return yaml.safe_load(f)

def get_logging_config(name):
    configuration = read_yaml_file()
    return configuration['logging'][name]

print (get_logging_config("log_level"))