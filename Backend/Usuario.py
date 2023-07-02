from flask import jsonify, flash
from Database import Database
from decimal import Decimal
import pyperclip
class Usuario: # CLASSE QUE TERÁ OS METODOS COMUNS A DESENVOLVEDOR E EMPRESA
    def deletaUsuario(self): # Passar tipo = True para DESENVOLVEDOR | tipo = False para EMPRESA
        Database.connect(self)
        if self.tipo == True:
            Database.delete(self, 'DESENVOLVEDOR', self.email)
        else:
            Database.delete('EMPRESA', self.email)
            
    def iniciaSessao(self, email, senha):
        Database.connect(self)
        if Database.autenticaUsuario(self, email, senha):
            self.email = email # Grava email do usuario logado para futuras consultas
            return True # vai vir como True ou False
        else:
            return False
        
    def finalizaSessao(self):
        pass # Apenas no front end

    def verificaUsuario(self):
        Database.connect(self)
        self.tipo = Database.verificaUsuario(self, self.email)
        return self.tipo
    
    def toClipboard(self, texto):
        pyperclip.copy(texto)
    
    def capturaEmail(self, email):
        self.email = email

    def pesquisaUsuario(self, nome, tipo):
        Database.connect(self)
        return Database.pesquisaUsuario(self, nome, tipo)
    
    #  def Follow(self, seguidor, seguido, tipoSeguidor, tipoSeguido):
    #     Database.connect(self)
    #     if self.verificaUsuario(self):
    #         tipo = 'dev'
    #     tipo = 'emp'
    #     if verificaUsuario(cod):
    #         tipoSeguido = 'dev'
    #     tipoSeguido = 'emp'
    #     if Database.checkFollow(self, self.cod, codSgd, tipoSgr, tipoSgd):
    #         return False  
    #         #Ja segue
    #     else:
    #         Database.Follow(self, self.cod, codSgd, tipoSgr, tipoSgd)
    #         return True 
    #         #começou a seguir

    # def Unfollow(self, cod, tipo):
    #     Database.connect(self)
    #     if self.verificaUsuario(self):
    #         tipo = 'dev'
    #     tipo = 'emp'
    #     if verificaUsuario(cod):
    #         tipoSeguido = 'dev'
    #     tipoSeguido = 'emp'
    #     if Database.checkFollow(self, self.cod, cod, tipo, tipoSeguido):
    #         Database.Unfollow(self, self.cod, cod)
    #         return True  
    #         #deu unfollow
    #     else:
    #         return False
    #         #nao estava seguindo

    def Depositar(self, tipoUsuario, codUsuario, valor):
        Database.connect(self)
        if Database.inserir_dinheiro(self, tipoUsuario, codUsuario, valor):
            return True
        return False

    def Sacar(self, tipoUsuario, codUsuario, valor):
        Database.connect(self)
        saldo = Database.verificar_saldo(self, tipoUsuario, codUsuario)
        valorDecimal = Decimal(valor)
        if saldo is None or saldo < valorDecimal:
            return False
            flash('Valor especificado é maior do que o saldo disponível na conta')
            return jsonify({'message': 'Falha ao sacar dinheiro da carteira'}), 400
        else:
            Database.sacar_dinheiro(self, tipoUsuario, codUsuario, valor)
            return True
            return jsonify({'message': 'Dinheiro sacado da carteira com sucesso'}), 200

    def realizarTransacao(self, codEmpresa, codDesenvolvedor, valor, descricao):
        Database.connect(self)
        saldoEmpresa = Database.verificar_saldo(self, False, codEmpresa)
        valorDecimal = Decimal(valor)
        if saldoEmpresa is None or saldoEmpresa < valorDecimal:
            return False
            flash('Valor para transacao é menor do que valor disponivel na conta')
            return jsonify({'message': 'Falha ao transferir'}), 400
        else:
            Database.realizar_transacao(self, codEmpresa, codDesenvolvedor, valor, descricao)
            return True
            return jsonify({'message': 'Transação realizada com sucesso'}), 200
    
    def verificarSaldo(self, tipoUsuario, codUsuario):
        Database.connect(self)
        saldo = Database.verificar_saldo(self, tipoUsuario, codUsuario)
        return saldo