import Usuario
from Database import Database
# OS GETTERS VÃO SER CONSULTAS NO BANCO DE DADOS PEDINDO AQUELA VARIAVEL
class Desenvolvedor(Usuario.Usuario):    
    def criaDesenvolvedor(self, nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta, senha, habilidade, experiencia, tag):
        values = (nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta, senha, habilidade, experiencia, tag)
        tipo = True
        Database.connect(self)
        Database.insert(self, values, tipo)

    # GETTERS

    def getNome(self):
        self.cursor.execute(f'SELECT nome FROM desenvolvedor WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit() 
        return str(self.cursor.fetchall())
    
    def getGenero(self):
        self.cursor.execute(f'SELECT genero FROM desenvolvedor WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    
    def getHabilidade(self):
        self.cursor.execute(f'SELECT habilidade FROM desenvolvedor WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    
    def getCpf(self):
        self.cursor.execute(f'SELECT CPF FROM desenvolvedor WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    
    def getDataNascimento(self):
        self.cursor.execute(f'SELECT data_nascimento FROM desenvolvedor WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    
    def getSobrenome(self):
        self.cursor.execute(f'SELECT sobrenome FROM desenvolvedor WHERE email = {self.email}') # Tenta achar o cara com essas credenciais
        self.con.commit()
        return str(self.cursor.fetchall())
    
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

    
    

