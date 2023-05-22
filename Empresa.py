import Usuario
class Empresa(Usuario):
    def __init__(self):
        super().__init__()
        self.razao_social = 'xxxx'
        self.projetos = []
    
    def criaEmpresa(self, id, email, telefone, agencia, conta, login, senha, razao_social):
        self.criaUsuario(id, email, telefone, agencia, conta, login, senha)
        self.razao_social = razao_social
    

    def getRazaoSocial(self):
        return self.razao_social
    
    def setRazaoSocial(self, razao_social):
        self.razao_social = razao_social
    
    def publicarProjeto(self, projeto):
        self.projetos.append(projeto)
    
    def visualizarProjetos(self, status):
        for projeto in self.projetos:
            if projeto.status == status:
                print(projeto)
    
    def seguirDesenvolvedor(self, desenvolvedor):
        self.desenvolvedores_seguidos.append(desenvolvedor)
    
    def pesquisarDesenvolvedores(self, tags):
        desenvolvedores_encontrados = []
        for desenvolvedor in self.desenvolvedores:
            if any(tag in desenvolvedor.tags for tag in tags):
                desenvolvedores_encontrados.append(desenvolvedor)
        return desenvolvedores_encontrados
    
    def inserirDinheiroCarteira(self, valor):
        self.saldo_carteira += valor
    
    def realizarPagamento(self, desenvolvedor, valor):
        self.saldo_carteira -= valor
        desenvolvedor.saldo_carteira += valor
    
    def marcarReuniao(self, desenvolvedor, data, hora):
        reuniao = Reuniao(desenvolvedor, data, hora) # Usar integração com Calendar
        self.reunioes_agendadas.append(reuniao)
    
    def pesquisarDesenvolvedor(self, nome):
        for desenvolvedor in self.desenvolvedores:
            if desenvolvedor.nome == nome:
                return desenvolvedor
        return None

    def avaliarDesenvolvedor(self, desenvolvedor, avaliacao):
        desenvolvedor.avaliacoes.append(avaliacao)

    def listarProjetosEmAndamento(self):
        for projeto in self.projetos:
            if projeto.status == "Em andamento":
                print(projeto)

    def listarProjetosConcluidos(self):
        for projeto in self.projetos:
            if projeto.status == "Concluído":
                print(projeto)

    def exibirInformacoes(self):
        print("Razão Social:", self.razao_social)
        print("Email:", self.email)
        print("Telefone:", self.telefone)
