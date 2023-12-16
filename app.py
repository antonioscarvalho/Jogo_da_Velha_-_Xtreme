import bottle
from bottle import template, request, redirect

from backend.jogo_da_velha import Partida, Jogo_da_Velha
from database.db import validar_usuario, cadastrar_usuario, historico_partidas

app = bottle.Bottle()
partida = Partida()

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def entrar():
    return template('frontend/desktop_1.tpl')

@app.route('/desktop_2')
def desktop_2():
    return template('frontend/desktop_2.tpl')

@app.route('/desktop_3')
def desktop_3():
    return template('frontend/desktop_3.tpl')

@app.route('/desktop_4')
def desktop_4():
    return template('frontend/desktop_4.tpl')

@app.route('/desktop_5')
def desktop_5():
    return template('frontend/desktop_5.tpl')

@app.route('/desktop_6')
def desktop_6():
    return template('frontend/desktop_6.tpl')

@app.route('/desktop_9')
def desktop_9():
    return template('frontend/desktop_9.tpl')

@app.route('/validar_usuario', method='POST')
def validar_usuario_route():
    resultado_validacao = ''
    nome_usuario = request.forms.get('usuario')
    senha_usuario = request.forms.get('senha')
    resultado_validacao = validar_usuario(nome_usuario, senha_usuario)
    
    if resultado_validacao == "Usuário válido.":
        redirect('/desktop_4')
    
    return template('frontend/desktop_2.tpl', resultado_validacao=resultado_validacao)

@app.route('/cadastrar_usuario', method='POST')
def cadastrar_usuario_route():
    nome_usuario = request.forms.get('usuario')
    senha_usuario = request.forms.get('senha')
    cadastrar_usuario(nome_usuario, senha_usuario)
    redirect('/desktop_4')

#functions

@app.route('/jogar', method='POST')
def jogar_route():
    global partida
    partida.iniciarPartida()
    return template('frontend/desktop_5.tpl')

@app.route('/resultado', method='GET')
def resultado_route():
    global historico_partidas
    if historico_partidas:
        resultado_ultima_partida = historico_partidas[-1]
    else:
        resultado_ultima_partida = "Nenhuma partida foi jogada ainda."

    return template("resultado", resultado=resultado_ultima_partida)

@app.route('/historico', method='POST')
def historico_route():
    global historico_partidas
    return template("historico", historico=historico_partidas)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

