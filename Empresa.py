import Usuario
class Empresa(Usuario.Usuario):
   
    def criaEmpresa(self, email, telefone, agencia, conta, login, senha, razao_social):
        self.criaUsuario(self, email, telefone, agencia, conta, login, senha)
        # Fazer insert da razao social
    
    def getRazaoSocial(self):
        #SELECT RAZAO_SOC FROM EMPRESA WHERE EMAIL = XXXX
        pass
    
    def setRazaoSocial(self, razao_social):
        #SELECT RAZAO_SOC FROM EMPRESA WHERE EMAIL = XXXX -- UPDATE
        pass
    #def publicarProjeto(self, projeto):
    #    self.projetos.append(projeto)
    
    #def visualizarProjetos(self, status):
    #    for projeto in self.projetos:
    #        if projeto.status == status:
    #            print(projeto)
    
    #def seguirDesenvolvedor(self, desenvolvedor):
    #    self.desenvolvedores_seguidos.append(desenvolvedor)
    
    def pesquisarDesenvolvedores(self, tags):
        # SELECT * FROM DEVS WHERE ?
        pass
        #return desenvolvedores_encontrados
    
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
