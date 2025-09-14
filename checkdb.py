import sqlite3


db = sqlite3.connect("accounts.sqlite")

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
#                       " history.account, history.amount FROM history ORDER BY history.time"):
for row in db.execute("SELECT * FROM localhistory"):
    print(row)

db.close()
