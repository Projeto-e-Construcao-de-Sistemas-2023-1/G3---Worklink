import Usuario
class Empresa(Usuario.Usuario):
    def criaEmpresa(self, cnpj, email, telefone, conta, senha, razao_social, area_negocio):
        self.cursor.execute(f'INSERT INTO empresa (CNPJ, razao_social, area_negocio, email, telefone, conta_bancaria, login, senha) VALUES ({cnpj}, {razao_social}, {area_negocio}, {email}, {telefone}, {conta}, {senha})')
        self.con.commit() # INSERT REALIZADO

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