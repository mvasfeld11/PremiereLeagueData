import sqlite3

print('hello')

try:
    sqliteConnection = sqlite3.connect('prem.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")