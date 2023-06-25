import unittest
from rest_api_response import success_response, error_response


class TestInit(unittest.TestCase):
    """Parent test case"""

    def test_error_response(self):
        payload = {"message": "Error!", "meta": {}}
        response = error_response(message=payload["message"])

        self.assertEqual(response["status"], False)
        response.pop("status")
        self.assertEqual(payload, response)

    def test_success_response(self):
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
        response.pop("status")
        self.assertEqual(payload, response)


if __name__ == "__main__":
    unittest.main()
