import mysql.connector
class Database:
    def insert(self, query, values, tipo):
        #print(f'INSERT INTO {tabela} ({colunas}) VALUES ({dados})')
        query = """ INSERT INTO DESENVOLVEDOR (nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta_bancaria, senha, habilidade, experiencia, tag_desenvolvedor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.cursor.execute(query, values)
        self.con.commit() # INSERT REALIZADO

    def update(self, coluna, dado, tabela, email):
        self.cursor.execute(f'UPDATE {tabela} SET {coluna} = {dado} WHERE email = "{email}"')
        self.con.commit() # UPDATE REALIZADO
    def delete(self, tabela, email):
        self.cursor.execute(f'DELETE FROM {tabela} WHERE email = {email}')
        self.con.commit() 
    def select(self, coluna, dado, tabela):
        pass
    def connect(self):
        self.con = mysql.connector.connect(
        host='35.247.225.250',
        database='db_worklink',
        user='root',
        password='pjSq2023@') # BD acessado!!!
        if self.con.is_connected():
            self.cursor = self.con.cursor()