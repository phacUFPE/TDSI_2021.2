import sqlite3

from backend.utils.constants import DatabaseConstants


def init_db():
    print('Creating database...')
    connection = sqlite3.connect(f'{DatabaseConstants.NAME}.db')

    with open(f'{DatabaseConstants.SCHEMA_NAME}.sql') as file:
        connection.executescript(file.read())

    connection.close()
    print('Database created.')
