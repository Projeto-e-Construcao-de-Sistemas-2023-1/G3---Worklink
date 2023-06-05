# Arquivo main para testes de funcionalidades das classes e do BD
from Desenvolvedor import Desenvolvedor
from Empresa import Empresa
from flask import Flask, render_template, redirect, request, requests, abort, url_for

emp = Empresa()
dev = Desenvolvedor()
dev.conectaBD()
dev.criaDesenvolvedor('dev@email.com', '21989212222', '123456789', '12345', 'desenvolvedor', 'pleno', 'nb', 'java',
                      '12345678900', '12/12/1995')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/loginDesenvolvedor', methods=['POST'])
def logindev():
    email = request.form.get('email')
    password = request.form.get('password')
    if dev.iniciaSessao(email, password) == True:
        return render_template('feed.html')
        # Avançar de página
        print('Passei!')
        pass
    else:
        print('Erro')
        return render_template('index.html')  # criar pagina de erro com para nova tentativa
        # Printar erro
        pass
@app.route('/registerDesenvolvedor', methods=['POST'])
def regdev():
   return render_template('RegisterDesenvolvedor.html')
  
@app.route('/registerEmpresa', methods=['POST'])
def regdev():
   return render_template('RegisterEmpresa.html')

@app.route('/loginEmpresa', methods=['POST'])
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


SITE_KEY = "6LeKBj8mAAAAAA3jCMVID2PjUUYmIM1TYOIKf3Ei"
SECRET_KEY = "6LeKBj8mAAAAAAIsJpHljREaS2EPF8y5uw2frJHA"
VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
