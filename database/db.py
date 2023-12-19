# Banco de Dados - Projeto 4 - Jogo da Velha: Xtreme
import os
import json
from bottle import Bottle, run, request, template

app = Bottle()

script_directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_directory, 'db.json')

def carregar_banco_de_dados():
    try:
        with open(db_path, "r") as arquivo_json:
            conteudo = arquivo_json.read()
            if not conteudo:
                return []
            return json.loads(conteudo)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        print("Erro de decodificação JSON. O arquivo pode estar corrompido.")
        return []

def adicionar_usuario(nome, senha):
    usuario = {"nome": nome, "senha": senha}
    banco_de_dados.append(usuario)
    print("Usuário cadastrado com sucesso!")

def exibir_usuarios():
    if not banco_de_dados:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(banco_de_dados, 1):
            print(f"{i}. Nome: {usuario['nome']}, Senha: {usuario['senha']}")

def excluir_usuario(nome=None, senha=None):
    if nome is None:
        nome_usuario = input("Digite o nome do usuário a ser excluído: ")
        senha_usuario = input("Digite a senha do usuário: ")
    else:
        nome_usuario = nome

    global banco_de_dados
    usuario_encontrado = next((usuario for usuario in banco_de_dados if usuario["nome"] == nome_usuario), None)

    if usuario_encontrado:
        if senha is None:
            senha_usuario = input("Digite a senha do usuário para confirmar a exclusão: ")

        if senha_usuario == usuario_encontrado["senha"]:
            banco_de_dados = [usuario for usuario in banco_de_dados if usuario["nome"] != nome_usuario]
            print("Usuário excluído com sucesso!")
            salvar_banco_de_dados()
        else:
            print("Senha incorreta. A exclusão do usuário foi cancelada.")
    else:
        print("Usuário não encontrado.")

def salvar_banco_de_dados():
    with open(db_path, "w") as arquivo_json:
        json.dump(banco_de_dados, arquivo_json)

def validar_usuario(nome=None, senha=None):
    if nome is None:
        nome_usuario = request.forms.get("usuario")
        senha_usuario = request.forms.get("senha")
    else:
        nome_usuario = nome
        senha_usuario = senha

    for usuario in banco_de_dados:
        if usuario["nome"] == nome_usuario and usuario["senha"] == senha_usuario:
            return "Usuário válido."

    return "Usuário inválido."

def cadastrar_usuario(nome, senha):
    adicionar_usuario(nome, senha)
    salvar_banco_de_dados()

def mostrar_usuarios_cadastrados():
    print("Usuários no banco de dados:")
    exibir_usuarios()

@app.route('/desktop_2', method='POST')
def desktop_2():
    resultado_validacao = validar_usuario()
    return template("desktop_2", resultado_validacao=resultado_validacao)

banco_de_dados = carregar_banco_de_dados()