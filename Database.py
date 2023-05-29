import mysql.connector
from tabulate import tabulate


class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            database='db-worklink',
            user='root',
            password='pjSq2023@') 
        #if self.connection.is_connected():
        # print('Conexão estabelecida.')

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print('Conexão encerrada.')

    def ler_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        #self.connection.commit()
        result = cursor.fetchall()
        if len(result) > 0:
            headers = [desc[0] for desc in cursor.description]  # Obter os nomes das colunas
            table = [list(row) for row in result]  # Converter os resultados em uma lista de listas
            print("Registros na tabela:")
            print(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            print("Nenhum registro encontrado na tabela.")
            #print(result)
            cursor.close()
            return result
    
    def criar_query(self, query, values):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        result = cursor.fetchall()
        if len(result) > 0:
            headers = [desc[0] for desc in cursor.description]  # Obter os nomes das colunas
            table = [list(row) for row in result]  # Converter os resultados em uma lista de listas
            print("Registros na tabela:")
            print(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            print("Nenhum registro encontrado na tabela.")
            #print(result)
            cursor.close()
            return result
