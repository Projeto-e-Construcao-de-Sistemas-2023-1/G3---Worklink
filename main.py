# Arquivo main para testes de funcionalidades das classes e do BD
from Desenvolvedor import Desenvolvedor
from Empresa import Empresa
from flask import Flask, render_template, redirect, request
from Usuario import Usuario

app = Flask(__name__)
def main():
    dev = Desenvolvedor()
    #home()
    #login(dev, empresa)
    dev.conectaBD()
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login(dev, empresa):
    email = request.form.get('email')
    password = request.form.get('password')
    if dev.iniciaSessao(email, password) == True:
        # Avançar de página
        print('Passei!')
        pass
    else:
        print('Erro')
        # Printar erro
        pass
    return redirect('/')

if(__name__) == '__main__':
    main()
