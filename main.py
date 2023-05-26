# Arquivo main para testes de funcionalidades das classes e do BD
from Desenvolvedor import Desenvolvedor
from Empresa import Empresa
from flask import Flask, render_template, redirect, request, abort
from Usuario import Usuario
#import requests 
emp = Empresa()
dev = Desenvolvedor()
dev.conectaBD()
app = Flask(__name__)
@app.route('/')
def main(self): 
        usuario = Usuario()
        usuario.conectaBD()

def home():
        return render_template('login.html', site_key=SITE_KEY)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # SE FOR INICIAR SESSAO COMO DESENVOLVEDOR
    dev.iniciaSessao(email, password)
    # SE FOR INICIAR SESSAO COMO EMPRESA
    emp.iniciaSessao(email, password)
    if dev.iniciaSessao(email, password) == True:
        # Avançar de página
        print('Passei!')
        pass
    else:
        print('Erro')
        # Printar erro
        pass
    return redirect('/')

@app.route("/sign-user-in", methods=['POST'])
def sign_in_user():
    secret_response = request.form['g-recaptcha-response']
    print(request.form)
    verify_response = requests.post(url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}')

    print(verify_response)

    if verify_response['success'] == False:
        abort(401)

    return redirect(url_for('home'))
                       

    #return redirect(url_for('home'))


SITE_KEY = '6LeKBj8mAAAAAA3jCMVID2PjUUYmIM1TYOIKf3Ei'
SECRET_KEY ='6LeKBj8mAAAAAAIsJpHljREaS2EPF8y5uw2frJHA'
VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'

