import unittest
from rest_api_payload import success_response, error_response


class TestInit(unittest.TestCase):
    
    def test_error_response(self):
        
        payload = {
            "status": False,
            "message": 'BAD REQUEST!'
        }
        self.assertEqual(
            payload, 
            error_response(
                status=payload.get("status"), 
                message=payload.get("message"))
        )
        
    def test_success_response(self):
        
        payload = {
            "status": True,
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