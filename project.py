import sys
import math
import random

def print_board(board):
    for i in range(3):
        print(" | ".join(board[3*i:3*i+3]))
        if i < 2:
            print("---------")

def check_winner(board):
    lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)            
    ]
    for a,b,c in lines:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Tie"
    return None

def make_move(board, pos, player):
    if pos < 0 or pos > 8 or board[pos] != " ":
        raise ValueError("Invalid move")
    board[pos] = player

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif winner == "Tie":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    if move is None:
        raise ValueError("No moves left")
    return move

def main():
    board = [" " for _ in range(9)]
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner is not None:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break
        if current_player == "X":
            try:
                pos = int(input("Enter your move (0-8): "))
                make_move(board, pos, "X")
            except (ValueError, IndexError):
                print("Invalid move. Try again.")
                continue
        else:
            pos = best_move(board)
            make_move(board, pos, "O")
            print(f"Computer moves to position {pos}")
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
