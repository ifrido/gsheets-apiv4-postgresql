from config import config, DATABASE_SECTION
import psycopg2


def connection():
    conn = None
    host = config['databases'][DATABASE_SECTION]['host']
    port = config['databases'][DATABASE_SECTION]['port']
    database = config['databases'][DATABASE_SECTION]['database']
    user = config['databases'][DATABASE_SECTION]['user']
    password = config['databases'][DATABASE_SECTION]['password']
    sslmode = config['databases'][DATABASE_SECTION]['sslmode']

    conn = psycopg2.connect(dbname=database, user=user, password=password, host=host, port=port, sslmode=sslmode)

    return conn


def query():
    return None
