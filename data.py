import configDataBase as config

def findInSetData(name):
    config.setCur.execute("SELECT * FROM omid WHERE NAME=?", (name,))
    return config.setCur.fetchone()[2]

def findInReadData(name):
    config.readCur.execute("SELECT * FROM refree WHERE NAME=?", (name,))
    return config.readCur.fetchall()
    
def clearSetData(userID):
    config.setCur.execute('DELETE FROM omid WHERE ID=?', (userID,))
    config.setData.commit()

def clearReadData(userID):
    config.readCur.execute('DELETE FROM refree WHERE ID=?', (userID,))
    config.readData.commit()

def updateDataBase(name,equl):
    setValue=(equl,name)
    config.setCur.execute("UPDATE omid set EQUL = ? where NAME=?", setValue)
    config.setData.commit()
    
def setDataValue(userID,name,equl):
    setValue=(userID,name,equl)
    config.setCur.execute("INSERT INTO omid VALUES(?, ?, ?);", setValue)
    config.setData.commit()

def readDataValue(userID,name,equl,xpos,ypos):
    readValue=(userID,name,equl,xpos,ypos)
    config.readCur.execute("INSERT INTO refree VALUES(?, ?, ?, ?, ?);", readValue)
    config.readData.commit()

class seter:
    id = 1
    name = 'hello'
    equl = 0

class reader:
    id = 1
    name = 'hello'
    equl = 0
    xpos = 0
    ypos = 0





