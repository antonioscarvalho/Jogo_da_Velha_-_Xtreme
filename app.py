import bottle
from bottle import template, request, redirect

from backend.jogo_da_velha import Partida, Jogo_da_Velha
from database.db import validar_usuario, cadastrar_usuario

app = bottle.Bottle()
partida = Partida()
historico_partidas = []

@app.route('/')
def index():
    return template('frontend/index.tpl')


@app.route('/entrar', method=['GET', 'POST'])
def desktop_2():
    resultado_validacao = None
    if request.method == 'POST':
        resultado_validacao = validar_usuario(request.forms.get('usuario'), request.forms.get('senha'))

        if resultado_validacao == "Usuário válido.":
            return redirect('/jogar')

    return template('frontend/entrar.tpl', resultado_validacao=resultado_validacao)

@app.route('/cadastrar', method=['GET', 'POST'])
def desktop_3():
    if request.method == 'POST':
        nome_usuario = request.forms.get('usuario')
        senha_usuario = request.forms.get('senha')
        cadastrar_usuario(nome_usuario, senha_usuario)
        return redirect('/jogar')

    return template('frontend/cadastrar.tpl')

@app.route('/jogar', method=['GET', 'POST'])
def introducaoJogo_route():
    global partida
    if request.method == 'POST':
        jogador = int(request.forms.get('jogador'))
        i = int(request.forms.get('i'))
        j = int(request.forms.get('j'))

        resultados = partida.jogo.introducaoJogo(jogador, i, j)
        return template("jogar.tpl", resultados=resultados)

@app.route('/partida')
def iniciarPartida_route():
    resultados = partida.iniciarPartida()
    return template("iniciarPartida.tpl", resultados=resultados)

@app.route('/partida/criarTabuleiro')
def criarTabuleiro_route():
    return template("criarTabuleiro", criarTabuleiro=criarTabuleiro)

@app.route('/partida/printTabuleiro')
def printTabuleiro_route():
    return template("printTabuleiro", printTabuleiro=printTabuleiro)

@app.route('/partida/validarInput')
def validarInput_route():
    return template("validarInput", validarInput=validarInput)

@app.route('/partida/aprovarMovimento')
def aprovarMovimento_route():
    return template("aprovarMovimento", aprovarMovimento=aprovarMovimento)

@app.route('/partida/realizarMovimento', method='POST')
def realizarMovimento_route():
    i = int(request.forms.get('i'))
    j = int(request.forms.get('j'))
    jogador = int(request.forms.get('jogador'))
    partida.jogo.realizarMovimento(i, j, jogador)
    return template("realizarMovimento.tpl")

@app.route('/partida/movimentoIA')
def movimentoIA_route():
    return template("movimentoIA", movimentoIA=movimentoIA)

@app.route('/partida/getPosicoes')
def getPosicoes_route():
    return template("getPosicoes", getPosicoes=getPosicoes)

@app.route('/partida/xtreme')
def xtreme_route():
    return template("xtreme", xtreme=xtreme)

@app.route('/resultado')
def visualizarGanhador_route():
    return template("visualizarGanhador.tpl", visualizarGanhador=visualizarGanhador)

def resultado_route():
    global historico_partidas
    if historico_partidas:
        resultado_ultima_partida = historico_partidas[-1]
    else:
        resultado_ultima_partida = "Nenhuma partida foi jogada ainda."

    return template("resultado.tpl", resultado=resultado_ultima_partida)

@app.route('/historico')
def historico_route():
    global historico_partidas
    return template("historico.tpl", historico=historico_partidas)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)