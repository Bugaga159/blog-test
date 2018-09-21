import random
class Wms:
  name = '1С:Предприятие'
  version = 1.2
  warehouse = 'Alfa'
  nameDB = 'WMS_new'
  server = '1csrv21B'
  login = 'Oblivion29'
  password = 'Kl12cSk3'
  def logPol(self, log, pas):
    self.login = log
    self.password = pas
  def get_logPol(self):
    return self.login
  def getName(self):
    return self.name

class OpenWms(Wms):
  def logPol(self, log, pas):
    self.login = log
    self.password = pas
    print('Это OpenWms')
  def get_logPol(self):
    descr = [self.name, self.nameDB ]
    return descr
class Admin(Wms):  
  position = 'Wms operator'
  level = 'C2'
  def logPol(self, log, pas):
    self.login = log
    self.password = pas
    print('Это Admin')
  def get_logPol(self):
    pos = [self.position, self.level ]
    return pos

Andrey = []
b = [OpenWms(), Admin()]
for i in range(1,11):
  n = random.randint(0,1)
  Andrey.append(b[n])
for add in Andrey:
  add.logPol('Andrey', 'bfg2H2')

