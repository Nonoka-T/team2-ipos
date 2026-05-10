import unittest

import app as game_app
from app import all_same_player, check_draw, check_winner, new_board, to_row_col


class TestGame(unittest.TestCase):
    def setUp(self):
        """Reset the board before each test to ensure a clean state."""
        game_app.board = new_board()

    def test_board_is_3x3(self):
        """Tests for new_board() — checks the board is created correctly as a 2D list."""
        board = new_board()
        self.assertEqual(len(board), 3)
        for row in board:
            self.assertEqual(len(row), 3)

    def test_to_row_col_conversion(self):
        """Tests for to_row_col() — checks flat cell numbers convert correctly to (row, col)."""
        # Cell 1 is the top-left corner of the board.
        # Expected: (row=0, col=0)
        self.assertEqual(to_row_col(1), (0, 0))

    def test_all_same_player_function(self):
        """Tests for all_same_player() — checks if all values in a line belong to the same player."""
        # All three values are 'O', so O is the winner of this line.
        # Expected: 'O'
        self.assertEqual(all_same_player(["O", "O", "O"]), "O")

    def test_check_winner(self):
        # O fills the entire left column (vertical) [0][0], [1][0], [2][0].
        # Expected: 'O'
        game_app.board[0][0] = "O"
        game_app.board[1][0] = "O"
        game_app.board[2][0] = "O"
        self.assertEqual(check_winner(), "O")

    def test_draw_when_board_full(self):
        # Every cell is filled with a player marker and there is no winner.
        # Expected: True
        # fmt: off
        game_app.board = [["X", "O", "X"],
                          ["X", "X", "O"],
                          ["O", "X", "O"]]
        self.assertTrue(check_draw())
        # fmt: on


if __name__ == "__main__":
    unittest.main()
