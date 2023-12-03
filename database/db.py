# Banco de Dados - Projeto 4 - Jogo da Velha: Xtreme

import json

banco_de_dados = []

def carregar_banco_de_dados():
    try:
        with open("db.json", "r") as arquivo_json:
            return json.load(arquivo_json)
    except FileNotFoundError:
        return []

def adicionar_usuario(nome, senha):
    usuario = {"nome": nome, "senha": senha}
    banco_de_dados.append(usuario)
    print("Usuário cadastrado com sucesso!")

def exibir_usuarios():
    if not banco_de_dados:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in banco_de_dados:
            print(f"Nome: {usuario['nome']}, Senha: {usuario['senha']}")

def salvar_banco_de_dados():
    with open("db.json", "w") as arquivo_json:
        json.dump(banco_de_dados, arquivo_json)

banco_de_dados = carregar_banco_de_dados()

while True:
    print("\nMenu:")
    print("1. Cadastrar usuário")
    print("2. Mostrar usuários cadastrados")
    print("3. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        nome_usuario = input("Digite o nome do usuário: ")
        senha_usuario = input("Digite a senha do usuário: ")
        adicionar_usuario(nome_usuario, senha_usuario)
        salvar_banco_de_dados()  # Salvar dados após adicionar usuário
    elif escolha == "2":
        print("Usuários no banco de dados:")
        exibir_usuarios()
    elif escolha == "3":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
