# gsheets-apiv4-postgresql
Small set of scripts for querying a postgresql database and storing the results in google sheets.

## Requirements
1. Google API credentials, obtain from [Google API Console](https://console.developers.google.com/apis/credentials)
    * Create new project if you don't already have one
    * Create service account for project, if you don't already have one and download `service-account.json`
1. Google Sheets enabled for Google API credentials, enable in [Google API Library](https://console.developers.google.com/apis/library/sheets.googleapis.com)
1. Postgresql database, should be reachable from where your script is running. Make sure you don't expose it in public.

Now you are ready to set configuration parameters for the script.

## Setup
1. Install dependencies from requirements.txt with `pip install -r requirements.txt`
1. Place your credentials file you downloaded before and define it in `config.py` with the variable `SERVICE_ACCOUNT_FILE`
1. Configure database, queries and sheets to store results as in `config-sample.yml`, define the file in `config.py` with the variable `CONFIG_FILE`

The script will loop through the different `sheets` sections in `spreadsheet`  defined in the `CONFIG_FILE`.
* For every sheet the defined range will be cleared (delete all data from the cells).
* Then the range will be filled with the columns and rows from the SQL query

This ensures that all data from the table in the database is properly copied to the sheet.

## Run
There are two scripts which can be executed (you will preferably use `batch_export.py` to minimize API calls):
### export.py
Runs every request sequentially, two per sheet (one to clear and one to update the range).
Which will result in `2n` API calls where `n` is the number of sheets configured.

Run with: `python export.py`

### batch_export.py
Executes two requests, bundles all the clear requests in the first API call and all the update requests in the second one API.

Run with: `python batch_export.py`