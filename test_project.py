import pytest
from project import check_winner, make_move, best_move

def test_check_winner_row():
    board = ["X", "X", "X",
             " ", "O", " ",
             " ", " ", "O"]
    assert check_winner(board) == "X"

def test_check_winner_col():
    board = ["O", "X", "X",
             "O", "X", " ",
             "O", " ", " "]
    assert check_winner(board) == "O"

def test_check_winner_diag():
    board = ["X", "O", " ",
             " ", "X", "O",
             " ", " ", "X"]
    assert check_winner(board) == "X"

def test_check_winner_tie():
    board = ["X", "O", "X",
             "X", "O", "O",
             "O", "X", "X"]
    assert check_winner(board) == "Tie"

def test_make_move_valid():
    board = [" " for _ in range(9)]
    make_move(board, 4, "X")
    assert board[4] == "X"

def test_make_move_invalid():
    board = [" " for _ in range(9)]
    make_move(board, 0, "O")
    with pytest.raises(ValueError):
        make_move(board, 0, "X")

def test_best_move():
    board = ["X", "O", "X",
             "X", "O", " ",
             " ", " ", " "]
    move = best_move(board)
    # best_move should return one of the empty positions
    assert move in [5, 6, 7, 8]
