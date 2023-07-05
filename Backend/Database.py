import mysql.connector
from calendar import monthrange
class Database:
    def insert(self, values, tipo):
        if tipo == True: # Indica que é um desenvolvedor
            query = """ INSERT INTO DESENVOLVEDOR (nome, sobrenome, CPF, email, genero, data_nascimento, telefone, conta_bancaria, senha, descricao, tag_desenvolvedor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.execute(query, values)
            self.con.commit() # INSERT REALIZADO
            cod_desenvolvedor = self.cursor.lastrowid
            query_saldo = """INSERT INTO SALDO_DESENVOLVEDOR (cod_desenvolvedor, saldo) VALUES (%s, %s)"""
            self.cursor.execute(query_saldo, (cod_desenvolvedor, 0))
            self.con.commit()  # Inserção na tabela SALDO_DESENVOLVEDOR
        else:
            query = """ INSERT INTO EMPRESA (cnpj, razao_social, email, telefone, conta_bancaria, senha, area_negocio, cep) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.execute(query, values)
            self.con.commit() # INSERT REALIZADO
            cod_empresa = self.cursor.lastrowid
            query_saldo = """INSERT INTO SALDO_EMPRESA (cod_empresa, saldo) VALUES (%s, %s)"""
            self.cursor.execute(query_saldo, (cod_empresa, 0))
            self.con.commit()  # Inserção na tabela SALDO_EMPRESA

    def update(self, coluna, dado, tabela, email):
        self.cursor.execute(f'SET FOREIGN_KEY_CHECKS=0;')
        self.con.commit()
        self.cursor.execute(f'UPDATE {tabela} SET {coluna} = "{dado}" WHERE email = "{email}"')
        self.con.commit() # UPDATE REALIZADO
        self.cursor.execute(f'SET FOREIGN_KEY_CHECKS=1;')
        self.con.commit()

    def delete(self, tabela, email):
        self.cursor.execute(f'SET FOREIGN_KEY_CHECKS=0;')
        self.con.commit()
        self.cursor.execute(f'DELETE FROM {tabela} WHERE email = "{email}"')
        self.con.commit()
        self.cursor.execute(f'SET FOREIGN_KEY_CHECKS=1;')
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
        if tipo:  # True para desenvolvedor
            self.cursor.execute('SELECT DESENVOLVEDOR.nome, DESENVOLVEDOR.sobrenome, DESENVOLVEDOR.cod_desenvolvedor FROM DESENVOLVEDOR WHERE nome LIKE %s', (f'%{nome}%',))
            self.con.commit()
        else:  # False para empresa
            self.cursor.execute('SELECT EMPRESA.razao_social, EMPRESA.area_negocio, EMPRESA.cod_empresa FROM EMPRESA WHERE nome LIKE %s', (f'%{nome}%',))
            self.con.commit()
        return self.cursor.fetchall()

    # def pesquisaUsuario(self, nome, tipo):
    #     #cursor = self.con.cursor(dictionary=True)
    #     if tipo:  # True para desenvolvedor
    #         #cursor.execute("SELECT * FROM DESENVOLVEDOR WHERE nome LIKE %s", (f"%{nome}%",))
    #         self.cursor.execute(f'SELECT DESENVOLVEDOR.nome, DESENVOLVEDOR.sobrenome, DESENVOLVEDOR.cod_desenvolvedor FROM DESENVOLVEDOR WHERE nome = "{nome}"')
    #         self.con.commit()
    #     else:  # False para empresa
    #         #cursor.execute("SELECT * FROM EMPRESA WHERE nome LIKE %s", (f"%{nome}%",))
    #         self.cursor.execute(f'SELECT EMPRESA.razao_social, EMPRESA.area_negocio, EMPRESA.cod_empresa FROM EMPRESA WHERE nome = "{nome}"')
    #         self.con.commit()
    #     return self.cursor.fetchall()
        # results = cursor.fetchall()
        # self.con.commit()
        # cursor.close()
        # return results
    
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
    
    def insertEvent(self, values, tipo):
        if tipo:
            query = "INSERT INTO `events` (`start`, `end`, `text`, `color`, `bg`, `idDev`) VALUES (%s,%s,%s,%s,%s,%s)"
        else:
            query = "INSERT INTO `events` (`start`, `end`, `text`, `color`, `bg`, `idEmp`) VALUES (%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(query, values)
        self.con.commit() # INSERT REALIZADO
    
    def updateEvent(self, inicio, fim, texto, cor, fundo, id):
        data = (inicio, fim, texto, cor, fundo, id)
        self.cursor.execute(f"UPDATE events SET start='{inicio}', end='{fim}', text='{texto}', color='{cor}', bg='{fundo}' WHERE id='{id}'")
        data = data + (id,) # Dando problema
        self.con.commit() # INSERT REALIZADO

    def deleteEvent(self, id):
        self.cursor.execute(f'DELETE FROM events WHERE id= "{id}"')
        self.con.commit()

    # -- TENTATIVA DE GET EVENTO

    def getEvent(self, month, year, id_user, tipo):
        daysInMonth = str(monthrange(year, month)[1])
        month = month if month>10 else "0" + str(month)
        dateYM = str(year) + "-" + str(month) + "-"
        start = dateYM + "01 00:00:00"
        end = dateYM + daysInMonth + " 23:59:59"
        if tipo: # -- Para DEV
            self.cursor.execute(f'SELECT * FROM events WHERE (idDev = "{id_user}" AND ((start BETWEEN "{start}" AND "{end}") OR (end BETWEEN "{start}" AND "{end}") OR (start <= "{start}" AND end >= "{end}")))')
        else:
            self.cursor.execute(f'SELECT * FROM events WHERE (idEmp = "{id_user}" AND ((start BETWEEN "{start}" AND "{end}") OR (end BETWEEN "{start}" AND "{end}") OR (start <= "{start}" AND end >= "{end}")))')  
        rows = self.cursor.fetchall()
        if len(rows)==0:
            return None
        data = {}
        for r in rows:
            data[r[0]] = {
            "s" : r[3], "e" : r[4],
            "c" : r[6], "b" : r[7],
            "t" : r[5]
            }
        return data
    
    def checkFollow(self, codSeguidor, codSeguido, tipoSeguido, tipoSeguidor):
        if tipoSeguidor == 'dev' and tipoSeguido == 'emp': 
             self.cursor.execute('SELECT COUNT(*) FROM SEGUIDORES WHERE seguidorDesenvolvedor = ? AND  seguidoEmpresa = ?', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'dev' and tipoSeguido == 'dev':
             self.cursor.execute('SELECT COUNT(*) FROM SEGUIDORES WHERE seguidorDesenvolvedor = ? AND  seguidoDesenvolvedor = ?', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'emp' and tipoSeguido == 'dev':
             self.cursor.execute('SELECT COUNT(*) FROM SEGUIDORES WHERE seguidorEmpresa = ? AND  seguidoDesenvolvedor = ?', (codSeguidor, codSeguido))
        else: 
        #elif tipoSeguidor =='emp' and tipoSeguido =='emp':
             self.cursor.execute('SELECT COUNT(*) FROM SEGUIDORES WHERE seguidorEmpresa = ? AND  seguidoEmpresa = ?', (codSeguidor, codSeguido))
        count = self.cursor.fetchone()[0]
        return count > 0

    def Unfollow(self, codSeguidor, codSeguido, tipoSeguido, tipoSeguidor):
        if tipoSeguidor == 'dev' and tipoSeguido == 'emp': 
             self.cursor.execute('DELETE FROM SEGUIDORES WHERE seguidorDesenvolvedor = ? AND seguidoEmpresa = ?', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'dev' and tipoSeguido == 'dev':
             self.cursor.execute('DELETE FROM SEGUIDORES WHERE seguidorDesenvolvedor = ? AND seguidoDesenvolvedor = ?', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'emp' and tipoSeguido == 'dev':
             self.cursor.execute('DELETE FROM SEGUIDORES WHERE seguidorEmpresa = ? AND seguidoDesenvolvedor = ?', (codSeguidor, codSeguido))
        else:
        #elif tipoSeguidor =='emp' and tipoSeguido =='emp':
             self.cursor.execute('DELETE FROM SEGUIDORES WHERE seguidorEmpresa = ? AND seguidoEmpresa = ?', (codSeguidor, codSeguido))
        self.conn.commit()

    def Follow(self, codSeguidor, codSeguido, tipoSeguidor, tipoSeguido):
        if tipoSeguidor == 'dev' and tipoSeguido == 'emp': 
             self.cursor.execute('INSERT INTO SEGUIDORES (seguidorDesenvolvedor, seguidoEmpresa) VALUES (?, ?)', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'dev' and tipoSeguido == 'dev':
             self.cursor.execute('INSERT INTO SEGUIDORES (seguidorDesenvolvedor, seguidoDesenvolvedor) VALUES (?, ?)', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'emp' and tipoSeguido == 'dev':
             self.cursor.execute('INSERT INTO SEGUIDORES (seguidorEmpresa, seguidoDesenvolvedor) VALUES (?, ?)', (codSeguidor, codSeguido))
        else:
        #elif tipoSeguidor =='emp' and tipoSeguido =='emp':
             self.cursor.execute('INSERT INTO SEGUIDORES (seguidorEmpresa, seguidoEmpresa) VALUES (?, ?)', (codSeguidor, codSeguido))
        self.conn.commit()

    def inserir_dinheiro(self, tipoUsuario, codUsuario, valor):
        cursor = self.con.cursor()
        if tipoUsuario == False:
            update_query = "UPDATE SALDO_EMPRESA SET saldo = saldo + %s WHERE cod_empresa = %s"
        # elif tipoUsuario == 'desenvolvedor':
        #     update_query = "UPDATE SALDO_DESENVOLVEDOR SET saldo = saldo + %s WHERE cod_desenvolvedor = %s"
        else:
            return False
        cursor.execute(update_query, (valor, codUsuario))
        self.con.commit()
        return True
    
    def verificar_saldo(self, tipo, codigo):
        cursor = self.con.cursor()
        if tipo == False:
            saldo_query = "SELECT saldo FROM SALDO_EMPRESA WHERE cod_empresa = %s"
        elif tipo == True:
            saldo_query = "SELECT saldo FROM SALDO_DESENVOLVEDOR WHERE cod_desenvolvedor = %s"
        else:
            return None
        cursor.execute(saldo_query, (codigo,))
        result = cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            return None

    def sacar_dinheiro(self, tipoUsuario, codUsuario, valor):
        cursor = self.con.cursor()
        if tipoUsuario == False:
            update_query = "UPDATE SALDO_EMPRESA SET saldo = saldo - %s WHERE cod_empresa = %s"
        elif tipoUsuario == True:
            update_query = "UPDATE SALDO_DESENVOLVEDOR SET saldo = saldo - %s WHERE cod_desenvolvedor = %s"
        else:
            return False
        cursor.execute(update_query, (valor, codUsuario))
        self.con.commit()
        return True

    def realizar_transacao(self, codEmpresa, codDesenvolvedor, valor, descricao):
        cursor = self.con.cursor()
        insert_query = "INSERT INTO TRANSACOES (descricao, valor, empresa_pagante, desenvolvedor_recebedor) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (descricao, valor, codEmpresa, codDesenvolvedor))
        update_query_SALDO_EMPRESA = "UPDATE SALDO_EMPRESA SET saldo = saldo - %s WHERE cod_empresa = %s"
        cursor.execute(update_query_SALDO_EMPRESA, (valor, codEmpresa))
        update_query_SALDO_DESENVOLVEDOR = "UPDATE SALDO_DESENVOLVEDOR SET saldo = saldo + %s WHERE cod_desenvolvedor = %s"
        cursor.execute(update_query_SALDO_DESENVOLVEDOR, (valor, codDesenvolvedor))
        self.con.commit()
        return True

    def connect(self):
        self.con = mysql.connector.connect(
        host='35.198.19.238',
        database='db_worklink',
        user='root',
        password='pjSq2023@') # BD acessado!!!
        if self.con.is_connected():
            self.cursor = self.con.cursor(buffered= True)

    def checkFollow(self, codSeguidor, codSeguido, tipoSeguido, tipoSeguidor):
        if tipoSeguidor == 'dev' and tipoSeguido == 'emp': 
             self.cursor.execute('SELECT COUNT(*) FROM SEGUIDORES WHERE seguidorDesenvolvedor = ? AND  seguidoEmpresa = ?', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'dev' and tipoSeguido == 'dev':
             self.cursor.execute('SELECT COUNT(*) FROM SEGUIDORES WHERE seguidorDesenvolvedor = ? AND  seguidoDesenvolvedor = ?', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'emp' and tipoSeguido == 'dev':
             self.cursor.execute('SELECT COUNT(*) FROM SEGUIDORES WHERE seguidorEmpresa = ? AND  seguidoDesenvolvedor = ?', (codSeguidor, codSeguido))
        else: 
        #elif tipoSeguidor =='emp' and tipoSeguido =='emp':
             self.cursor.execute('SELECT COUNT(*) FROM SEGUIDORES WHERE seguidorEmpresa = ? AND  seguidoEmpresa = ?', (codSeguidor, codSeguido))
        count = self.cursor.fetchone()[0]
        return count > 0

    def Unfollow(self, codSeguidor, codSeguido, tipoSeguido, tipoSeguidor):
        if tipoSeguidor == 'dev' and tipoSeguido == 'emp': 
             self.cursor.execute('DELETE FROM SEGUIDORES WHERE seguidorDesenvolvedor = ? AND seguidoEmpresa = ?', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'dev' and tipoSeguido == 'dev':
             self.cursor.execute('DELETE FROM SEGUIDORES WHERE seguidorDesenvolvedor = ? AND seguidoDesenvolvedor = ?', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'emp' and tipoSeguido == 'dev':
             self.cursor.execute('DELETE FROM SEGUIDORES WHERE seguidorEmpresa = ? AND seguidoDesenvolvedor = ?' (codSeguidor, codSeguido))
        else:
        #elif tipoSeguidor =='emp' and tipoSeguido =='emp':
             self.cursor.execute('DELETE FROM SEGUIDORES WHERE seguidorEmpresa = ? AND seguidoEmpresa = ?', (codSeguidor, codSeguido))
        self.conn.commit()

    def Follow(self, codSeguidor, codSeguido, tipoSeguidor, tipoSeguido):
        if tipoSeguidor == 'dev' and tipoSeguido == 'emp': 
             self.cursor.execute('INSERT INTO SEGUIDORES (seguidorDesenvolvedor, seguidoEmpresa) VALUES (?, ?)', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'dev' and tipoSeguido == 'dev':
             self.cursor.execute('INSERT INTO SEGUIDORES (seguidorDesenvolvedor, seguidoDesenvolvedor) VALUES (?, ?)', (codSeguidor, codSeguido))
        elif tipoSeguidor == 'emp' and tipoSeguido == 'dev':
             self.cursor.execute('INSERT INTO SEGUIDORES (seguidorEmpresa, seguidoDesenvolvedor) VALUES (?, ?)', (codSeguidor, codSeguido))
        else:
        #elif tipoSeguidor =='emp' and tipoSeguido =='emp':
             self.cursor.execute('INSERT INTO SEGUIDORES (seguidorEmpresa, seguidoEmpresa) VALUES (?, ?)', (codSeguidor, codSeguido))
        self.conn.commit()

    def inserir_dinheiro(self, tipoUsuario, codUsuario, valor):
        cursor = self.con.cursor()
        if tipoUsuario == 'empresa':
            update_query = "UPDATE SALDO_EMPRESA SET saldo = saldo + %s WHERE cod_empresa = %s"
        elif tipoUsuario == 'desenvolvedor':
            update_query = "UPDATE SALDO_DESENVOLVEDOR SET saldo = saldo + %s WHERE cod_desenvolvedor = %s"
        else:
            return False
        cursor.execute(update_query, (valor, codUsuario))
        self.con.commit()
        return True
    
    def verificar_saldo(self, tipo, codigo):
        cursor = self.con.cursor()
        if tipo == 'empresa':
            saldo_query = "SELECT saldo FROM SALDO_EMPRESA WHERE cod_empresa = %s"
        elif tipo == 'desenvolvedor':
            saldo_query = "SELECT saldo FROM SALDO_DESENVOLVEDOR WHERE cod_desenvolvedor = %s"
        else:
            return None
        cursor.execute(saldo_query, (codigo,))
        result = cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            return None

    def sacar_dinheiro(self, tipoUsuario, codUsuario, valor):
        cursor = self.con.cursor()
        if tipoUsuario == 'empresa':
            update_query = "UPDATE SALDO_EMPRESA SET saldo = saldo - %s WHERE cod_empresa = %s"
        elif tipoUsuario == 'desenvolvedor':
            update_query = "UPDATE SALDO_DESENVOLVEDOR SET saldo = saldo - %s WHERE cod_desenvolvedor = %s"
        else:
            return False
        cursor.execute(update_query, (valor, codUsuario))
        self.con.commit()
        return True

    def realizar_transacao(self, codEmpresa, codDesenvolvedor, valor, descricao):
        cursor = self.con.cursor()
        insert_query = "INSERT INTO TRANSACOES (descricao, valor, empresa_pagante, desenvolvedor_recebedor) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (descricao, valor, codEmpresa, codDesenvolvedor))
        update_query_SALDO_EMPRESA = "UPDATE SALDO_EMPRESA SET saldo = saldo - %s WHERE cod_empresa = %s"
        cursor.execute(update_query_SALDO_EMPRESA, (valor, codEmpresa))
        update_query_SALDO_DESENVOLVEDOR = "UPDATE SALDO_DESENVOLVEDOR SET saldo = saldo + %s WHERE cod_desenvolvedor = %s"
        cursor.execute(update_query_SALDO_DESENVOLVEDOR, (valor, codDesenvolvedor))
        self.con.commit()
        return True