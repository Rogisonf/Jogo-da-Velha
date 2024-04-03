from collections import deque
import random


class TicTacToe:
    def _init_(self):
        self.board = ["-"] * 9  # Inicializa o tabuleiro com 9 espaços vazios
        self.current_winner = None  # Mantém o controle do vencedor

    def print_board(self):
        # Imprime o tabuleiro
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Retorna uma lista de índices de movimentos válidos
        return [i for i, spot in enumerate(self.board) if spot == "-"]

    def check_winner(self):
        # Linhas, colunas e diagonais para verificar
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
            (0, 4, 8), (2, 4, 6)             # Diagonais
        ]
        for cond in win_conditions:
            if self.board[cond[0]] == self.board[cond[1]] == self.board[cond[2]] != "-":
                self.current_winner = self.board[cond[0]]
                return True
        return False

    def random_move(self, player):
        available = self.available_moves()
        if len(available) > 0:
            position = random.choice(available)
            self.make_move(position, player)
            return True
        return False

    def make_move(self, position, player):
        if self.board[position] == "-" and position in range(9):
            self.board[position] = player
            if self.check_winner():
                print(f"O jogador {player} venceu!")
                return True
            return False
        else:
            print("Movimento inválido. Tente novamente.")
            return False

    # Adicione mais métodos conforme necessário (ex: fazer uma jogada, verificar vitória)


def get_next_states(state):
    # Aqui, state poderia ser a representação do tabuleiro do jogo da velha,
    # por exemplo, uma lista de 9 elementos.
    # Esta função deve retornar uma lista de estados que são alcançáveis
    # a partir do estado atual com uma única jogada.

    next_states = []
    for i in range(9):  # Considerando um tabuleiro de 3x3
        if state[i] == '-':  # Se a posição está vazia
            # Exemplo de adicionar 'X' na posição vazia
            next_state = state[:i] + 'X' + state[i+1:]
            next_states.append(next_state)

    return next_states


def play_game(game):
    player = 'X'  # O jogador humano começa.
    while True:
        game.print_board()  # Imprime o tabuleiro no início de cada turno
        if player == 'X':
            print("\nSua vez:")
            position = input("Escolha uma posição de 0 a 8: ")
            try:
                position = int(position)
                if position not in game.available_moves():
                    print("Essa posição já está ocupada ou é inválida. Tente outra.")
                    continue
                if game.make_move(position, player):
                    if game.current_winner:
                        game.print_board()
                        print(f"O jogador {player} venceu!")
                        break
            except ValueError:
                print("Por favor, insira um número válido.")
                continue
        else:
            print("\nVez da máquina:")
            game.random_move('O')  # Garante que a máquina jogue com 'O'

        # Troca de jogador após cada jogada válida
        player = 'O' if player == 'X' else 'X'

        # Verifica se o tabuleiro está cheio para declarar empate
        if '-' not in game.board:
            game.print_board()
            print("Empate!")
            break


# Exemplo de como iniciar um jogo
game = TicTacToe()
play_game(game)


https://www.canva.com/design/DAGBUaRaw5Y/SFM2qmeXUCTeG-ZAlLNB6w/edit?utm_content=DAGBUaRaw5Y&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
