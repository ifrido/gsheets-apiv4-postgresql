import yaml

CONFIG_FILE = "config-sample.yml"
SERVICE_ACCOUNT_FILE = 'service-account-sample.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
DATABASE_SECTION = 'default'

with open(CONFIG_FILE, "r") as configfile:
    config = yaml.load(configfile, Loader=yaml.FullLoader)