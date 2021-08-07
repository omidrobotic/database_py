import configDataBase as config

def findInSetData(name):
    config.setCur.execute("SELECT * FROM omid WHERE name=?", (name,))
    return config.setCur.fetchall()

def findInReadData(name):
    config.readCur.execute("SELECT * FROM refree WHERE name=?", (name,))
    return cconfig.readCur.fetchall()
    
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
    readValue=('1','refree','2.2','2','2')
    config.readCur.execute("INSERT INTO refree VALUES(?, ?, ?, ?, ?);", readValue)
    config.readData.commit()

class seterClass:
    id = 1
    name = 'hello'
    equl = 0

class readerClass:
    id = 1
    name = 'hello'
    equl = 0
    xpos = 0
    ypos = 0

seter = seterClass()
seter.id=10
seter.name='ali'
seter.equl=10

clearSetData(seter.id)
setDataValue(seter.id,seter.name,seter.equl)

print(findInSetData('ali'))



