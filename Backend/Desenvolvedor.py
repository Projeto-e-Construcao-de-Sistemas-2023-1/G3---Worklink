import Usuario
from Database import Database
# OS GETTERS VÃO SER CONSULTAS NO BANCO DE DADOS PEDINDO AQUELA VARIAVEL
class Desenvolvedor(Usuario.Usuario):    
    def criaDesenvolvedor(self, nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta, senha, tag):

        
        values = (nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta, senha, tag)
        tipo = True
        #print(lista_dados)
        Database.connect(self)
        Database.insert(self, values, tipo)
        
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

    # def setHabilidade(self, habilidade):
    #     self.cursor.execute(f'UPDATE desenvolvedor SET habilidade = {habilidade} WHERE email = "{self.email}"')
    #     self.con.commit()
    #     return True

    def setNome(self, nome):
        self.cursor.execute(f'UPDATE desenvolvedor SET nome = {nome} WHERE email = "{self.email}"')
        self.con.commit()
        return True

    def setSobrenome(self, sobrenome):
        self.cursor.execute(f'UPDATE desenvolvedor SET sobrenome = {sobrenome} WHERE email = "{self.email}"')
        self.con.commit()
        return True
    
    def setGenero(self, genero):
        self.cursor.execute(f'UPDATE desenvolvedor SET genero = {genero} WHERE email = "{self.email}"')
        self.con.commit()
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

    
    

