import sqlite3

# create a connection to the database
conn = sqlite3.connect('users.db')

# create the recipes table with the correct schema
conn.execute('''DROP TABLE IF EXISTS recipes;''')
conn.execute('''CREATE TABLE users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 email TEXT NOT NULL,
                 name TEXT NOT NULL,
                 username TEXT NOT NULL UNIQUE,
                 password TEXT NOT NULL
               );''')