import unittest
import app as game_app
from app import check_winner

class TestScoreCounter(unittest.TestCase):
    def test_x_wins(self):
        game_app.board[0] = 'X'
        game_app.board[1] = 'X'
        game_app.board[2] = 'X'
        result = check_winner()
        assert result == 'X'


if __name__ == '__main__':
    unittest.main()