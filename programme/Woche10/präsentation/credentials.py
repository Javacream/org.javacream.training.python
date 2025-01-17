import keyring

def get_password(configuration):
    return keyring.get_password(configuration['system'], configuration['username'])