import sqlite3


setData = sqlite3.connect('config.db')
setCur = setData.cursor()
setCur.execute("""CREATE TABLE IF NOT EXISTS omid(
    ID INT PRIMARY KEY,
    NAME TEXT,
    EQUL REAL);
""")

setData.commit()


readData = sqlite3.connect('readData.db')
readCur = setData.cursor()
readCur.execute("""CREATE TABLE IF NOT EXISTS refree(
    ID INT PRIMARY KEY,
    NAME TEXT,
    EQUL REAL,
    xpos INT,
    ypos INT);
""")
readData.commit()
