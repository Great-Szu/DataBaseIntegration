import sqlite3
import datetime

db = sqlite3.connect("accounts.sqlite")

for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    local_time = datetime.datetime.now().isoformat()
    print("{}\t{}".format(utc_time, local_time))
db.close()
