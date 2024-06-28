import chess
import math

# Heuristic evaluation function
def evaluate_board(board):
    if board.is_checkmate():
        if board.turn:
            return -9999  # Black wins
        else:
            return 9999  # White wins
    elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition():
        return 0  # Draw

    # Material evaluation
    eval = 0
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0  # King value is not relevant
    }
    for piece_type in piece_values:
        eval += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        eval -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
    
    return eval

# Minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)
    if maximizing_player:
        max_eval = -math.inf
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to find the best move
def find_best_move(board, depth):
    best_move = None
    best_value = -math.inf if board.turn else math.inf
    for move in board.legal_moves:
        board.push(move)
        board_value = minimax(board, depth - 1, -math.inf, math.inf, not board.turn)
        board.pop()
        if board.turn:
            if board_value > best_value:
                best_value = board_value
                best_move = move
        else:
            if board_value < best_value:
                best_value = board_value
                best_move = move
    return best_move

# Example usage
def play_game():
    board = chess.Board()
    depth = 3  # Set search depth
    print("Initial board:")
    print(board)

    while not board.is_game_over():
        if board.turn:
            # White's turn (Human)
            move = input("Enter your move in UCI notation (e.g., e2e4): ")
            board.push_uci(move)
        else:
            # Black's turn (AI)
            print("AI is thinking...")
            best_move = find_best_move(board, depth)
            board.push(best_move)
            print(f"AI plays: {best_move}")

        print(board)

    print("Game over!")
    print(board.result())

# Play the game
play_game()

