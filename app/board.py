import chess
import chess.svg

def print_board(board):
    print(board)

def get_move():
    move = input("Enter your move (e.g., 'e2e4'): ")
    try:
        chess.Move.from_uci(move)
        return move
    except ValueError:
        print("Invalid move. Please try again.")
        return get_move()

def play_chess():
    board = chess.Board()

    while not board.is_game_over():
        print_board(board)
        move = get_move()

        if chess.Move.from_uci(move) in board.legal_moves:
            board.push(chess.Move.from_uci(move))
        else:
            print("Illegal move. Try again.")

    print("Game Over")
    print("Result: " + board.result())

if __name__ == "__main__":
    play_chess()


