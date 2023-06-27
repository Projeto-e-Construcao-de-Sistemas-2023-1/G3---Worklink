from Database import Database
from Desenvolvedor import Desenvolvedor
from Empresa import Empresa

class Evento():
    def criaEventoDev(self, inicio, fim, texto, cor, fundo, id_dev, tipo):
        Database.connect(self)
        values = (inicio, fim, texto, cor, fundo, id_dev)
        Database.insertEvent(self, values, tipo)

    def criaEventoEmp(self, inicio, fim, texto, cor, fundo, id_emp, tipo):
        Database.connect(self)
        values = (inicio, fim, texto, cor, fundo, id_emp)
        Database.insertEvent(self, values, tipo)

    def atualizaEvento(self,inicio, fim, texto, cor, fundo, id):
        Database.connect(self)
        values = (inicio, fim, texto, cor, fundo, id)
        Database.updateEvent(self, values, id)

    def deletaEvento(self, id):
        Database.connect(self)
        Database.deleteEvent(self, id)

    def getEvento(self, month, year, id_user, tipo):
        Database.connect(self)
        Database.getEvent(self, month, year, id_user, tipo)
