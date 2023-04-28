import sqlite3

# create a connection to the database
conn = sqlite3.connect('recipes.db')

# create the recipes table with the correct schema
conn.execute('''DROP TABLE IF EXISTS recipes;''')
conn.execute('''CREATE TABLE recipes (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT NOT NULL,
                 cuisine TEXT NOT NULL,
                 ingredients TEXT NOT NULL,
                 instructions TEXT NOT NULL,
                 cookingtime INTEGER
               );''')
