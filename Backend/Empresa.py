import Usuario
from Database import Database
class Empresa(Usuario.Usuario):
    def criaEmpresa(self, cnpj, razao_social, email, telefone, conta, senha, area_negocio):
        values = (cnpj, razao_social, email, telefone, conta, senha, area_negocio)
        tipo = False
        Database.connect(self)
        Database.insert(self, values, tipo)
    def setCnpj(self, cnpj, email):
        Database.connect(self)
        Database.update(self, 'CNPJ', cnpj, 'EMPRESA', email)
    def setRazaoSocial(self, razao_social, email):
        Database.connect(self)
        Database.update(self, 'razao_social', razao_social, 'EMPRESA', email)
    def setEmail(self, email_novo, email):
        Database.connect(self)
        Database.update(self, 'email', email_novo, 'EMPRESA', email)
    def setTelefone(self, telefone, email):
        Database.connect(self)
        Database.update(self, 'telefone', telefone, 'EMPRESA', email)
    def setConta(self, conta, email):
        Database.connect(self)
        Database.update(self, 'conta_bancaria', conta, 'EMPRESA', email)
    def setSenha(self, senha, email):
        Database.connect(self)
        Database.update(self, 'senha', senha, 'EMPRESA', email)
    def setAreaNegocio(self, area_negocio, email):
        Database.connect(self)
        Database.update(self, 'area_negocio', area_negocio, 'EMPRESA', email)
    def getRazaoSocial(self):
        self.cursor.execute(f'SELECT razao_social FROM empresa WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    def getCnpj(self):
        self.cursor.execute(f'SELECT CNPJ FROM empresa WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    def getAreaNegocio(self):
        self.cursor.execute(f'SELECT area_negocio FROM empresa WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    
    
    
    #def setRazaoSocial(self, razao_social):
        #SELECT RAZAO_SOC FROM EMPRESA WHERE EMAIL = XXXX -- UPDATE
    #    pass
    #def publicarProjeto(self, projeto):
    #    self.projetos.append(projeto)
    
    #def visualizarProjetos(self, status):
    #    for projeto in self.projetos:
    #        if projeto.status == status:
    #            print(projeto)
    
    #def seguirDesenvolvedor(self, desenvolvedor):
    #    self.desenvolvedores_seguidos.append(desenvolvedor)
    
    def pesquisarDesenvolvedores(self):
        self.cursor.execute(f'SELECT * FROM desenvolvedor') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    
    
    #def inserirDinheiroCarteira(self, valor):
    #    self.saldo_carteira += valor
    
    #def realizarPagamento(self, desenvolvedor, valor):
    #    self.saldo_carteira -= valor
    #    desenvolvedor.saldo_carteira += valor
    
    #def marcarReuniao(self, desenvolvedor, data, hora):
    #    reuniao = Reuniao(desenvolvedor, data, hora) # Usar integração com Calendar
    #    self.reunioes_agendadas.append(reuniao)

    #def avaliarDesenvolvedor(self, desenvolvedor, avaliacao):
    #    desenvolvedor.avaliacoes.append(avaliacao)

    #def listarProjetosEmAndamento(self):
    #    for projeto in self.projetos:
    #        if projeto.status == "Em andamento":
    #            print(projeto)

    #def listarProjetosConcluidos(self):
    #    for projeto in self.projetos:
    #        if projeto.status == "Concluído":
    #            print(projeto)

    #def exibirInformacoes(self):
    #    print("Razão Social:", self.razao_social)
    #    print("Email:", self.email)
    #    print("Telefone:", self.telefone)
