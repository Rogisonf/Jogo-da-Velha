from collections import deque

class TicTacToe:
    def _init_(self):
        self.board = ["-"] * 9
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == "-"]

    def make_move(self, move, player):
        self.board[move] = player

    def check_winner(self):
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


def get_next_states(state, player):
    next_states = []
    for i in range(9):
        if state[i] == '-':
            next_state = state[:i] + player + state[i+1:]
            next_states.append(next_state)
    return next_states


def bfs(initial_state, player):
    visited = set()
    queue = deque([initial_state])

    while queue:
        state = queue.popleft()
        visited.add(state)

        for next_state in get_next_states(state, player):
            if next_state not in visited:
                queue.append(next_state)
    return visited


def dfs(initial_state, player, visited=None):
    if visited is None:
        visited = set()

    visited.add(initial_state)

    for next_state in get_next_states(initial_state, player):
        if next_state not in visited:
            dfs(next_state, player, visited)
    return visited


def human_vs_human():
    game = TicTacToe()
    current_player = "X"
    while not game.check_winner() and "-" in game.board:
        game.print_board()
        move = int(input(f"Player {current_player}, choose your move (0-8): "))
        if game.board[move] == "-":
            game.make_move(move, current_player)
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move! Try again.")
    game.print_board()
    winner = game.current_winner
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")


def human_vs_algorithm(algorithm):
    game = TicTacToe()
    current_player = "X"
    while not game.check_winner() and "-" in game.board:
        if current_player == "X":
            game.print_board()
            move = int(input(f"Player {current_player}, choose your move (0-8): "))
            if game.board[move] == "-":
                game.make_move(move, current_player)
                current_player = "O"
            else:
                print("Invalid move! Try again.")
        else:
            game_state = "".join(game.board)
            next_states = algorithm(game_state, current_player)
            next_move = next_states.pop()
            game.make_move(int(next_move), current_player)
            current_player = "X"
    game.print_board()
    winner = game.current_winner
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")


if _name_ == "_main_":
    print("Welcome to Tic-Tac-Toe!")
    choice = input("Choose game mode (1: Human vs Human, 2: Human vs Algorithm): ")

    if choice == "1":
        human_vs_human()
    elif choice == "2":
        algo_choice = input("Choose algorithm (1: BFS, 2: DFS): ")
        if algo_choice == "1":
            human_vs_algorithm(bfs)
        elif algo_choice == "2":
            human_vs_algorithm(dfs)
        else:
            print("Invalid choice!")
    else:
        print("Invalid choice!")
