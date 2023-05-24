# Arquivo main para testes de funcionalidades das classes e do BD
from Desenvolvedor import Desenvolvedor
from Empresa import Empresa
 from flask import Flask, render_template, redirect, request

def main():
    dev1 = Desenvolvedor()
    dev1.setEmail()
if(__name__) == '__main__':
    main()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    print('email: ', email)
    print('senha', password)
    return redirect('/')
