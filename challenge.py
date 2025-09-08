import sqlite3

db = sqlite3.connect("contacts.sqlite")
cursor = db.cursor()
zapytanie = "SELECT * FROM contacts WHERE name = ?"
user_input = input("Who you want to check? ")
cursor.execute(zapytanie, (user_input,))
print(cursor.fetchall())

db.close()
