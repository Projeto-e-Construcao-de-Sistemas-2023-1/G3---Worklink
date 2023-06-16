from flask import Flask, render_template, request, redirect, url_for, abort, jsonify, flash
from Empresa import Empresa
from Desenvolvedor import Desenvolvedor
import requests
from flask_wtf import FlaskForm, RecaptchaField 
import Usuario



app = Flask(__name__,template_folder="templates", static_folder= "styles")
app.config["SECRET_KEY"] = "mysecretkey"
app.config["RECAPTCHA_PUBLIC_KEY"] = '6Lfi1XcmAAAAAG6go6mUbSpX_01xHunP7wgn9StD'
app.config["RECAPTCHA_PRIVATE_KEY"] = '6Lfi1XcmAAAAANyI3-604hr8oKpQkRuH1A0XI9kw'

emp = Empresa()
dev = Desenvolvedor()
resposta = dev.setSenha('senha_nova', 'dev@outlook.com')
print(resposta)

class Widgets(FlaskForm):
    recaptcha = RecaptchaField()

#Rotas
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Widgets()
    if request.method == 'POST':
        if form.validate():
            # Verifica se o recaptcha foi marcado corretamente
            flash("reCAPTCHA verificado com sucesso!")
            
            # verificar usuario e senha aqui
            return redirect('/home')
        else:
            flash("Por favor, marque o reCAPTCHA.")
    
    return render_template('login.html', form=form)



@app.route('/editar_perfil', methods=['GET'])
def editarp():
    return render_template('editar_perfil.html') 

@app.route('/signup_dev', methods=['GET'])
def regdv():
    return render_template('RegisterDesenvolvedor.html') 

@app.route('/signup_emp', methods=['GET'])
def regem():
    return render_template('RegisterEmpresa.html') 

@app.route('/criar_Projeto', methods=['GET'])
def criar_projeto():
    return render_template('criarProjeto.html')

#metodos 

@app.route('/authlogin', methods=['POST'])
def authlogin():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if dev.iniciaSessao(email, password) == True:
        print(email)
        emailsessao=email
        #funcao pesquisar email na tabela de dev
        return render_template('pagina_inicial.html', emailsessao=dev.getNome(email))
    else:
        print('Erro')
        return render_template('home.html')  # criar pagina de erro com para nova tentativa

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

@app.route('/loginDesenvolvedor', methods=['POST'])
def logindev():
    secret_response = request.form['g-recaptcha-response']
    verify_response = requests.post(url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}')
    print(verify_response)
    
@app.route('/loginempresa', methods=['POST'])
def loginemp():
    email = request.form.get('email')
    password = request.form.get('password')
    if emp.iniciaSessao(email, password) == True:
        return render_template('feed.html')
        # Avançar de página
        print('Passei!')
        pass
    else:
        print('Erro')
        return render_template('index.html')  # criar pagina de erro com para nova tentativa
        # Printar erro
        pass
    return redirect('/')  # aqui o final do antigo cofigo


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

if __name__ == "__main__":
    app.run()

app.run()

