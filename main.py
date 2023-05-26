# Arquivo main para testes de funcionalidades das classes e do BD
from Desenvolvedor import Desenvolvedor
from Empresa import Empresa
from flask import Flask, render_template, redirect, request
from Usuario import Usuario

emp = Empresa()
dev = Desenvolvedor()
dev.conectaBD()
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')

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