# gsheets-apiv4-postgresql
Small set of scripts for querying a postgresql database and storing the results in google sheets.

## Requirements
* Google API credentials
* Google Sheets enabled for Google API credentials
* Postgresql database

## Setup
* Install dependencies from requirements.txt
* Store credentials in service-account.json
* Configure database, queries and sheets to store results

## Run
Execute the python script export.py or batch_export.py (preferably batch_export.py to minimize API calls).