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
    def getNome(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'nome', email)
    
    def getSobrenome(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'sobrenome', email)
    
    def getCPF(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'CPF', email)
    
    def getEmail(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'email', email)
    
    def getGenero(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'genero', email)
    
    def getDataNascimento(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'data_nascimento', email)
    
    def getTelefone(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'telefone', email)
    
    def getConta(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'conta_bancaria', email)
    
    def getNome(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'nome', email)
    
    def getSenha(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'senha', email)
    
    def getDescricao(self, email):
        Database.connect(self)
        return Database.select(self, 'DESENVOLVEDOR', 'descricao', email)
    
    def getSobrenome(self):
        self.cursor.execute(f'SELECT sobrenome FROM desenvolvedor WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())

    def setHabilidade(self, habilidade):
        self.cursor.execute(f'UPDATE desenvolvedor SET habilidade = {habilidade} WHERE email = "{self.email}"')
        self.con.commit()
        return True
        
    def setSenha(self, senha, email):
        Database.connect(self)
        Database.update(self, 'senha', senha, 'DESENVOLVEDOR', email)
        return True

    def setHabilidade(self, habilidade, email):
        Database.connect(self)
        Database.update(self, 'habilidade', habilidade, 'DESENVOLVEDOR', email)
        return True

    def setExperiencia(self, experiencia, email):
        Database.connect(self)
        Database.update(self, 'experiencia', experiencia, 'DESENVOLVEDOR', email)
        return True

    def setTag(self, tag, email):
        Database.connect(self)
        Database.update(self, 'tag', tag, 'DESENVOLVEDOR', email)
        return True
    
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

    
    

