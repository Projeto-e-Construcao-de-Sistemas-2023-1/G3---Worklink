import Usuario
from Database import Database
# OS GETTERS VÃO SER CONSULTAS NO BANCO DE DADOS PEDINDO AQUELA VARIAVEL
class Desenvolvedor(Usuario.Usuario):    
    def criaDesenvolvedor(self, nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta, senha, descricao, tag):
        values = (nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta, senha, descricao, tag)
        tipo = True
        Database.connect(self)
        Database.insert(self, values, tipo)

    # GETTERS
    def getNome(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'nome', self.email)
    
    def getSobrenome(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'sobrenome', self.email)
    
    def getCPF(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'CPF', self.email)
    
    def getEmail(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'email', self.email)
    
    def getGenero(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'genero', self.email)
    
    def getDataNascimento(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'data_nascimento', self.email)
    
    def getTelefone(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'telefone', self.email)
    
    def getConta(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'conta_bancaria', self.email)
    
    def getNome(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'nome', self.email)
    
    def getSenha(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'senha', self.email)
    
    def getDescricao(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'descricao', self.email)
    
    def getTag(self):
        Database.connect(self)
        return Database.select('DESENVOLVEDOR', 'tag', self.email)
    
    # SETTERS
    def setNome(self, nome, email):
        Database.connect(self)
        Database.update(self, 'nome', nome, 'DESENVOLVEDOR', email)

    def setSobrenome(self, sobrenome, email):
        Database.connect(self)
        Database.update(self, 'sobrenome', sobrenome, 'DESENVOLVEDOR', email)

    def setCpf(self, CPF, email):
        Database.connect(self)
        Database.update(self, 'CPF', CPF, 'DESENVOLVEDOR', email)

    def setEmail(self, email_novo, email):
        Database.connect(self)
        Database.update(self, 'email', email_novo, 'DESENVOLVEDOR', email)

    def setGenero(self, genero, email):
        Database.connect(self)
        Database.update(self, 'genero', genero, 'DESENVOLVEDOR', email)

    def setDataNascimento(self, data_nascimento, email):
        Database.connect(self)
        Database.update(self, 'data_nascimento', data_nascimento, 'DESENVOLVEDOR', email)

    def setTelefone(self, telefone, email):
        Database.connect(self)
        Database.update(self, 'telefone', telefone, 'DESENVOLVEDOR', email)

    def setConta(self, conta, email):
        Database.connect(self)
        Database.update(self, 'conta_bancaria', conta, 'DESENVOLVEDOR', email)
        
    def setSenha(self, senha, email):
        Database.connect(self)
        Database.update(self, 'senha', senha, 'DESENVOLVEDOR', email)

    def setHabilidade(self, habilidade, email):
        Database.connect(self)
        Database.update(self, 'habilidade', habilidade, 'DESENVOLVEDOR', email)

    def setExperiencia(self, experiencia, email):
        Database.connect(self)
        Database.update(self, 'experiencia', experiencia, 'DESENVOLVEDOR', email)

    def setTag(self, tag, email):
        Database.connect(self)
        Database.update(self, 'tag', tag, 'DESENVOLVEDOR', email)
    
    #def candidataProjeto(self, projeto):
        # INSERIR NO BD O PROJETO QUE O CARA SE CANDIDATOU
    #    pass
    
    #def visualizaProjetos(self, status):
    #    for projeto in self.projetos:
    #        if projeto.status == status:
    #            print(projeto)
    
    #def segueEmpresa(self, empresa):
    #    self.empresas_seguidas.append(empresa)
    
    #def pesquisaProjetos(self, tags):
    #    projetos_encontrados = []
    #    for projeto in self.projetos:
    #        if any(tag in projeto.tags for tag in tags):
    #            projetos_encontrados.append(projeto)
    #    return projetos_encontrados
    
    #def guardaDinheiroCarteira(self, valor):
    #    self.saldo_carteira += valor
    
    #def marcaReuniao(self, empresa, data, hora):
    #    reuniao = Reuniao(empresa, data, hora) # Usar integração com Calendar
    #    self.reunioes_agendadas.append(reuniao)
    
    #def pesquisaEmpresa(self, razao_social):
    #    for empresa in self.empresas:
    #        if empresa.razao_social == razao_social:
    #            return empresa
    #    return None

    #def avaliaEmpresa(self, empresa, avaliacao):
    #    empresa.avaliacoes.append(avaliacao)

    
    

