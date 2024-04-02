import numpy as np
from collections import deque

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.players = {-1: 'X', 1: 'O'}
        self.winning_combos = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

    def print_board(self):
        for row in self.board:
            print(" | ".join([self.players[item] if item in self.players else ' ' for item in row]))
            print("-" * 5)

    def check_winner(self):
        for combo in self.winning_combos:
            symbols = [self.board[pos] for pos in combo]
            if len(set(symbols)) == 1 and symbols[0] != 0:
                return symbols[0]
        return 0

    def is_draw(self):
        return len(np.where(self.board == 0)[0]) == 0

    def is_game_over(self):
        return self.check_winner() != 0 or self.is_draw()

    def get_possible_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]

    def make_move(self, player, move):
        self.board[move] = player

    def minimax(self, player):
        if self.is_game_over():
            winner = self.check_winner()
            if winner == 0:
                return 0
            else:
                return 1 if winner == player else -1

        possible_moves = self.get_possible_moves()

        if player == 1:
            best_value = -np.inf
            for move in possible_moves:
                self.make_move(player, move)
                value = self.minimax(-player)
                self.make_move(0, move)
                best_value = max(best_value, value)
            return best_value
        else:
            best_value = np.inf
            for move in possible_moves:
                self.make_move(player, move)
                value = self.minimax(-player)
                self.make_move(0, move)
                best_value = min(best_value, value)
            return best_value

    def find_best_move(self, player):
        possible_moves = self.get_possible_moves()
        best_value = -np.inf if player == 1 else np.inf
        best_move = None
        for move in possible_moves:
            self.make_move(player, move)
            value = self.minimax(-player)
            self.make_move(0, move)
            if (player == 1 and value > best_value) or (player == -1 and value < best_value):
                best_value = value
                best_move = move
        return best_move

    def bfs(self, player):
        queue = deque([(self.board, player)])
        while queue:
            board, current_player = queue.popleft()
            if self.is_game_over():
                winner = self.check_winner()
                if winner == player:
                    return board
                else:
                    continue
            for move in self.get_possible_moves():
                new_board = board.copy()
                new_board[move] = current_player
                queue.append((new_board, -current_player))

    def dfs(self, player):
        stack = [(self.board, player)]
        while stack:
            board, current_player = stack.pop()
            if self.is_game_over():
                winner = self.check_winner()
                if winner == player:
                    return board
                else:
                    continue
            for move in self.get_possible_moves():
                new_board = board.copy()
                new_board[move] = current_player
                stack.append((new_board, -current_player))


if __name__ == "__main__":
    game = TicTacToe()
    game.print_board()
    current_player = 1
    while not game.is_game_over():
        print(f"Player {game.players[current_player]}'s turn")
        if current_player == 1:
            move = game.find_best_move(current_player)
            # Alternatively, you can use BFS or DFS to get the move:
            # move = game.bfs(current_player)
            # move = game.dfs(current_player)
        else:
            move = tuple(map(int, input("Enter your move (row, col): ").split(',')))
        game.make_move(current_player, move)
        game.print_board()
        current_player *= -1
    winner = game.check_winner()
    if winner == 0:
        print("It's a draw!")
    else:
        print(f"Player {game.players[winner]} wins!")
