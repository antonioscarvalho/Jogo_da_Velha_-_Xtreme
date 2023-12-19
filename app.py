from bottle import Bottle, run, template, request, redirect
from database.db import validar_usuario, cadastrar_usuario

app = Bottle()

@app.route('/')
def entrar():
    return template('frontend/desktop_1.tpl')

@app.route('/desktop_2', method='GET')
def desktop_2():
    return template('frontend/desktop_2.tpl', resultado_validacao='')

@app.route('/desktop_3', method='GET')
def desktop_3():
    return template('frontend/desktop_3.tpl')

@app.route('/desktop_4', method='GET')
def desktop_4():
    return template('frontend/desktop_4.tpl')

@app.route('/desktop_5', method='GET')
def desktop_5():
    return template('frontend/desktop_5.tpl')

@app.route('/desktop_6', method='GET')
def desktop_6():
    return template('frontend/desktop_6.tpl')

@app.route('/desktop_9', method='GET')
def desktop_9():
    return template('frontend/desktop_9.tpl')

@app.route('/validar_usuario', method='POST')
def validar_usuario_route():
    resultado_validacao = validar_usuario(request.forms.get('usuario'), request.forms.get('senha'))
    return template('frontend/desktop_2.tpl', resultado_validacao=resultado_validacao)

@app.route('/cadastrar_usuario', method=['GET', 'POST'])
def cadastrar_usuario_route():
    if request.method == 'POST':
        nome_usuario = request.forms.get('usuario')
        senha_usuario = request.forms.get('senha')
        cadastrar_usuario(nome_usuario, senha_usuario)
        redirect('/desktop_4')
    else:
        return template('frontend/desktop_3.tpl')

@app.route('/jogar', method='POST')
def jogar_route():
    partida = Partida()
    partida.iniciarPartida()
    redirect('/desktop_5')

@app.route('/resultado', method='GET')
def resultado_route():
    global historico_partidas
    if historico_partidas:
        resultado_ultima_partida = historico_partidas[-1]
    else:
        resultado_ultima_partida = "Nenhuma partida foi jogada ainda."

    return template("resultado", resultado=resultado_ultima_partida)

@app.route('/historico', method='GET')
def historico_route():
    global historico_partidas
    return template("historico", historico=historico_partidas)

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)