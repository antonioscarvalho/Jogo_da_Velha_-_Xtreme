#Workbench - Projeto 4 - Jogo da Velha: Xtreme
from jogo_da_velha import criarTabuleiro, realizarMovimento,  validarInput, printTabuleiro, vizualizarGanhador,  aprovarMovimento

from xtreme import movimentoIA

reset0 = 0

introduçãoJogo = print('''
Jogo da Velha: Xtreme
                       
Este jogo não é qualquer jogo da velha comum, pois nele você sempre perde ou empata, mas existem regras...

*Você nunca começa o jogo;
*É necessário que você seja sábio ao jogá-lo;
*A entidade Xtreme vai ser sua adversária sempre.                
                       
Ainda quer jogar? HAHAHAHAHAHAH''')
print('''
Para começar jogo, digite: "S"
Se não quer jogar, tchau, mas antes digite : "N"''')
soun = str(input()).rstrip().lstrip().upper()
print('''''')
if soun == 'S':
    name = str(input("Qual o nome do Jogador? "))
    print(f'''
Bem vindo, {name}!
''')
    age = int(input("Qual a sua idade? "))
    print(f'''
Sua idade é {age}, certo?[S/N]
''')
    sn = str(input('Confirme aqui: ')).rstrip().lstrip().upper()

    while reset0 != 'N':

        jogador = 0 # jogador 1
        board = criarTabuleiro()
        ganhador = vizualizarGanhador(board)
        while(not ganhador):
            print('''
Jogo começa:
''')
            print("===================")
            printTabuleiro(board)
            print("===================")
            if(jogador == 0):
                i,j = movimentoIA(board, jogador)
            else:
                i,j = movimentoIA(board, jogador)
                i = validarInput("Digite a linha: ")
                j = validarInput("Digite a coluna: ")
            
            if(aprovarMovimento(board, i, j)):
                realizarMovimento(board, i, j, jogador)
                jogador = (jogador + 1)%2
            else:
                print("A posicao informado ja esta ocupada")
            
            ganhador = vizualizarGanhador(board)
            print("===================")
            printTabuleiro(board)
            print("===================")
            print(f'''
Ganhador = {ganhador}
            ''')
            print("===================")
            print('Quer jogar novamente?')
        reset0 = str(input('Se sim, digite "S". Se não, digite "N": ')).rstrip().lstrip().upper()
        if reset0 == 'N':
            print('Seu jogo acaba aqui.')
else:
    print('Seu jogo acaba aqui.')