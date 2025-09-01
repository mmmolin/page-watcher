import yaml

def validate_config(config):
    required_properties = ['url', 'to_email', 'from_email', 'smtp_server', 'smtp_port']
    for rp in required_properties:
        if rp not in config:
            return False
    return True


def read_config():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        isValid = validate_config(config)
        if isValid is False:
            raise KeyError('Missing key in config.yaml')
        return config