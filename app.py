from bottle import Bottle, run, template, request, redirect
from database.db import validar_usuario, cadastrar_usuario

app = Bottle()

@app.route('/')
def entrar():
    return template('frontend/desktop_1.tpl')

@app.route('/validar_usuario', method='POST')
def validar_usuario_route():
    resultado_validacao = ''
    nome_usuario = request.forms.get('usuario')
    senha_usuario = request.forms.get('senha')
    resultado_validacao = validar_usuario(nome_usuario, senha_usuario)
    
    if resultado_validacao == "Usuário válido.":
        redirect('/desktop_4')
    
    return template('frontend/desktop_2.tpl', resultado_validacao=resultado_validacao)

@app.route('/desktop_3')
def desktop_3():
    return template('frontend/desktop_3.tpl')

@app.route('/desktop_4')
def desktop_4():
    return template('frontend/desktop_4.tpl')

@app.route('/cadastrar_usuario', method='POST')
def cadastrar_usuario_route():
    nome_usuario = request.forms.get('usuario')
    senha_usuario = request.forms.get('senha')
    cadastrar_usuario(nome_usuario, senha_usuario)
    redirect('/desktop_4')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)