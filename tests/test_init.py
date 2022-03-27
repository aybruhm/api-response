import unittest
from rest_api_payload import error_response, success_response


class TestInit(unittest.TestCase):
    
    def test_error_response(self):
        
        payload = {
            "status": "400 bad request",
            "message": 'BAD REQUEST!'
        }
        self.assertEqual(
            payload, 
            error_response(status=payload.get("status"), message=payload.get("message"))
        )
        
    def test_success_response(self):
        
        payload = {
            "status": "200 ok",
            "message": 'OKKK!',
            "data": {
                "title": "title 1",
                "content": 'Some text here',
                "author": 1
            }
        }
        self.assertEqual(
            payload, 
            success_response(
                status=payload.get("status"), 
                message=payload.get("message"),
                data=payload.get("data"))
        )
        
if __name__ == '__main__':
    unittest.main()