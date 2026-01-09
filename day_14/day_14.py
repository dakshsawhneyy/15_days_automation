import sqlite3
import subprocess
import datetime
from datetime import date
import os

# conn = sqlite3.connect("metrics.db")    # create file if not xists
# cursor = conn.cursor()

# disc_usage_output = subprocess.run(["df", "-h", "/"], text=True, capture_output=True)
# disc_usage_out = disc_usage_output.stdout.splitlines()[1]
# disc_usage = disc_usage_out.split()[4].strip("%")

# cursor.execute("CREATE TABLE IF NOT EXISTS disc_usage (date TEXT, percent INTEGER)")
# cursor.execute(f"INSERT INTO disc_usage VALUES (?, ?)", (datetime.datetime.now().isoformat(), disc_usage))
# print(f"disc usage: {disc_usage} inserted in metrics.db")

# # Fetching all data
# cursor.execute("SELECT * FROM disc_usage")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# conn.commit()
# conn.close()


# ! Ticket 2 -- Log Rotation
log_file = "./app.log"
# Log Rotation
if os.path.exists(log_file):
    os.rename(log_file, f"app_{date.today()}.log")
    print("logfile rotated successfully")
    
# Create new app.log
open("app.log", "w").close()    # creating empty file