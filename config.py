import yaml

with open("config.yml", "r") as configfile:
    config = yaml.load(configfile, Loader=yaml.FullLoader)