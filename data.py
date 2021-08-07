import sqlite3
conn = sqlite3.connect('omiddatabase.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS omid(
   userid INT PRIMARY KEY,
   name TEXT,
   equl REAL);
""")
conn.commit()
user=('1','refree','2.2')
cur.execute("INSERT INTO omid VALUES(?, ?, ?);", user)
conn.commit()
