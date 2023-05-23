import sqlite3
class Usuario:
    def __init__(self) -> None:
        self.id = 0
        self.email = 'xxxx@gmail.com'
        self.telefone = '123456789'
        self.agencia = '1234'
        self.conta = '123456'
        self.senha = 'yyyy'
    def criaUsuario(self, id, email, telefone, agencia, conta, login, senha): # O id vai ser necessário no back-end e no BD?
        self.email = email
        self.telefone = telefone
        self.agencia = agencia
        self.conta = conta
        self.login = login
        self.senha = senha
        # Usar lib externa pra colocar esse usuario no BD
    def setEmail(self, email):
        self.email = email
        # Colocar novo email no BD
    def setTelefone(self, telefone):
        self.telefone = telefone
        # Colocar novo telefone no BD
    def setContaBancaria(self, agencia, conta):
        self.agencia = agencia
        self.conta = conta
        # Colocar nova Agência e conta no BD
    def setSenha(self, senha):
        self.senha = senha 
        # Colocar nova senha no BD
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
        # Conversar com Julia em como faremos pra deletar do banco de dados o objeto dessa classe.
        pass
    def iniciaSessao(self, login, senha):
        global sessao_ativa
        conexao = sqlite3.connect('nossoBD.db')
        cursor = conexao.cursor()
        consulta = 'SELECT * FROM desenvolvedor WHERE login = ? AND password = ?'
        cursor.execute(consulta, login, senha)
        if cursor.fetchone():
            conexao.close()
            sessao_ativa = True # Apto para rodar o site do usuário FALAR COM JHONNY
            return True # Logado com sucesso 
            
        else:
            conexao.close()
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
    
        


