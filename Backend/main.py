from flask import Flask, render_template, request, redirect, url_for, abort, jsonify, flash
from Empresa import Empresa
from Database import Database
from Usuario import Usuario
from Desenvolvedor import Desenvolvedor
from flask_wtf import FlaskForm, RecaptchaField
import requests
from datetime import datetime as dt
from Evento import Evento
import sys
from Projeto import Projeto

app = Flask(__name__, template_folder="templates")
emailsessao=''
emp = Empresa()
evt = Evento()
dev = Desenvolvedor()
db = Database()
us=Usuario()
pjt = Projeto()
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
    if tipo == True:
        return render_template('editar_perfil.html', nome=dev.getNome(), contabancaria=dev.getConta(), sobrenome=dev.getSobrenome(), 
                           telefone=dev.getTelefone(), descricao=dev.getDescricao())
    
    else:
        return render_template('editar_perfil_emp.html', razaosocial=emp.getRazaoSocial(), contabancaria=emp.getConta(), 
                           telefone=emp.getTelefone(), descricao=emp.getAreaNegocio())

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
            global tipo # tipo == True desenvolvedor. tipo == false Empresa
            tipo=dev.verificaUsuario()
            if tipo:
                dev.capturaEmail(email)
                return redirect(url_for('feed'))
            else:
                emp.capturaEmail(email)
                return redirect(url_for('feed'))
        else:
            flash('***EMAIL OU SENHA INCORRETOS***')
            return redirect(url_for('login')) 

@app.route('/perfil', methods=['GET'])
def perfil():
   if tipo == True:
        return render_template('perfil_dev.html', nome=dev.getNome(), sobrenome=dev.getSobrenome(), descricao=dev.getDescricao(), email=dev.getEmail())
   else:
       return render_template('perfil_dev.html', nome=emp.getRazaoSocial(), descricao=emp.getAreaNegocio(), email=emp.getEmail())

@app.route('/criar_Projeto', methods=['GET'])
def criar_projeto():
    return render_template('criarProjeto.html')

@app.route('/feed', methods=['GET'])
def feed():
    if tipo == True:
        return render_template('pagina_inicial.html', nome=dev.getNome(), sobrenome=dev.getSobrenome(), descricao=dev.getDescricao())
    else:
        return render_template('pagina_inicial.html', nome=emp.getRazaoSocial(), descricao=emp.getAreaNegocio())

#metodos 
    
@app.route('/pesquisa_usuario', methods=['GET'])
def pesquisaUsuario():
    nome = request.form.get('nome')
    tipo = True
    resultado = Usuario().pesquisaUsuario(nome, tipo)
    return jsonify(resultado)
    #print(resultado)
    
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
    cep = request.form.get('cep')
    #confirm_password = request.form.get('confirm_password')
    area_negocio = request.form.get('area_negocio')

    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    if requisicao.status_code == 200:
        #funcao para o backend
        emp.criaEmpresa(cnpj, razao_social, email, telefone, conta, senha, area_negocio, cep)
        return render_template('home.html')
    else:
        flash("CEP inválido!")
        return redirect(url_for('regem'))

@app.route('/delete_conta', methods=['GET'])
def delete_conta():
    dev.deletaUsuario()
    return render_template('home.html')

@app.route('/edita_perfil', methods=['POST'])
def edita_perfil():
    if tipo == True:
        name = request.form.get('name')
        sobrenome = request.form.get('sobrenome')
        descricao = request.form.get('descricao')
        contabancaria = request.form.get('contabancaria')
        telefone = request.form.get('telefone')
        hashtags = request.form.get('hashtags')
        genero = request.form.get('genero')
        password = request.form.get('password')

        dev.setNome(name)
        dev.setSobrenome(sobrenome)
        dev.setDescricao(descricao)
        dev.setConta(contabancaria)
        dev.setTelefone(telefone)
        dev.setGenero(genero)
        dev.setTag(hashtags)
        dev.setSenha(password)

        return redirect(url_for('perfil'))

    else:
        contabancaria = request.form.get('contabancaria')
        telefone = request.form.get('telefone')
        password = request.form.get('password')
        areanegocio = request.form.get('areanegocio')
        razaosocial = request.form.get('razaosocial')

        emp.setRazaoSocial(razaosocial)
        emp.setConta(contabancaria)
        emp.setTelefone(telefone)
        emp.setAreaNegocio(areanegocio)
        emp.setSenha(password)

        return redirect(url_for('perfil'))

