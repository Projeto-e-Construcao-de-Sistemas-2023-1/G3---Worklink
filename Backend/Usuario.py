from Database import Database
import pyperclip
class Usuario: # CLASSE QUE TERÁ OS METODOS COMUNS A DESENVOLVEDOR E EMPRESA
    def deletaUsuario(self): # Passar tipo = True para DESENVOLVEDOR | tipo = False para EMPRESA
        Database.connect(self)
        if self.tipo == True:
            Database.delete(self, 'DESENVOLVEDOR', self.email)
        else:
            Database.delete('EMPRESA', self.email)
            
    def iniciaSessao(self, email, senha):
        Database.connect(self)
        if Database.autenticaUsuario(self, email, senha):
            self.email = email # Grava email do usuario logado para futuras consultas
            return True # vai vir como True ou False
        else:
            return False
        
    def finalizaSessao(self):
        pass # Apenas no front end

    def verificaUsuario(self):
        Database.connect(self)
        self.tipo = Database.verificaUsuario(self, self.email)
        return self.tipo
    
    def toClipboard(self, texto):
        pyperclip.copy(texto)
    
    def capturaEmail(self, email):
        self.email = email

    def pesquisaUsuario(self, nome, tipo):
        Database.connect(self)
        return Database.pesquisaUsuario(self, nome, tipo)
    
    def Follow(self, seguidor, seguido, tipoSeguidor, tipoSeguido):
        Database.connect(self)
        if self.verificaUsuario(self):
            tipo = 'dev'
        tipo = 'emp'
        if verificaUsuario(cod):
            tipoSeguido = 'dev'
        tipoSeguido = 'emp'
        if Database.checkFollow(self, self.cod, codSgd, tipoSgr, tipoSgd):
            return False  
            #Ja segue
        else:
            Database.Follow(self, self.cod, codSgd, tipoSgr, tipoSgd)
            return True 
            #começou a seguir

    def Unfollow(self, cod, tipo):
        Database.connect(self)
        if self.verificaUsuario(self):
            tipo = 'dev'
        tipo = 'emp'
        if verificaUsuario(cod):
            tipoSeguido = 'dev'
        tipoSeguido = 'emp'
        if Database.checkFollow(self, self.cod, cod, tipo, tipoSeguido):
            Database.Unfollow(self, self.cod, cod)
            return True  
            #deu unfollow
        else:
            return False
            #nao estava seguindo