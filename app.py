from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_recaptcha import ReCaptcha
from Empresa import Empresa
from Desenvolvedor import Desenvolvedor
import requests
from datetime import datetime as dt
from flask_wtf import FlaskForm, RecaptchaField 



app = Flask(__name__,template_folder="templates")
app.config["SECRET_KEY"] = "mysecretkey"

app.config["RECAPTCHA_PUBLIC_KEY"] = '6Lfi1XcmAAAAAG6go6mUbSpX_01xHunP7wgn9StD'
app.config["RECAPTCHA_PRIVATE_KEY"] = '6Lfi1XcmAAAAANyI3-604hr8oKpQkRuH1A0XI9kw'

emp = Empresa()
dev = Desenvolvedor()
# dev.criaDesenvolvedor('dev@outlook.com', '(21)8573487509','joaozin123', '1234567')
class Widgets(FlaskForm):
    recaptcha = RecaptchaField()

##CODIGO DO OUTRO VIDEO USANDO O FORMS HTML 
# recaptcha = ReCaptcha(app=app)

# app.config.update(dict(
#     RECAPTCHA_ENABLED = True,
#     RECAPTCHA_SITE_KEY = "6Lfi1XcmAAAAAG6go6mUbSpX_01xHunP7wgn9StD",
#     RECAPTCHA_SECRET_KEY = "6Lfi1XcmAAAAANyI3-604hr8oKpQkRuH1A0XI9kw",
# ))

# recaptcha = ReCaptcha()
# recaptcha.init_app(app)

# app.config['SECRET_KEY'] = 'cairocoders-ednalan'

@app.route("/")
def home():
    form = Widgets()
    return render_template('home.html', form=form)



@app.route('/loginDesenvolvedor', methods=['POST'])
def logindev():
    secret_response = request.form['g-recaptcha-response']
    verify_response = requests.post(url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}')
    print(verify_response)

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


# @app.route('/register')
# def register():
#     return render_template("form.html")    

# @app.route('/submit', methods=['POST'])
# def submit():
#     if recaptcha.verify():
#         flash('New Device Added successfully')
#         return redirect(url_for('register'))
#     else:
#         flash('Error ReCaptcha')
#         return redirect(url_for('register'))
# if __name__ == '__main__':
#  app.run(debug=True)

app.run()

