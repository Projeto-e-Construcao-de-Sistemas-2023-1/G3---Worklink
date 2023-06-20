from Database import Database
<<<<<<< HEAD
class Usuario:
    def getEmail(self):
        return str(self.email)
    def getConta(self):
        self.cursor.execute(f'SELECT conta_bancaria FROM empresa WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    def setTelefone(self, telefone):
        self.cursor.execute(f'UPDATE desenvolvedor SET telefone = {telefone} WHERE email = "{self.email}"')
        self.con.commit()
        return True
    def setContaBancaria(self, conta):
        self.cursor.execute(f'UPDATE desenvolvedor SET conta_bancaria = {conta} WHERE email = "{self.email}"')
        self.con.commit()
        return True
    def setSenha(self, senha):
        self.cursor.execute(f'UPDATE desenvolvedor SET senha = {senha} WHERE email = "{self.email}"')
        self.con.commit()
        return True
    def getTelefone(self):
        self.cursor.execute(f'SELECT telefone FROM empresa JOIN desenvolvedor WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    def editaUsuario(self, mudança):
        # perguntar ao usuario o que ele quer editar -> ver com pessoal do frontend
        mudança = mudança.lower()
        if(mudança == 'email'):
            # pedir o novo email
            self.setEmail(novo_email) # RECEBER DO FRONT END
        elif(mudança == 'telefone'):
            # pedir o novo telefone
            self.setTelefone(novo_telefone) # RECEBER DO FRONT END
        elif(mudança == 'conta bancaria'):
            # pedir a nova conta bancaria
            self.setContaBancaria(novo_agencia, novo_conta) # RECEBER DO FRONT END
        elif(mudança == 'senha'):
            # pedir a nova senha
            self.setSenha(novo_senha) # RECEBER DO FRONT END
        elif(mudança == 0):
            exit()
        else:
            self.editaUsuario()
    def deletaUsuario(self, email):
        try:
            self.cursor.execute(f'DELETE FROM usuario WHERE email = {email}')
            self.con.commit() 
            return True # PRINTAR NA TELA QUE O USUARIO FOI DELETADO COM SUCESSO
        except Exception as e:
            print(e)
            return False # PRINTAR ERRO NA DELEÇÃO    
    def iniciaSessao(self, email, senha):
        global sessao_ativa
        self.email = email # Grava email do usuario logado para futuras consultas
        self.cursor.execute(f'SELECT * FROM desenvolvedor JOIN empresa WHERE email = {email} AND senha = {senha}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        if self.cursor.fetchone():
            sessao_ativa = True # Apto para rodar o site do usuário FALAR COM JHONNY
            return True # Logado com sucesso 
        else:
            sessao_ativa = False
            return False # Credenciais inválidas  
    def finalizaSessao(self):
        global sessao_ativa # Só rodar o site do usuário se a sessão estiver ativa FALAR COM JHONNY
        sessao_ativa = False
    def pesquisaUsuario(self):
        self.cursor.execute(f'SELECT * FROM desenvolvedor JOIN empresa')
        self.con.commit()
        return str(self.cursor.fetchall()) # MOSTRAR OS REGISTROS NA TELA DO FRONT END
=======
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
    
    def searchUsuario(self, pesquisa_user):
        Database.connect(self)
        return Database.verificaUsuarioNome(self, pesquisa_user)
        
    def sessao(self, email):
        Database.connect(self)
        return (email)
>>>>>>> 65ac48e8794cd093ab268ffb8c08e14f7e2f1252
