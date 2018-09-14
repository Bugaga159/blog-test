class Wms:
  def __init__(self,n, v, w ):
    self.name = n
    self.version = v
    self.warehouse = w
  
  __nameDB = 'WMS_new'
  __server = '1csrv21B'
  __login = 'Oblivion29'
  __password = 'aLsd223L'
  
  def newDB(self, db):
    self.__nameDB = db
  def get_newDB(self):
    return self.__nameDB  
  
  def newPerson(self, l, p):
    self.__login = l
    self.__password = p
  def get_newPerson(self):
    per = [self.__login, self.__password]
    return per
  
class Admin:
  def __init__(self, l, p):
    self.login = l
    self.password = p
  
  __position = 'wms operator'
  __level = 'B2'
  __warehouse = 'Alfa'


  def newPosition(self, pos, l, w):
    self.__position = pos
    self.__level = l
    self.__warehouse = w

sap = Wms('SAP', 2.0, 'K&B')
Andrey = Admin('Andrey29', 'Jkd2sj8HN')
print('Добро пожаловать в систему',sap.name, ', версия -', sap.version)
print('Пользователь', Andrey.login,', добро пожаловать!')

####################################### LESSON 4
class Wms:  
  __name = '1C:Предприятие'
  __version = 1.2
  __warehouse = "Alfa"  
  __nameDB = 'WMS_new'
  __server = '1csrv21B'
  __login = 'Oblivion29'
  __password = 'aLsd223L'
  def logPol(self, log, pas):
    self.__login = log
    self.__password = pas
  def get_logPol(self):
    return self.__login
  
class OpenWms(Wms):
  def __init__(self,n, v, w ):
    self.__name = n
    self.__version = v
    self.__warehouse = w

  def get_sys(self):
    b = [self.__name, self.__version, self.__warehouse]
    return b  
  
class Admin(Wms):
  __position = 'wms operator'
  __level = 'B2'
  
  def get_log(self):
    return self.__login

  def newPosit(self, p, l):
    self.__position = p
    self.__level = l
  def get_newPosit(self):
    pos = [self.__login, self.__position, self.__level]
    return pos

sap = OpenWms('SAP', 2.0, 'K&B')
newAdmin = Admin()
Andrey =[sap, newAdmin]
for add in Andrey:
  add.logPol('Andrey', 'hch2Jbg1')
print('Добро пожаловать', sap.get_logPol(),', нам Вас не хватало!')





