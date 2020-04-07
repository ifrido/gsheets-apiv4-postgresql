from config import config
import api
import database
import json


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    # The ID and range of a sample spreadsheet.
    spreadsheet_id = config['spreadsheet']['id']

    service = api.service()
    conn = database.connection()
    cursor = conn.cursor()

    # Call the Sheets API
    spreadsheet = service.spreadsheets()

    ranges = []
    value_ranges = []

    for sheet in config['spreadsheet']['sheets']:
        query = config['spreadsheet']['sheets'][sheet]['query']
        range = config['spreadsheet']['sheets'][sheet]['name'] + '!' + config['spreadsheet']['sheets'][sheet]['range']
        ranges.append(range)

        cursor.execute(query)
        cols = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        values = [cols]
        for row in rows:
            values.append(list(row))

        update_range = range + str(len(values))

        value_range = {
            'range': update_range,
            'values': values
        }

        value_ranges.append(value_range)

    response_cleared = api.batch_clear(spreadsheet=spreadsheet, id=spreadsheet_id, ranges=ranges)
    response_update = api.batch_update(spreadsheet=spreadsheet, id=spreadsheet_id, data=value_ranges)

    print(json.dumps(response_cleared, indent=2))
    print(json.dumps(response_update, indent=2))

    if conn is not None:
        conn.close()


if __name__ == '__main__':
    main()
