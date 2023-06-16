from Database import Database
import pyperclip
class Usuario: # CLASSE QUE TERÁ OS METODOS COMUNS A DESENVOLVEDOR E EMPRESA
    def deletaUsuario(self, email, tipo): # Passar tipo = True para DESENVOLVEDOR | tipo = False para EMPRESA
        Database.connect(self)
        if tipo == True:
            Database.delete(self, 'DESENVOLVEDOR', email)
        else:
            Database.delete('EMPRESA', email)
            
    def iniciaSessao(self, email, senha):
        Database.connect(self)
        if Database.autenticaUsuario(self, email, senha):
            self.email = email # Grava email do usuario logado para futuras consultas
            return True # vai vir como True ou False
        else:
            return False
        
    def finalizaSessao(self):
        pass # Apenas no front end

    def verificaUsuario(self, email):
        Database.connect(self)
        return Database.verificaUsuario(self, email)
    
    def toClipboard(self, texto):
        pyperclip.copy(texto)
    
    def pesquisaUsuario(self, nome):
        Database.connect(self)
        return Database.pesquisaUsuario(self, nome)