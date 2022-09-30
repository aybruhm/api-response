def error_response(status:bool, message:str):
    """
    Custom error response
    
    :param status: The status code of the response
    :type status: bool
    
    :param message: The message you want to display to the end user
    :type message: str
    
    :return: A dictionary of status and message
    """
    
    payload = {
        "status": status,
        "message": message
    }
    return payload


def success_response(status:bool, message:str, data:dict = {}):
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
