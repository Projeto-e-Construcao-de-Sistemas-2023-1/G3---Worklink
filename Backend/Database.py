import mysql.connector
class Database:
    def __init__(self) -> None:
        pass
    def insert(tipo, dado, tabela):
        pass
    def update(tipo, dado, tabela):
        pass
    def delete(tipo, dado, tabela):
        pass
    def select(tipo, dado, tabela):
        pass
    def conect(self):
        self.con = mysql.connector.connect(
        host='35.247.225.250',
        database='db_worklink',
        user='root',
        password='pjSq2023@') # BD acessado!!!
        if self.con.is_connected():
            self.cursor = self.con.cursor()