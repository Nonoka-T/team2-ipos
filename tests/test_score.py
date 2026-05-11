import unittest
import app as game_app
from app import check_winner, P1


class TestScoreCounter(unittest.TestCase):
    def setUp(self):
        game_app.board = game_app.new_board()

    def test_x_wins(self):
        game_app.board[0][0] = P1
        game_app.board[0][1] = P1
        game_app.board[0][2] = P1
        result = check_winner()
        self.assertEqual(result, P1)


if __name__ == "__main__":
    unittest.main()