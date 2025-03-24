# Tic-Tac-Toe Game with Minimax AI

## [Video Demo](https://youtu.be/your-demo-link)

### Description:
This project is a Tic-Tac-Toe game implemented in Python, featuring an unbeatable AI powered by the Minimax algorithm. The game allows the player to face off against an intelligent computer opponent that always makes the optimal move.

#### How the Program Works?
The game features a simple command-line interface where the player can play against an AI opponent. The AI uses the Minimax algorithm to calculate the best possible move. Here’s how the game works:

1. The board consists of 9 positions, numbered from 0 to 8.
2. The player plays as "X" and the AI plays as "O."
3. The game alternates between the player's move and the AI’s move until a winner is determined or a tie occurs.
4. The Minimax algorithm simulates all possible moves, recursively analyzing each possibility and selecting the best outcome for the AI. It maximizes the AI's chances of winning and minimizes the player's chances.

### TODO:

#### Download
Download the repository through Clone Repository or Download Zip.
```
git clone https://github.com/xmadmaxdx/tic-tac-toe-minimax.git
```

#### Installation
After downloading, navigate to the project folder directory in your terminal.
```
cd tic-tac-toe-minimax
```
Use [pip](https://pip.pypa.io/en/stable/) to install the necessary libraries.
```
pip install -r requirements.txt
```

#### Usage
Run the Python script `project.py` to start the game:
```
python project.py
```
The game will prompt the user to enter a move, and you will play as "X" against the AI ("O").

To run tests using [pytest](https://docs.pytest.org/en/7.2.x/), use the following command:
```
pytest test_project.py
```

#### Game Instructions:
- The board positions are numbered from 0 to 8 as follows:
```
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

- Enter a number between 0-8 to place your `X` on the board. The AI will automatically place its `O` on its best move.



>[!NOTE]
> The positions on the board are indexed from 0 to 8, starting from the top-left corner.

>[!IMPORTANT]
> If an invalid move is entered (for example, choosing an already filled position), the program will prompt the user to try again.

## References
- Minimax algorithm: [Minimax Wikipedia](https://en.wikipedia.org/wiki/Minimax)
- Python `random` module: [Python docs](https://docs.python.org/3/library/random.html)
