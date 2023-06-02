import mysql.connector
class Database:
    def insert(self, tabela, colunas, dados):
        print(f'INSERT INTO {tabela} ({colunas}) VALUES ({dados})')
        self.cursor.execute(f'INSERT INTO {tabela} ({colunas}) VALUES ({dados})')
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