from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

# Constants
P1 = "X"
P2 = "O"
COLS = 3

# Initialise game board and current player
board = [" "] * 9
current_player = P1
score_x = 0
score_o = 0


def all_same_player(values):
    """Return the player if all values in the list are the same, otherwise None."""
    if len(set(values)) == 1 and values[0] != " ":
        return values[0]
    return None


def check_winner():
    """Return the winning player (X or O) or None. Logic is dynamic — works for any n×n board."""
    b = board
    n = len(b)

    # Check rows
    for r in range(n):
        winner = all_same_player(b[r])
        if winner:
            return winner

    # Check columns
    for c in range(n):
        column_values = []
        for r in range(n):
            column_values.append(b[r][c])
        winner = all_same_player(column_values)
        if winner:
            return winner

    # Check main diagonal (top-left to bottom-right)
    main_diagonal = []
    for i in range(n):
        main_diagonal.append(b[i][i])
    winner = all_same_player(main_diagonal)
    if winner:
        return winner

    # Check anti-diagonal (top-right to bottom-left)
    anti_diagonal = []
    for r in range(n):
        anti_diagonal.append(b[r][n - 1 - r])
    winner = all_same_player(anti_diagonal)
    if winner:
        return winner

    return None


def check_draw():
    """Return True if no empty cells remain (no number left on the board)."""
    for row in board:
        for cell in row:
            # If we find a number, the game is NOT a tie
            if cell not in {P1, P2}:
                return False
    # If we never found a number, it is a tie
    return True


def new_board():
    """Initialize a new 3x3 board."""
    return [[" " for _ in range(COLS)] for _ in range(COLS)]


def to_row_col(target):
    """Convert a 1-based flat cell number (1-9) to (row, col) for the 2D board."""
    row = (target - 1) // COLS
    col = (target - 1) % COLS
    return row, col


# Initialise game board and current player
board = new_board()
current_player = P1


@app.route("/")
def index():
    winner = check_winner()
    draw = check_draw()
    return render_template(
        "index.html",
        board=board,
        current_player=current_player,
        winner=winner,
        draw=draw,
    )


@app.route("/play/<int:cell>")
def play(cell):
    global current_player, score_x, score_o
    if board[cell] == " ":
        board[cell] = current_player
        winner = check_winner()
        if winner == "X":
            score_x += 1
        elif winner == "O":
            score_o += 1
        if not winner:
            current_player = "O" if current_player == "X" else "X"
    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    global board, current_player
    board = new_board()
    current_player = P1
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
