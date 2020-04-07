from config import config
import api
import database


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

    for sheet in config['spreadsheet']['sheets']:
        query = config['spreadsheet']['sheets'][sheet]['query']
        range = config['spreadsheet']['sheets'][sheet]['name'] + '!' + config['spreadsheet']['sheets'][sheet]['range']

        cursor.execute(query)
        cols = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        values = [cols]
        for row in rows:
            values.append(list(row))

        update_range = range + str(len(values))

        response_cleared = api.clear(spreadsheet=spreadsheet, id=spreadsheet_id,
                                     range=range)

        body = {
            'range': update_range,
            'values': values
        }

        response_update = api.update(spreadsheet=spreadsheet, id=spreadsheet_id,
                                     range=update_range,
                                     body=body)

    if conn is not None:
        conn.close()


if __name__ == '__main__':
    main()
