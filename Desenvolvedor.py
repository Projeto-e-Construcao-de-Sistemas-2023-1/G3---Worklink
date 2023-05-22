import Usuario
class Desenvolvedor(Usuario):
    def __init__(self):
        super().__init__()
        self.nome = 'xxxx'
        self.CPF = 'xxxx'
        self.data_nascimento = 'xx/xx/xxxx'
    
    def criaDesenvolvedor(self, id, email, telefone, agencia, conta, login, senha, nome, CPF, data_nascimento):
        self.criaUsuario(id, email, telefone, agencia, conta, login, senha)
        self.nome = nome
        self.CPF = CPF
        self.data_nascimento = data_nascimento
        self.tags = []
        self.empresas_seguidas = []
    
    def getNome(self):
        return self.nome
    
    def setDescricao(self, descricao):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao

    def setNome(self, nome):
        self.nome = nome
    
    def setTags(self, tag):
        self.tags.append(tag) # COLOCAR NO BANCO DE DADOS ESSA TAG NOVA

    def getCPF(self):
        return self.CPF
    
    def setCPF(self, CPF):
        self.CPF = CPF
    
    def getDataNascimento(self):
        return self.data_nascimento
    
    def setDataNascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento
    
    def candidataProjeto(self, projeto):
        self.projetos_candidatados.append(projeto)
    
    def visualizaProjetos(self, status):
        for projeto in self.projetos:
            if projeto.status == status:
                print(projeto)
    
    def segueEmpresa(self, empresa):
        self.empresas_seguidas.append(empresa)
    
    def pesquisaProjetos(self, tags):
        projetos_encontrados = []
        for projeto in self.projetos:
            if any(tag in projeto.tags for tag in tags):
                projetos_encontrados.append(projeto)
        return projetos_encontrados
    
    def guardaDinheiroCarteira(self, valor):
        self.saldo_carteira += valor
    
    def marcaReuniao(self, empresa, data, hora):
        reuniao = Reuniao(empresa, data, hora) # Usar integração com Calendar
        self.reunioes_agendadas.append(reuniao)
    
    def pesquisaEmpresa(self, razao_social):
        for empresa in self.empresas:
            if empresa.razao_social == razao_social:
                return empresa
        return None

    def avaliaEmpresa(self, empresa, avaliacao):
        empresa.avaliacoes.append(avaliacao)

    
    

