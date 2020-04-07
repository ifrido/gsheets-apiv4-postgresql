from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'service-account.json'


def service():
    """Authenticates and returns Google Sheets API v4
    """
    service = None

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=creds)

    return service


def update(spreadsheet=None, id=None, range=None, body=None, value_input_option='USER_ENTERED'):
    request = spreadsheet.values().update(spreadsheetId=id, range=range, valueInputOption=value_input_option, body=body)
    response = request.execute()
    return response


def clear(spreadsheet=None, id=None, range=None):
    request = spreadsheet.values().clear(spreadsheetId=id, range=range)
    response = request.execute()
    return response


def batch_update(spreadsheet=None, id=None, data=None, value_input_option='USER_ENTERED'):
    body = {
        "valueInputOption": value_input_option,
        "data": data
    }
    request = spreadsheet.values().batchUpdate(spreadsheetId=id, body=body)
    response = request.execute()
    return response


def batch_clear(spreadsheet=None, id=None, ranges=None):
    body = {
        'ranges': ranges
    }
    request = spreadsheet.values().batchClear(spreadsheetId=id, body=body)
    response = request.execute()
    return response