@app.route('/criarProjeto', methods=['POST'])
def criarProjeto():
    nomeProjeto = request.form.get('nomeProjeto')
    nunDev = request.form.get('nunDev')
    tag = request.form.get('tag')
    descricao = request.form.get('descricao')
    return render_template('perfil_dev.html')

@app.route("/get/", methods=["POST"])
def get():
    data = dict(request.form)
    if dev.verificaUsuario():
        events = evt.getEvento(int(data["month"]), int(data["year"]), dev.getCodigo(), True)
    else:
        events = evt.getEvento(int(data["month"]), int(data["year"]), emp.getCodigo(), False)
    # print(events)
    return "{}" if events is None else events

@app.route("/save/", methods=["POST"])
def save():
    data = dict(request.form)
    if dev.verificaUsuario():
        ok = evt.criaEventoDev(data["s"], data["e"], data["t"], data["c"], data["b"], dev.getCodigo(), True)
        us.enviarEmailReuniaoCriada(dev.getEmail(), dev.getNome(), data["s"])
    else:
        ok = evt.criaEventoEmp(data["s"], data["e"], data["t"], data["c"], data["b"], emp.getCodigo(), False)
        us.enviarEmailReuniaoCriada(emp.getEmail(), emp.getRazaoSocial(), data["s"])
    msg = "OK" 
    return 'Reunião criada com sucesso!'
    # if ok:
    #     return make_response(msg, 500)

@app.route("/delete/", methods=["POST"])
def delete():
  data = dict(request.form)
  ok = evt.deletaEvento(data["id"])
  if dev.verificaUsuario():
      us.enviarEmailReuniaoExcluida(dev.getEmail(), dev.getNome(), data["s"])
  else:
      us.enviarEmailReuniaoExcluida(emp.getEmail(), emp.getRazaoSocial(), data["s"])
  msg = "OK"
  return 'Reunião excluída com sucesso!' 
#   if ok:
#     #else sys.last_value
#     return make_response(msg, 500)

@app.route('/deposito', methods=['POST'])
def deposito():
    tipoUsuario = tipo
    if tipoUsuario:
        codUsuario = dev.getCodigo()
    else:
        codUsuario = emp.getCodigo()
    valor = request.form.get('valor')
    valor = valor.replace(',', '.')
    if Usuario().Depositar(tipoUsuario, codUsuario, valor):
        return jsonify({'message': 'Deposito realizado com sucesso'}), 200
    else:
        return jsonify({'message': 'Erro ao realizar deposito'}), 400

@app.route('/saque', methods=['POST'])
def saque():
    tipoUsuario = tipo
    if tipoUsuario:
        codUsuario = dev.getCodigo()
    else:
        codUsuario = emp.getCodigo()
    valor = request.form.get('valor')
    valor = valor.replace(',', '.')
    if Usuario().Sacar(tipoUsuario, codUsuario, valor):
        return jsonify({'message': 'Saque realizado com sucesso'}), 200
    else:
        return jsonify({'message': 'Erro ao realizar saque'}), 400

@app.route('/transacao', methods=['POST'])
def transacao():
    codEmpresa = emp.getCodigo()
    codDesenvolvedor = request.form.get('codDev')
    valor = request.form.get('valor')
    valor = valor.replace(',', '.')
    descricao = request.form.get('descricao')
    if Usuario().realizarTransacao(codEmpresa, codDesenvolvedor, valor, descricao):
        return jsonify({'message': 'Transacao realizado com sucesso'}), 200
    else:
        return jsonify({'message': 'Erro ao realizar transacao'}), 400


@app.route('/carteira', methods=['GET'])
def carteira():
    if tipo:
        saldo = Usuario().verificarSaldo(True, dev.getCodigo())
    else:
        saldo = Usuario().verificarSaldo(False, emp.getCodigo())
    return render_template('carteira.html', saldo=saldo)

@app.route('/listarusuarios', methods=['GET'])
def listar_usuarios():
    usuarios_tupla = Usuario.pesquisaUsuario()

if __name__ == "__main__":
    app.run()