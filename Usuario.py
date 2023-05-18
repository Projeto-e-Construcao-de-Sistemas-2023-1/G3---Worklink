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
    def setTelefone(self, telefone):
        self.telefone = telefone
    def setContaBancaria(self, agencia, conta):
        self.agencia = agencia
        self.conta = conta
    def setSenha(self, senha):
        self.senha = senha
    def editaUsuario(self, mudança):
        # perguntar ao usuario o que ele quer editar -> ver com pessoal do frontend
        mudança = mudança.lower()
        if(mudança == 'email'):
            # pedir o novo email
            novo_email = input(print('Digite o novo email: '))
            self.setEmail(novo_email)
        elif(mudança == 'telefone'):
            # pedir o novo telefone
            novo_telefone = input(print('Digite o novo telefone: '))
            self.setTelefone(novo_telefone)
        elif(mudança == 'conta bancaria'):
            # pedir a nova conta bancaria
            novo_agencia = input(print('Digite a nova agencia: '))
            novo_conta = input(print('Digite a nova conta: '))
            self.setContaBancaria(novo_agencia, novo_conta)
        elif(mudança == 'senha'):
            # pedir a nova senha
            novo_senha = input(print('Digite a nova senha: '))
            self.setSenha(novo_senha)
        elif(mudança == 0):
            exit()
        else:
            self.editaUsuario()
    def deletaUsuario(self):
        # Conversar com Julia em como faremos pra deletar do banco de dados o objeto dessa classe.
        pass
        
    
    
        


