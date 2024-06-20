#Alpha-Beta 修剪法修改自Chatgpt

class Gomoku:
    def __init__(self, size=11):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_winner = None
    
    def print_board(self):
        print("   " + "   ".join([chr(ord('A') + i) for i in range(self.size)]))

        for r in range(self.size):
            row = [str(self.board[r][c]) for c in range(self.size)]
            print(str(r + 1).rjust(2) + " " + " | ".join(row))
            if r < self.size - 1:
                print("  " + "---|" * (self.size - 1) + "---")
    
    def available_moves(self):
        return [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == ' ']

    def make_move(self, square, letter):
        if self.board[square[0]][square[1]] == ' ':
            self.board[square[0]][square[1]] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind, col_ind = square
        directions = [
            [(row_ind + i, col_ind) for i in range(-4, 5)],
            [(row_ind, col_ind + i) for i in range(-4, 5)],
            [(row_ind + i, col_ind + i) for i in range(-4, 5)],
            [(row_ind + i, col_ind - i) for i in range(-4, 5)]
        ]
        for direction in directions:
            count = 0
            for r, c in direction:
                if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == letter:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
        return False


def evaluate(board):
    score = 0
    size = len(board)
    for row in board:
        score += evaluate_line(row)
    for col in range(size):
        col_vals = [board[row][col] for row in range(size)]
        score += evaluate_line(col_vals)
    for d in range(-size + 1, size):
        diag1 = [board[i][i - d] for i in range(max(0, d), min(size, size + d)) if 0 <= i - d < size]
        diag2 = [board[i][d + size - 1 - i] for i in range(max(0, -d), min(size, size - d)) if 0 <= d + size - 1 - i < size]
        score += evaluate_line(diag1)
        score += evaluate_line(diag2)
    return score

def evaluate_line(line):
    score = 0
    for i in range(len(line) - 4):
        window = line[i:i+5]
        if window.count('X') == 5:
            score += 1000
        elif window.count('O') == 5:
            score -= 1000
        elif window.count('X') == 4 and window.count(' ') == 1:
            score += 100
        elif window.count('O') == 4 and window.count(' ') == 1:
            score -= 100
        elif window.count('X') == 3 and window.count(' ') == 2:
            score += 10
        elif window.count('O') == 3 and window.count(' ') == 2:
            score -= 10
    return score
def alpha_beta(state, depth, alpha, beta, maximizing_player):
    max_player = 'X'
    other_player = 'O' if maximizing_player == 'X' else 'X'

    if state.current_winner:
        return {'position': None, 'score': 1000 if state.current_winner == max_player else -1000}
    
    if depth == 0 or not state.available_moves():
        return {'position': None, 'score': evaluate(state.board)}
    
    if maximizing_player:
        max_eval = {'position': None, 'score': -float('inf')}
        for move in state.available_moves():
            state.make_move(move, max_player)
            evaluation = alpha_beta(state, depth - 1, alpha, beta, False)
            state.board[move[0]][move[1]] = ' '
            state.current_winner = None
            evaluation['position'] = move
            if evaluation['score'] > max_eval['score']:
                max_eval = evaluation
            alpha = max(alpha, evaluation['score'])
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = {'position': None, 'score': float('inf')}
        for move in state.available_moves():
            state.make_move(move, other_player)
            evaluation = alpha_beta(state, depth - 1, alpha, beta, True)
            state.board[move[0]][move[1]] = ' '
            state.current_winner = None
            evaluation['position'] = move
            if evaluation['score'] < min_eval['score']:
                min_eval = evaluation
            beta = min(beta, evaluation['score'])
            if beta <= alpha:
                break
        return min_eval
    
def play_game():
    g = Gomoku()
    letter = 'X'
    while g.available_moves():
        if letter == 'O':
            print("AI's turn (O):")
            square = alpha_beta(g, 3, -float('inf'), float('inf'), True)['position']
        else:
            g.print_board()
            while True:
                move = input("Your turn (X), enter your move (e.g., E6): ").upper()
                if len(move) < 2 or len(move) > 3:
                    print("Invalid move. Please enter a valid move (e.g., E6).")
                    continue
                col = ord(move[0]) - ord('A')
                row = int(move[1:]) - 1
                if 0 <= col < g.size and 0 <= row < g.size and g.board[row][col] == ' ':
                    square = (row, col)
                    break
                else:
                    print("Invalid move. Please enter a valid move (e.g., E6).")

        g.make_move(square, letter)
        g.print_board()
        print('')

        if g.current_winner:
            print(letter + ' wins!')
            return

        letter = 'O' if letter == 'X' else 'X'

    print('It\'s a tie!')

if __name__ == '__main__':
    play_game()

