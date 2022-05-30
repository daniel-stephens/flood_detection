import sqlite3

try:

    con = sqlite3.connect('pixils.db')

    cur = con.cursor()
    print("Successfully Connected to SQlite")

    cur.execute("SELECT * FROM vid_pixils")

    rows = cur.fetchall()

    for row in rows:
        print(row)


except con.Error as error:
    print("Error while executing sqlite script", error)


# Create table
# cur.execute('''CREATE TABLE vid_pixils
#                (pixil_number, pixils)''')


finally:
    if con:
        con.close()