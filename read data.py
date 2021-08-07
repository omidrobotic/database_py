import sqlite3
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(all_results)
