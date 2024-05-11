import unittest
from rest_api_response.responses import error_response, success_response


class TestCustomResponses(unittest.TestCase):
    def test_error_response(self):
        message = "Error message"
        meta = {"key": "value"}
        response = error_response(message, meta)

        self.assertIsInstance(response, dict)
        self.assertEqual(response["status"], False)
        self.assertEqual(response["message"], message)
        self.assertEqual(response["meta"], meta)

    def test_success_response_dict(self):
        payload = {
            "message": "Successful!",
            "data": {
                "title": "title 1",
                "content": "Some text here",
                "author": 1,
            },
        }
        response = success_response(
            message=payload["message"],
            data=payload["data"],
        )

        self.assertEqual(response["status"], True)
        self.assertEqual(isinstance(response["data"], dict), True)
        response.pop("status")
        self.assertEqual(payload, response)

    def test_success_response_list(self):
        payload = {
            "message": "Successful!",
            "data": [
                {
                    "title": "title 1",
                    "content": "Some text here",
                    "author": 1,
                },
                {
                    "title": "title 2",
                    "content": "Some text here",
                    "author": 2,
                },
            ],
        }
        response = success_response(
            message=payload["message"],
            data=payload["data"],
        )

        self.assertEqual(response["status"], True)
        self.assertEqual(isinstance(response["data"], list), True)
        response.pop("status")
        self.assertEqual(payload, response)

if __name__ == "__main__":
    unittest.main()
