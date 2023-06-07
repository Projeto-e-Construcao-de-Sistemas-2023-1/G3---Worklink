<<<<<<<< HEAD:Backend/Usuario.py
from Database import Database
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
========
import sqlite3
class Usuario:    
    def criaUsuario(self, email, telefone, agencia, conta, login, senha): # O id vai ser necessário no back-end e no BD?
        print('usuario criado com sucesso!')
        pass
        # Fazer os inserts no BD
    def setEmail(self, email):
        # Colocar novo email no BD -- UPDATE
        pass
    def setTelefone(self, telefone):
        # Colocar novo telefone no BD -- UPDATE
        pass
    def setContaBancaria(self, agencia, conta):
        # Colocar nova Agência e conta no BD -- UPDATE
        pass
    def setSenha(self, senha):
        # Colocar nova senha no BD -- UPDATE
        pass
>>>>>>>> origin/julia:Usuario.py
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
<<<<<<<< HEAD:Backend/Usuario.py
    def deletaUsuario(self, email):
        try:
            self.cursor.execute(f'DELETE FROM usuario WHERE email = {email}')
            self.con.commit() 
            return True # PRINTAR NA TELA QUE O USUARIO FOI DELETADO COM SUCESSO
        except Exception as e:
            print(e)
            return False # PRINTAR ERRO NA DELEÇÃO    
    def iniciaSessao(self, email, senha):
========
    def deletaUsuario(self):
        # Deletar usuário do BD.
        pass
    def iniciaSessao(self, login, senha):
>>>>>>>> origin/julia:Usuario.py
        global sessao_ativa
        consulta = 'SELECT * FROM desenvolvedor WHERE login = ? AND password = ?'
        self.cursor.execute(consulta, login, senha)
        if self.cursor.fetchone():
            self.conexao.close()
            sessao_ativa = True # Apto para rodar o site do usuário FALAR COM JHONNY
            return True # Logado com sucesso 
            
        else:
            self.conexao.close()
            sessao_ativa = False
            return False # Credenciais inválidas  
    def finalizaSessao(self):
        global sessao_ativa # Só rodar o site do usuário se a sessão estiver ativa FALAR COM JHONNY
        sessao_ativa = False
<<<<<<<< HEAD:Backend/Usuario.py
    def pesquisaUsuario(self):
        self.cursor.execute(f'SELECT * FROM desenvolvedor JOIN empresa')
        self.con.commit()
        return str(self.cursor.fetchall()) # MOSTRAR OS REGISTROS NA TELA DO FRONT END
========

    def pesquisaUsuario(self, nome):
        conexao = sqlite3.connect('nossoBD.db')
        cursor = conexao.cursor()
        consulta = 'SELECT * FROM usuario WHERE nome = ?'
        cursor.execute(consulta, nome)
        resultado = cursor.fetchall()
        return resultado
        # MOSTRAR OS REGISTROS NA TELA DO FRONT END
    def conectaBD(self):
        self.conexao = sqlite3.connect('banco-de-dados.sql')
        self.cursor = self.conexao.cursor()
        


>>>>>>>> origin/julia:Usuario.py
