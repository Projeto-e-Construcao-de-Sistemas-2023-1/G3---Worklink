from Database import Database
class Usuario: # CLASSE QUE TERÁ OS METODOS COMUNS A DESENVOLVEDOR E EMPRESA
    def deletaUsuario(self, email, tipo): # Passar tipo = True para DESENVOLVEDOR | tipo = False para EMPRESA
        Database.connect(self)
        if tipo == True:
            Database.delete(self, 'DESENVOLVEDOR', email)
        else:
            Database.delete('EMPRESA', email)
    def iniciaSessao(self, email, senha):
        Database.connect(self)
        if Database.autenticarUsuario(email, senha) == True:
            self.email = email # Grava email do usuario logado para futuras consultas
            return Database.autenticaUsuario(email, senha) # vai vir como True ou False
        else:
            return Database.autenticaUsuario(email, senha)
    def finalizaSessao(self):
        pass # Apenas no front end
    def pesquisaUsuario(self, nome):
        Database.connect()
        return Database.pesquisaUsuario(nome)