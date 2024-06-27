import math

# Define constants for players
HUMAN = -1
AI = 1

# Define the initial empty board
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Function to print the board
def print_board(board):
    chars = {HUMAN: 'X', AI: 'O', 0: ' '}
    for row in board:
        print(' | '.join([chars[cell] for cell in row]))
        print('-' * 5)

# Function to check for a win
def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Function to check for a draw
def check_draw(board):
    return all([cell != 0 for row in board for cell in row])

# Heuristic evaluation function
def heuristic_evaluate(board):
    if check_win(board, AI):
        return 100
    elif check_win(board, HUMAN):
        return -100
    
    score = 0

    # Check rows for potential
    for row in board:
        if row.count(AI) == 2 and row.count(0) == 1:
            score += 10
        if row.count(HUMAN) == 2 and row.count(0) == 1:
            score -= 10

    # Check columns for potential
    for col in range(3):
        col_cells = [board[row][col] for row in range(3)]
        if col_cells.count(AI) == 2 and col_cells.count(0) == 1:
            score += 10
        if col_cells.count(HUMAN) == 2 and col_cells.count(0) == 1:
            score -= 10

    # Check diagonals for potential
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]
    if diag1.count(AI) == 2 and diag1.count(0) == 1:
        score += 10
    if diag1.count(HUMAN) == 2 and diag1.count(0) == 1:
        score -= 10
    if diag2.count(AI) == 2 and diag2.count(0) == 1:
        score += 10
    if diag2.count(HUMAN) == 2 and diag2.count(0) == 1:
        score -= 10

    return score

# Minimax function with depth limitation and heuristic evaluation
def minimax(board, depth, is_maximizing, max_depth):
    score = heuristic_evaluate(board)
    if abs(score) == 100 or check_draw(board) or depth == max_depth:
        return score

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = AI
                    best_score = max(best_score, minimax(board, depth + 1, False, max_depth))
                    board[i][j] = 0
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = HUMAN
                    best_score = min(best_score, minimax(board, depth + 1, True, max_depth))
                    board[i][j] = 0
        return best_score

# Function to find the best move
def find_best_move(board, max_depth):
    best_move = None
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = AI
                move_score = minimax(board, 0, False, max_depth)
                board[i][j] = 0
                if move_score > best_score:
                    best_score = move_score
                    best_move = (i, j)
    return best_move

# Function to play the game
def play_game():
    print("Initial board:")
    print_board(board)

    while True:
        # Human move
        human_move = tuple(map(int, input("Enter your move (row and column): ").split()))
        if board[human_move[0]][human_move[1]] != 0:
            print("Invalid move! Try again.")
            continue
        board[human_move[0]][human_move[1]] = HUMAN
        print("Board after your move:")
        print_board(board)
        
        if check_win(board, HUMAN):
            print("You win!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        
        # AI move
        ai_move = find_best_move(board, max_depth=5)  # Adjust max_depth as needed
        if ai_move:
            board[ai_move[0]][ai_move[1]] = AI
            print("Board after AI's move:")
            print_board(board)

        if check_win(board, AI):
            print("AI wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

# Play the game
play_game()

