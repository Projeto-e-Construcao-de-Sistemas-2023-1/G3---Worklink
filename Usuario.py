import sqlite3
import mysql.connector


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
    def deletaUsuario(self):
        # Deletar usuário do BD.
        pass
    def iniciaSessao(self, login, senha):
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

    def pesquisaUsuario(self, nome):
        conexao = sqlite3.connect('nossoBD.db')
        cursor = conexao.cursor()
        consulta = 'SELECT * FROM usuario WHERE nome = ?'
        cursor.execute(consulta, nome)
        resultado = cursor.fetchall()
        return resultado
        # MOSTRAR OS REGISTROS NA TELA DO FRONT END
    def conectaBD(self):
        con = mysql.connector.connect(
        host='localhost',
        database='worklink',
        user='root',
        password='pjSq2023@')

        if con.is_connected():
            db_info = con.get_server_info()
            print("conectado ao servidor MYSQL versão", db_info)
            cursor = con.cursor()
            comando = 'SELECT * FROM usuario'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)
            
            cursor.close()
            con.close()


