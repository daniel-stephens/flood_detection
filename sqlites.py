import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        c = conn.cursor()
        c.execute(""" CREATE TABLE vid_pixils (id INTEGER PRIMARY KEY, frame_number int NOT NULL, num int NOT NULL) """)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(".\\pixils.db")