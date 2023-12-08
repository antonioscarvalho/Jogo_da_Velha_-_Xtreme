#Classes - Projeto 4 - Jogo da Velha: Xtreme
branco = " "
token = ["X", "O"]

def __init__(self, board, mensagem, jogador, i, j):
        self.board = board
        self.mensagem = mensagem
        self.jogador = jogador
        self.i = i
        self.j = j

def criarTabuleiro(self):
        board = [
            [branco, branco, branco],
            [branco, branco, branco],
            [branco, branco, branco],
        ]
        return board


def printTabuleiro(self, board):
        for i in range(3):
            print("|".join(board[i]))
            if(i < 2):
                print("------")


def validarInput(self, mensagem):
        try:
            n = int(input(mensagem))
            if(n >= 1 and n <= 3):
                return n - 1
            else:
                print("Número precisa estar entre 1 e 3")
                return mensagem
        except:
            print("Numero nao valido")
            return mensagem


def aprovarMovimento(self, board, i , j):
        if(board[i][j] == branco):
            return True
        else:
            return False


def realizarMovimento(self, board, i, j, jogador):
        board[i][j] = token[jogador]


def vizualizarGanhador(self, board):
        # linhas 
        for i in range(3):
            if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != branco):
                return board[i][0]
        
        # coluna
        for i in range(3):
            if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != branco):
                return board[0][i]

        # diagonal principal
        if(board[0][0] != branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            return board[0][0]

        # diagonal secundaria
        if(board[0][2] != branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            return board[0][2]

        for i in range(3):
            for j in range(3):
                if(board[i][j] == branco):
                    return False

        return "EMPATE"