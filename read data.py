import sqlite3
conn = sqlite3.connect('omiddatabase.db')
cur = conn.cursor()
cur.execute("SELECT * FROM omid;")
all_results = cur.fetchall()
print(all_results)
