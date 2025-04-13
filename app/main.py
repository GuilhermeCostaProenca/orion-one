import os
from flask import Flask, render_template, request, redirect
from app.memory import lembrar_comando, listar_comandos
from app.database import criar_banco

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, '..', 'static')  # << ADICIONE ESSA LINHA

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)  # << MODIFICADO
criar_banco()

@app.route('/')
def index():
    comandos = listar_comandos()
    return render_template('index.html', memoria=comandos)

@app.route('/enviar', methods=['POST'])
def enviar():
    comando = request.form['mensagem']
    lembrar_comando(comando)
    return redirect('/')

@app.route('/memoria')
def memoria():
    comandos = listar_comandos()
    return render_template('index.html', memoria=comandos)

if __name__ == '__main__':
    app.run(debug=True)
