from flask import Flask, render_template, request, redirect, url_for, abort, jsonify, flash
from Empresa import Empresa
from Database import Database
from Usuario import Usuario
from Desenvolvedor import Desenvolvedor
from flask_wtf import FlaskForm, RecaptchaField
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
    return render_template('editar_perfil.html', nome=dev.getNome(), contabancaria=dev.getConta(), sobrenome=dev.getSobrenome(), 
                           telefone=dev.getTelefone(), descricao=dev.getDescricao(), tag=dev.getTag()) 

@app.route('/signup_dev', methods=['GET'])
def regdv():
    return render_template('RegisterDesenvolvedor.html') 

@app.route('/signup_emp', methods=['GET'])
def regem():
    return render_template('RegisterEmpresa.html')

@app.route('/authlogin', methods=['GET', 'POST'])
def login():
    form = Widgets()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            flash('Por favor, preencha todos os campos.')
            return redirect(url_for('login'))
        
        elif 'g-recaptcha-response' not in request.form:
            flash('Por favor, marque a caixa de verificação reCaptcha.')
            return redirect(url_for('login'))
        
        elif dev.iniciaSessao(email, password):
            dev.capturaEmail(email)
            dev.verificaUsuario()
            return redirect(url_for('feed'))
        else:
            flash('***EMAIL OU SENHA INCORRETOS***')
            return redirect(url_for('login'))

@app.route('/perfil', methods=['GET'])
def perfildev():
   return render_template('perfil_dev.html', nome=dev.getNome(), sobrenome=dev.getSobrenome(), descricao=dev.getDescricao(), email=dev.getEmail(), tag=dev.getTag())

@app.route('/criar_Projeto', methods=['GET'])
def criar_projeto():
    return render_template('criarProjeto.html')

@app.route('/feed', methods=['GET'])
def feed():
    return render_template('pagina_inicial.html', nome=dev.getNome(), sobrenome=dev.getSobrenome(), descricao=dev.getDescricao())
#metodos 
    
@app.route('/pesquisa_usuario', methods=['post'])
def pesquisaUser():
    pesquisa_user = request.form.get('pesquisa_user')
    print(pesquisa_user)
    
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
        return redirect(url_for('home'))
    
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

@app.route('/delete_conta', methods=['GET'])
def delete_conta():
    dev.deletaUsuario()
    return render_template('home.html')

@app.route('/edita_perfil', methods=['POST'])
def edita_perfil():
    name = request.form.get('name')
    sobrenome = request.form.get('sobrenome')
    descricao = request.form.get('descricao')
    contabancaria = request.form.get('contabancaria')
    telefone = request.form.get('telefone')
    tag = request.form.get('tag')
    genero = request.form.get('genero')
    password = request.form.get('password')
  

    dev.setNome(name)
    dev.setSobrenome(sobrenome)
    dev.setDescricao(descricao)
    dev.setConta(contabancaria)
    dev.setTelefone(telefone)
    dev.setGenero(genero)
    dev.setTag(tag)
    dev.setSenha(password)

    return redirect(url_for('perfildev'))

@app.route('/criarProjeto', methods=['POST'])
def criarProjeto():
    nomeProjeto = request.form.get('nomeProjeto')
    nunDev = request.form.get('nunDev')
    tag = request.form.get('tag')
    descricao = request.form.get('descricao')
    return render_template('perfil_dev.html')
  
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

@app.route("/calendario", methods=["GET", "POST"])
def index():
  return render_template("S4A_calendar.html")


if __name__ == "__main__":
    app.run()

VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"