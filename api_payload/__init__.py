"""
AUTHOR: ABRAHAM ISRAEL
CODE NAME: ABRAM 🐼
GITHUB: https://github.com/israelabraham
LINKEDIN: https://linkedin.com/in/abraham-israel
EMAIL: israelvictory87@gmail.com
"""


def error_response(status, message):
    """
    Custom error response

    Args:
        status ([string]): [status message -> 404 not found, 500 server error, 400 bad request, etc]
        message ([string]): [what error message do you want to show to the end user?]

    Returns:
        [response]: [Returns a dictionary of status, and message]
    """
    
    payload = {
        "status": status,
        "message": message
    }
    return payload


def success_response(status, message, data):
    """
    Custom success response

    Args:
        status ([string]): [status message -> 201 created, 200 ok, 202 accepted, etc]
        message ([string]): [what message do you want to show to the end user?]
        data ([dict]): [serialized data from the server side]

    Returns:
        [response]: [Returns a dictionary of status, message, data of whatever object that was serialized]
    """
    
    payload = {
        "status": status,
        "message": message,
        "data": data
    }
    return payload
