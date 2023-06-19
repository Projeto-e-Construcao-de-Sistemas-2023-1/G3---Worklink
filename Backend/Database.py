import mysql.connector
class Database:
    def insert(self, values, tipo):
        if tipo == True: # Indica que é um desenvolvedor
            query = """ INSERT INTO DESENVOLVEDOR (nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta_bancaria, senha, descricao, tag_desenvolvedor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        else:
            query = """ INSERT INTO EMPRESA (cnpj, razao_social, email, telefone, conta_bancaria, senha, area_negocio) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(query, values)
        self.con.commit() # INSERT REALIZADO

    def update(self, coluna, dado, tabela, email):
        self.cursor.execute(f'UPDATE {tabela} SET {coluna} = "{dado}" WHERE email = "{email}"')
        self.con.commit() # UPDATE REALIZADO

    def delete(self, tabela, email):
        self.cursor.execute(f'DELETE FROM {tabela} WHERE email = "{email}"')
        self.con.commit() 

    def select(self, tabela, tipo, email): # Se coluna = '0' -> seleciona tudo da tabela sobre aquele dado
        self.cursor.execute(f'SELECT {tipo} FROM {tabela} WHERE email = "{email}"')
        self.con.commit()
        tupla = self.cursor.fetchone()
        return tupla[0]
    
    def autenticaUsuario(self, email, senha):
        self.cursor.execute(f'SELECT * FROM DESENVOLVEDOR JOIN EMPRESA WHERE DESENVOLVEDOR.email = "{email}" AND DESENVOLVEDOR.senha = "{senha}" OR EMPRESA.email = "{email}" AND EMPRESA.senha = "{senha}"') # Tenta achar o cara com essas credenciais
        self.con.commit()
        if self.cursor.fetchall():
            return True # Logado com sucesso 
        else:
            return False # Credenciais inválidas

    def pesquisaUsuario(self, nome, tipo):
        if tipo == True: # TRUE PARA DEV
            self.cursor.execute(f'SELECT DESENVOLVEDOR.nome, DESENVOLVEDOR.descricao FROM DESENVOLVEDOR WHERE nome = "{nome}"')
            self.con.commit()
        else: # FALSE PARA EMPRESA
            self.cursor.execute(f'SELECT EMPRESA.razao_social, EMPRESA.area_negocio FROM EMPRESA WHERE nome = "{nome}"')
            self.con.commit()
        return self.cursor.fetchall() # MOSTRAR OS REGISTROS NA TELA DO FRONT END
    
    def verificaUsuario(self, email):
        self.cursor.execute(f'SELECT * FROM DESENVOLVEDOR WHERE email = "{email}"')
        self.con.commit()
        if self.cursor.fetchall():
            return True # É Desenvolvedor
        else:
            return False # É empresa
    def pesquisaDesenvolvedor(self, nome):
        self.cursor.execute(f'SELECT * FROM DESENVOLVEDOR WHERE nome = "{nome}"')
        self.con.commit()
        return self.cursor.fetchall() # MOSTRAR OS REGISTROS NA TELA DO FRONT END

    def verificaUsuarioNome(self, nome):
        self.cursor.execute(f'SELECT * FROM DESENVOLVEDOR WHERE nome = "{nome}"')
        self.con.commit()
        if self.cursor.fetchall():
            return True # É Desenvolvedor
        else:
            return False # É empresa

    def connect(self):
        self.con = mysql.connector.connect(
        host='35.198.19.238',
        database='db_worklink',
        user='root',
        password='pjSq2023@') # BD acessado!!!
        if self.con.is_connected():
            self.cursor = self.con.cursor(buffered= True)