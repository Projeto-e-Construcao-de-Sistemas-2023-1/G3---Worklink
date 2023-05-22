class Desenvolvedor(Usuario):
    def __init__(self):
        super().__init__()
        self.nome = ''
        self.CPF = ''
        self.data_nascimento = ''
    
    def criaDesenvolvedor(self, id, email, telefone, agencia, conta, login, senha, nome, CPF, data_nascimento):
        self.criaUsuario(id, email, telefone, agencia, conta, login, senha)
        self.nome = nome
        self.CPF = CPF
        self.data_nascimento = data_nascimento
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getCPF(self):
        return self.CPF
    
    def setCPF(self, CPF):
        self.CPF = CPF
    
    def getDataNascimento(self):
        return self.data_nascimento
    
    def setDataNascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento
    
    def candidatarProjeto(self, projeto):
        self.projetos_candidatados.append(projeto)
    
    def visualizarProjetos(self, status):
        for projeto in self.projetos:
            if projeto.status == status:
                print(projeto)
    
    def seguirEmpresa(self, empresa):
        self.empresas_seguidas.append(empresa)
    
    def pesquisarProjetos(self, tags):
        projetos_encontrados = []
        for projeto in self.projetos:
            if any(tag in projeto.tags for tag in tags):
                projetos_encontrados.append(projeto)
        return projetos_encontrados
    
    def guardarDinheiroCarteira(self, valor):
        self.saldo_carteira += valor
    
    def marcarReuniao(self, empresa, data, hora):
        reuniao = Reuniao(empresa, data, hora)
        self.reunioes_agendadas.append(reuniao)
    
    def pesquisarEmpresa(self, razao_social):
        for empresa in self.empresas:
            if empresa.razao_social == razao_social:
                return empresa
        return None
    
    def avaliarEmpresa(self, empresa, avaliacao):
        empresa.avaliacoes.append(avaliacao)
    

