import sqlite3


setData = sqlite3.connect('setData.db')
setCur = setData.cursor()
setCur.execute("""CREATE TABLE IF NOT EXISTS omid(
    userid INT PRIMARY KEY,
    name TEXT,
    equl REAL);
""")

setData.commit()


readData = sqlite3.connect('readData.db')
readCur = setData.cursor()
readCur.execute("""CREATE TABLE IF NOT EXISTS refree(
    userid INT PRIMARY KEY,
    name TEXT,
    equl REAL,
    xpos INT,
    ypos INT);
""")
readData.commit()
