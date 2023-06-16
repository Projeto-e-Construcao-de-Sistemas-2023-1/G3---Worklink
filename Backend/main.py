# Arquivo main para testes de funcionalidades das classes e do BD
from Desenvolvedor import Desenvolvedor
from Empresa import Empresa
from Database import Database
from flask import Flask, render_template, redirect, request, abort, url_for, jsonify, flash
import requests
from datetime import datetime as dt
from flask_wtf import FlaskForm, RecaptchaField 
import Usuario

app = Flask(__name__, template_folder="templates")
emailsessao=''
emp = Empresa()
#emp.criaEmpresa(cnpj, razao_social, email, telefone, conta, senha, area_negocio)
dev = Desenvolvedor()
#dev.criaDesenvolvedor('desenvolvedor', 'senior', '19828347589', 'dev@outlook.com', 'masculino', '2000/12/12', '(21)8573487509', '12345678901',
#                     'senha', 'pleno', 'python')
db = Database()

app.config["SECRET_KEY"] = "mysecretkey"
app.config["RECAPTCHA_PUBLIC_KEY"] = '6Lfi1XcmAAAAAG6go6mUbSpX_01xHunP7wgn9StD'
app.config["RECAPTCHA_PRIVATE_KEY"] = '6Lfi1XcmAAAAANyI3-604hr8oKpQkRuH1A0XI9kw'

class Widgets(FlaskForm):
    recaptcha = RecaptchaField()

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
    form = Widgets()    
    return render_template('login.html', form=form)

@app.route('/criar_Projeto', methods=['GET'])
def criar_projeto():
    return render_template('criarProjeto.html')

#metodos 

@app.route('/authlogin', methods=['POST'])
def authlogin():
    recaptchaForm = Widgets()
    email = request.form.get('email')
    password = request.form.get('password')
    
    if dev.iniciaSessao(email, password) == False:
        print('Erro')
        return render_template('home.html')  # criar pagina de erro com para nova tentativa
    elif dev.iniciaSessao(email, password) == True and (recaptchaForm.validate() == False):
        flash("Por favor, marque o reCAPTCHA.")
    elif dev.iniciaSessao(email, password) == True and recaptchaForm.validate():
        flash("reCAPTCHA verificado com sucesso!")
        #return redirect('/home')
        print(email)
        #funcao pesquisar email na tabela de dev
        return render_template('pagina_inicial.html', nome=dev.getNome(email), sobrenome=dev.getSobrenome(email), descricao=dev.getDescricao(email))

@app.route('/pesquisa_usuario', methods=['POST'])
def pesquisaUser():
    pesquisa_user = request.form.get('pesquisa_user')
    
    if db.verificaUsuario(pesquisa_user) == True:
        return render_template('pagina_inicial.html', nome=db.getNome(pesquisa_user), sobrenome=dev.getSobrenome(email), descricao=dev.getDescricao(email))
    else:
        return render_template('pagina_inicial.html', nome=dev.getNome(email), sobrenome=dev.getSobrenome(email), descricao=dev.getDescricao(email))

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

@app.route('/criarProjeto', methods=['POST'])
def criarProjeto():
    nomeProjeto = request.form.get('nomeProjeto')
    nunDev = request.form.get('nunDev')
    tag = request.form.get('tag')
    descricao = request.form.get('descricao')
    return render_template('feed.html')
  
@app.route('/follow', methods=['POST'])
def follow():
    Id = request.json['Id']
    Usuario.Follow(Id)
    return jsonify(success=True)


@app.route('/unfollow', methods=['POST'])
def unfollow():
    Id = request.json['Id']
    Usuario.Unfollow(Id)
    return jsonify(success=True)

if __name__ == "__main__":
    app.run()


VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
