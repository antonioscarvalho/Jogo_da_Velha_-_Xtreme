class Partida:
    def __init__(self):
        self.jogo = Jogo_da_Velha()

    def iniciarPartida(self):
        while True:
            self.jogo.introducaoJogo()
            resetar = input('Quer iniciar um novo jogo? (S para Sim, N para Não): ').strip().upper()
            if resetar != 'S':
                print('Obrigado por jogar!')
                break

class Jogo_da_Velha:
    def __init__(self):
        self.branco = " "
        self.token = ["X", "O"]
        self.board = self.criarTabuleiro()
        self.score = {"EMPATE": 0, "X": 1, "O": -1}
        self.jogador = 0  # jogador 1

    def criarTabuleiro(self):
        board = [[self.branco, self.branco, self.branco] for _ in range(3)]
        return board

    def printTabuleiro(self):
        for i in range(3):
            print("|".join(self.board[i]))
            if i < 2:
                print("------")

    def validarInput(self, mensagem):
        try:
            n = int(input(mensagem))
            if 1 <= n <= 3:
                return n - 1
            else:
                print("Número precisa estar entre 1 e 3.")
                return self.validarInput(mensagem)
        except ValueError:
            print("Esse número não é válido.")
            return self.validarInput(mensagem)

    def aprovarMovimento(self, i, j):
        if self.board[i][j] == self.branco:
            return True
        else:
            return False

    def realizarMovimento(self, i, j, jogador):
        self.board[i][j] = self.token[jogador]

    def visualizarGanhador(self):
        # Linhas
        for i in range(3):
            if (
                self.board[i][0] == self.board[i][1]
                and self.board[i][1] == self.board[i][2]
                and self.board[i][0] != self.branco
            ):
                return self.board[i][0]

        # Coluna
        for i in range(3):
            if (
                self.board[0][i] == self.board[1][i]
                and self.board[1][i] == self.board[2][i]
                and self.board[0][i] != self.branco
            ):
                return self.board[0][i]

        # Diagonal principal
        if (
            self.board[0][0] != self.branco
            and self.board[0][0] == self.board[1][1]
            and self.board[1][1] == self.board[2][2]
        ):
            return self.board[0][0]

        # Diagonal secundária
        if (
            self.board[0][2] != self.branco
            and self.board[0][2] == self.board[1][1]
            and self.board[1][1] == self.board[2][0]
        ):
            return self.board[0][2]

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.branco:
                    return False

        return "EMPATE"

    def movimentoIA(self):
        possibilidades = self.getPosicoes()
        melhor_valor = None
        melhor_movimento = None

        for possibilidade in possibilidades:
            self.board[possibilidade[0]][possibilidade[1]] = self.token[self.jogador]
            valor = self.xtreme(self.jogador)
            self.board[possibilidade[0]][possibilidade[1]] = self.branco

            if melhor_valor is None:
                melhor_valor = valor
                melhor_movimento = possibilidade
            elif self.jogador == 0:
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = possibilidade
            elif self.jogador == 1:
                if valor < melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = possibilidade

        return melhor_movimento[0], melhor_movimento[1]

    def getPosicoes(self):
        posicoes = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.branco:
                    posicoes.append([i, j])

        return posicoes

    def xtreme(self, jogador):
        ganhador = self.visualizarGanhador()
        if ganhador:
            return self.score[ganhador]
        jogador = (jogador + 1) % 2

        possibilidades = self.getPosicoes()
        melhor_valor = None

        for possibilidade in possibilidades:
            self.board[possibilidade[0]][possibilidade[1]] = self.token[jogador]
            valor = self.xtreme(jogador)
            self.board[possibilidade[0]][possibilidade[1]] = self.branco

            if melhor_valor is None:
                melhor_valor = valor
            elif jogador == 0:
                if valor > melhor_valor:
                    melhor_valor = valor
            elif jogador == 1:
                if valor < melhor_valor:
                    melhor_valor = valor

        return melhor_valor

    def introducaoJogo(self):
        ganhador = self.visualizarGanhador()
        jogador = 0
        self.jogo = Jogo_da_Velha()
        ganhador = self.jogo.visualizarGanhador()
        while not ganhador:
            print("===================")
            self.jogo.printTabuleiro()
            print("===================")
            if jogador == 0:
                i, j = self.jogo.movimentoIA()
            else:
                i = self.jogo.validarInput("Digite a linha: ")
                j = self.jogo.validarInput("Digite a coluna: ")

            if self.jogo.aprovarMovimento(i, j):
                self.jogo.realizarMovimento(i, j, jogador)
                jogador = (jogador + 1) % 2
            else:
                print("A posição informada já está ocupada")

            ganhador = self.jogo.visualizarGanhador()
            print("===================")
            self.jogo.printTabuleiro()
            print("===================")
            print(f'''
Ganhador = {ganhador}
                ''')
            print("===================")
partida = Partida()
partida.iniciarPartida()