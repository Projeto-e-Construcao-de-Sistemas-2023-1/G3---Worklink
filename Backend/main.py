# Arquivo main para testes de funcionalidades das classes e do BD
from Desenvolvedor import Desenvolvedor
from Empresa import Empresa
from Database import Database
from Usuario import Usuario
from flask import Flask, render_template, redirect, request, abort, url_for, session 
import requests
from datetime import datetime as dt

app = Flask(__name__, template_folder="templates")
emailsessao=''
emp = Empresa()
#emp.criaEmpresa(cnpj, razao_social, email, telefone, conta, senha, area_negocio)
dev = Desenvolvedor()
#dev.criaDesenvolvedor('desenvolvedor', 'senior', '19828347589', 'dev@outlook.com', 'masculino', '2000/12/12', '(21)8573487509', '12345678901',
#                     'senha', 'pleno', 'python')
db = Database()
us = Usuario()
#Rotas 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/editar_perfil', methods=['GET'])
def editarp():
    return render_template('editar_perfil.html') 

@app.route('/signup_dev', methods=['GET'])
def regdv():
    return render_template('RegisterDesenvolvedor.html') 

@app.route('/signup_emp', methods=['GET'])
def regem():
    return render_template('RegisterEmpresa.html') 

@app.route('/login', methods=['GET'])
def login():
   return render_template('login.html')

@app.route('/perfil', methods=['GET'])
def perfildev():
   return render_template('perfil_dev.html')

@app.route('/criar_Projeto', methods=['GET'])
def criar_projeto():
    return render_template('criarProjeto.html')

#metodos 

@app.route('/authlogin', methods=['POST'])
def authlogin():
    email = request.form.get('email')
    password = request.form.get('password')
    us.sessao(email)
    if dev.iniciaSessao(email, password) == True:
        #funcao pesquisar email na tabela de dev
        return render_template('pagina_inicial.html', nome=dev.getNome(email), sobrenome=dev.getSobrenome(email), descricao=dev.getDescricao(email))
    else:
        print('Erro')
        return render_template('home.html')  # criar pagina de erro com para nova tentativa
emailsessao=dev.getNome
@app.route('/pesquisa_usuario', methods=['post'])
def pesquisaUser():
    pesquisa_user = request.form.get('pesquisa_user')
    print(pesquisa_user)
    
    if us.verificaUsuario(pesquisa_user) == True:
        return render_template('resultado_pesquisa.html', nome=dev.getNome(pesquisa_user), descricao=dev.getDescricao(pesquisa_user))
    #else:
    #   return render_template('resultado_pesquisa.html', nome=emp.getRazaoSocial(pesquisa_user), descricao=emp.getAreaNegocio(pesquisa_user))

@app.route('/signup_developer', methods=['POST'])
def regdev():
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        cpf = request.form.get('cpf')
        email = request.form.get('email')
        genero = request.form.get('genero')
        data_nascimento = request.form.get('data_nascimento')
        telefone = request.form.get('telefone')
        conta = request.form.get('conta')
        senha = request.form.get('senha')
        #rNovaSenha = request.form.get('rNovaSenha')
        descricao = request.form.get('descricao')
        tag = request.form.get('tag')
    #funcao para o backend
        dev.criaDesenvolvedor(nome, sobrenome, cpf, email, genero, data_nascimento, telefone, conta, senha, descricao, tag)
        print(email)
        print(senha)
        return render_template('home.html') 
    
@app.route('/signup_enterprise', methods=['POST'])
def regEmp():
    cnpj = request.form.get('cnpj')
    razao_social = request.form.get('razao_social')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    conta = request.form.get('conta')
    senha = request.form.get('senha')
    #confirm_password = request.form.get('confirm_password')
    area_negocio = request.form.get('area_negocio')
    #funcao para o backend
    emp.criaEmpresa(cnpj, razao_social, email, telefone, conta, senha, area_negocio)
    return render_template('home.html')

@app.route('/delete_conta', methods=['POST'])
def delete_conta():
    emailsessao = session.get('emailsessao')
    if db.verificaUsuario(emailsessao)==True:
        tabela=('DESENVOLVEDOR')
    else:
        tabela=('EMPRESA')
        
    db.delete(tabela, emailsessao)

@app.route('/edita_perfil', methods=['POST'])
def edita_perfil():
    name = request.form.get('name')
    sobrenome = request.form.get('sobrenome')
    descricao = request.form.get('descricao')
    print(name)
    print(emailsessao)
    print(sobrenome)
    print(descricao)
    dev.setNome(name, emailsessao)
    dev.setSobrenome(sobrenome, emailsessao)
    dev.setDescricao(descricao, emailsessao)

    return render_template('perfil_dev.html')

@app.route('/criarProjeto', methods=['POST'])
def criarProjeto():
    nomeProjeto = request.form.get('nomeProjeto')
    nunDev = request.form.get('nunDev')
    tag = request.form.get('tag')
    descricao = request.form.get('descricao')
    return render_template('perfil_dev.html')
  
@app.route("/sign-user-in", methods=['POST'])
def sign_in_user():
    secret_response = request.form['g-recaptcha-response']
    print(request.form)
    verify_response = requests.post(url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}')

    print(verify_response)

    if verify_response['success'] == False:
        abort(401)

    return redirect(url_for('home'))

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()

SITE_KEY = "6LeKBj8mAAAAAA3jCMVID2PjUUYmIM1TYOIKf3Ei"
SECRET_KEY = "6LeKBj8mAAAAAAIsJpHljREaS2EPF8y5uw2frJHA"
VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"