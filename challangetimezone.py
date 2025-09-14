import sqlite3
import datetime


db = sqlite3.connect("accounts.sqlite")

def _local_time_zone():
    local_utc = str(datetime.datetime.now().astimezone())
    return local_utc[-6:]

current_timelocal = _local_time_zone()

print(current_timelocal)




db.close()
