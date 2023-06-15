# Arquivo main para testes de funcionalidades das classes e do BD
from Desenvolvedor import Desenvolvedor
from Empresa import Empresa
from Database import Database
import S2_lib as evt
from flask import Flask, render_template, redirect, request, abort, url_for
import requests
from datetime import datetime as dt

app = Flask(__name__, template_folder="templates")

emp = Empresa()
dev = Desenvolvedor()
# dev.criaDesenvolvedor('desenvolvedor', 'senior', '19828347589', 'dev@outlook.com', 'masculino', '2000/12/12', '(21)8573487509', '12345678901',
#                       'senha', 'python')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/loginDesenvolvedor', methods=['POST'])
def logindev():
    secret_response = request.form['g-recaptcha-response']
    verify_response = requests.post(url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}')
    print(verify_response)


@app.route('/loginEmpresa', methods=['GET', 'POST'])
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
    return redirect('/')  # aqui o final do antigo codigo


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

@app.route("/calendario", methods=["GET", "POST"])
def index():
  return render_template("S4A_calendar.html")

if __name__ == "__main__":
    app.run()


# SITE_KEY = "6LeKBj8mAAAAAA3jCMVID2PjUUYmIM1TYOIKf3Ei"
# SECRET_KEY = "6LeKBj8mAAAAAAIsJpHljREaS2EPF8y5uw2frJHA"
# VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
