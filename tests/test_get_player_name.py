import unittest
from app import app


class TestGetPlayerName(unittest.TestCase):
    """ Set to test mode to see the error message """
    def setUp(self):
        app.config["TESTING"] = True
        app.secret_key = "test" #to avoid session error just in case
        self.client = app.test_client()

    def test_index_returns_200(self):
        """ Test the index page if it shows correct response or not"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_names_redirect(self):
        """ check if it'll redirect to the original page after sending the name"""
        response = self.client.post("/set_name",
                                    data={"p1_name":"Nonoka", "p2_name":"Grace"},
                                    follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
