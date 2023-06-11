import Usuario
from Database import Database
class Empresa(Usuario.Usuario):
    def criaEmpresa(self, cnpj, razao_social, email, telefone, conta, senha, area_negocio):
        values = (cnpj, razao_social, email, telefone, conta, senha, area_negocio)
        tipo = False
        Database.connect(self)
        Database.insert(self, values, tipo)

    # GETTERS
    def getCnpj(self):
        Database.connect(self)
        return Database.select('EMPRESA', 'CNPJ', self.email)
    
    def getRazaoSocial(self):
        Database.connect(self)
        return Database.select('EMPRESA', 'razao_social', self.email)
    
    def getEmail(self):
        Database.connect(self)
        return Database.select('EMPRESA', 'email', self.email)
    
    def getTelefone(self):
        Database.connect(self)
        return Database.select('EMPRESA', 'telefone', self.email)
    
    def getConta(self):
        Database.connect(self)
        return Database.select('EMPRESA', 'conta_bancaria', self.email)
    
    def getSenha(self):
        Database.connect(self)
        return Database.select('EMPRESA', 'senha', self.email)
    
    def getAreaNegocio(self):
        Database.connect(self)
        return Database.select('EMPRESA', 'area_negocio', self.email)
    
    # SETTERS
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
    
    #def pesquisarDesenvolvedores(self):
    #    self.cursor.execute(f'SELECT * FROM desenvolvedor') # Tenta achar o cara com essas credenciais
    #    self.con.commit()
    #    return str(self.cursor.fetchall())
    
    
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