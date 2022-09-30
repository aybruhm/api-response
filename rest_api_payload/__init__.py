# Typing Imports
from typing import Any


def error_response(status:bool, message:str) -> dict[str, Any]:
    """
    Custom error response
    
    :param status: This is a boolean value that indicates whether the request was not successful
    :type status: bool
    
    :param message: This is the message you want to send to the user
    :type message: str
    
    :return: A dictionary with the keys status and message.
    """
    
    payload = {
        "status": status,
        "message": message
    }
    return payload


def success_response(status:bool, message:str, data:dict = {}) -> dict[str, Any]:
    """
    Custom success response
    
    :param status: This is a boolean value that indicates whether the request was successful
    :type status: bool
    
    :param message: This is the message you want to send to the user
    :type message: str
    
    :param data: This is the data that you want to return to the client
    :type data: dict
    
    :return: A dictionary with the keys status, message, and data.
    """
    
    payload = {
        "status": status,
        "message": message,
        "data": data
    }
    return payload
