import Usuario, pymysql
# OS GETTERS VÃO SER CONSULTAS NO BANCO DE DADOS PEDINDO AQUELA VARIAVEL
class Desenvolvedor(Usuario.Usuario):    
    def criaDesenvolvedor(self, email, telefone, agencia, conta, login, senha):#, nome, CPF, data_nascimento):
        self.criaUsuario(self, email, telefone, agencia, conta, login, senha)
        # Fazer também os inserts no BD de nome, CPF e data_nascimento

    def getNome(self):
        # CONSULTA NO BD PEDINDO O NOME (DANDO O EMAIL)
        # SELECT NOME FROM DEVS WHERE EMAIL = XXXX
        pass

    def setDescricao(self, descricao):
        # INSERT DA DESCRIÇÃO NO BD
        pass

    def getDescricao(self):
        #SELECT DESCRIÇÃO FROM DEVS WHERE EMAIL = XXXX
        pass

    def setNome(self, nome):
        # INSERT NO NOME DO CARA
        pass
    
    def setTags(self, tag):
        # COLOCAR NO BANCO DE DADOS ESSA TAG NOVA
        pass

    def getCPF(self):
        # SELECT CPF FROM DEVS WHERE EMAIL = XXXX
        pass
    
    def setCPF(self, CPF):
        # MUDAR O CPF DO CARA NO BD
        pass
    
    def getDataNascimento(self):
        # SELECT DATA_NASC FROM DEVS WHERE EMAIL = XXXX
        pass
    
    def setDataNascimento(self, data_nascimento):
        # MUDAR A DATA_NASC DO CARA NO BD
        pass
    
    def conectaBD():
        
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

    
    

