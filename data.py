import configDataBase as config

def findInSetData(name):
    config.setCur.execute("SELECT * FROM omid WHERE name=?", (name,))
    return config.setCur.fetchall()

def findInReadData(name):
    config.readCur.execute("SELECT * FROM refree WHERE name=?", (name,))
    return config.readCur.fetchall()
    
def clearSetData(userID):
    config.setCur.execute('DELETE FROM omid WHERE userid=?', (userID,))
    config.setData.commit()

def clearReadData(userID):
    config.readCur.execute('DELETE FROM refree WHERE userid=?', (userID,))
    config.readData.commit()

    
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





