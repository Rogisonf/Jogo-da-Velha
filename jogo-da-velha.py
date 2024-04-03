class TicTacToe:
    def __init__(self):
        self.board = ["-"] * 9
        self.current_winner = None  # Track the winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == "-"]

    def make_move(self, position, player):
        if self.board[position] == "-" and position in range(9):
            self.board[position] = player
            if self.check_winner()[0]:
                self.current_winner = player
                return True
            return False
        return False

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for cond in win_conditions:
            if self.board[cond[0]] == self.board[cond[1]] == self.board[cond[2]] != "-":
                # Atualiza o vencedor atual
                self.current_winner = self.board[cond[0]]
                return True, self.board[cond[0]]  # Retorna True e o vencedor

        # Verifica empate apenas se não houver vencedor
        if "-" not in self.board:
            return True, "Tie"  # Indica empate
        return False, None  # Jogo ainda em andamento

    def minimax(self, is_maximizing):
        # Ajuste para capturar ambos os valores retornados
        game_over, winner = self.check_winner()
        if game_over:
            if winner == 'O':
                return {'position': None, 'score': -1}  # Máquina ('O') ganhou
            elif winner == 'X':
                return {'position': None, 'score': 1}   # Jogador ('X') ganhou
            else:
                return {'position': None, 'score': 0}   # Empate

        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for move in self.available_moves():
                self.board[move] = 'X'  # Tenta a jogada como 'X'
                score = self.minimax(False)['score']
                self.board[move] = '-'  # Desfaz a jogada
                if score > best_score:
                    best_score = score
                    best_move = move
            return {'position': best_move, 'score': best_score}
        else:
            best_score = float('inf')
            best_move = None
            for move in self.available_moves():
                self.board[move] = 'O'  # Tenta a jogada como 'O'
                score = self.minimax(True)['score']
                self.board[move] = '-'  # Desfaz a jogada
                if score < best_score:
                    best_score = score
                    best_move = move
            return {'position': best_move, 'score': best_score}


def play_game(game):
    player = 'X'  # X sempre começa
    while True:
        game.print_board()

        game_over, winner = game.check_winner()
        if game_over:
            if winner == "Tie":
                print("O jogo terminou em empate!")
            else:
                print(f"O jogador {winner} venceu!")
            break

        if player == 'X':  # Vez do jogador humano
            while True:  # Garante que o jogador escolha uma posição válida
                try:
                    position = int(input("\nSua vez (0-8): "))
                    if position in game.available_moves():
                        game.make_move(position, player)
                        break
                    else:
                        print("Posição inválida ou já ocupada. Tente novamente.")
                except ValueError:
                    print("Por favor, insira um número válido.")

        else:  # Vez da máquina
            print("\nVez da máquina:")
            # False porque 'O' é o minimizador no seu contexto
            result = game.minimax(False)
            if result['position'] is not None:
                game.make_move(result['position'], 'O')
                print(f"Máquina jogou em: {result['position']}")
            else:
                print("Jogo ainda em andamento.")

        player = 'O' if player == 'X' else 'X'  # Troca de jogador


game = TicTacToe()
play_game(game)
