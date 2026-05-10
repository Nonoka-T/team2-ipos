import unittest
from unittest.mock import patch

from app import app


class TestFrontend(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client before each test."""
        self.client = app.test_client()
        app.config["TESTING"] = True

    @patch("app.render_template")
    def test_index_route_passes_correct_data(self, mock_render_template):
        """Tests for index route, checks if the correct data is passed to the template."""
        mock_render_template.return_value = "Mocked Template"

        # Make a GET request to the index route.
        # Expected: 200 OK
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        # Verify render_template was called with the expected variables.
        # Expected: board, current_player, winner, and draw are passed to the template.
        mock_render_template.assert_called_once()
        _, kwargs = mock_render_template.call_args

        self.assertIn("board", kwargs)
        self.assertIn("current_player", kwargs)
        self.assertIn("winner", kwargs)
        self.assertIn("draw", kwargs)

    @patch("app.new_board")
    def test_reset_route_calls_new_board(self, mock_new_board):
        """Tests for reset route, checks if the board is wiped by calling new_board."""
        # Make a GET request to the reset route.
        # Expected: 302 redirect to the index page
        response = self.client.get("/reset")
        self.assertEqual(response.status_code, 302)

        # Verify that new_board was called to reset the game state.
        # Expected: new_board is called once
        mock_new_board.assert_called_once()


if __name__ == "__main__":
    unittest.main()
