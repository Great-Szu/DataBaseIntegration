import sqlite3

db = sqlite3.connect("contacts.sqlite")
cursor = db.cursor()
for row in cursor.execute("SELECT * FROM sqlite_master"):
    print(row)

db.close()
