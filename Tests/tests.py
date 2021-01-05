
import unittest
from users import get_users
from unittest import mock
# from unittest.mock import patch

class BasicTests(unittest.TestCase):
    @mock.patch('users.requests.get')
    def test_request_response(self, mock_get):
        mock_get.return_value.status_code = 200 
        response = get_users()

        # Assert that the request-response cycle completed successfully with status code 200.
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
