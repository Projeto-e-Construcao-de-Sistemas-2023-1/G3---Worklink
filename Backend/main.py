from flask import Flask, render_template, request, redirect, url_for, abort
from Empresa import Empresa
from Desenvolvedor import Desenvolvedor
import requests
from flask_wtf import FlaskForm, RecaptchaField 



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

@app.route("/")
def home():
    form = Widgets()
    return render_template('home.html', form=form)

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

@app.route("/sign-user-in", methods=['POST'])
def sign_in_user():
    secret_response = request.form['g-recaptcha-response']
    print(request.form)
    verify_response = requests.post(url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}')
    print(verify_response)
    if verify_response['success'] == False:
        abort(401)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()

app.run()


SITE_KEY = ""
SECRET_KEY = ""
VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
