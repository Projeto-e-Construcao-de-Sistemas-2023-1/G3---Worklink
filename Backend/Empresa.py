import Usuario
from Database import Database
class Empresa(Usuario.Usuario):
    def criaEmpresa(self, cnpj, razao_social, email, telefone, conta, senha, area_negocio):
        values = (cnpj, razao_social, email, telefone, conta, senha, area_negocio)
        tipo = False
        Database.connect(self)
        Database.insert(self, values, tipo)

    # GETTERS
    def getCnpj(self, email):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'CNPJ', email)
    
    def getRazaoSocial(self, email):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'razao_social', email)
    
    def getEmail(self, email):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'email', email)
    
    def getTelefone(self, email):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'telefone', email)
    
    def getConta(self, email):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'conta_bancaria', email)
    
    def getSenha(self, email):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'senha', email)
    
    def getAreaNegocio(self, email):
        Database.connect(self)
        return Database.select(self, 'EMPRESA', 'area_negocio', email)
    
    # SETTERS
    def setCnpj(self, cnpj, email):
        Database.connect(self)
        Database.update(self, 'CNPJ', cnpj, 'EMPRESA', email)
        return True

    def setRazaoSocial(self, razao_social, email):
        Database.connect(self)
        Database.update(self, 'razao_social', razao_social, 'EMPRESA', email)
        return True

    def setEmail(self, email_novo, email):
        Database.connect(self)
        Database.update(self, 'email', email_novo, 'EMPRESA', email)
        return True

    def setTelefone(self, telefone, email):
        Database.connect(self)
        Database.update(self, 'telefone', telefone, 'EMPRESA', email)
        return True

    def setConta(self, conta, email):
        Database.connect(self)
        Database.update(self, 'conta_bancaria', conta, 'EMPRESA', email)
        return True

    def setSenha(self, senha, email):
        Database.connect(self)
        Database.update(self, 'senha', senha, 'EMPRESA', email)
        return True

    def setAreaNegocio(self, area_negocio, email):
        Database.connect(self)
        Database.update(self, 'area_negocio', area_negocio, 'EMPRESA', email)
        return True

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
