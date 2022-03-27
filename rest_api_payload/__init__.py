def error_response(status:str, message:str):
    """
    This function returns a dictionary of status and message
    
    :param status: The status code of the response
    :type status: str
    
    :param message: The message you want to display to the end user
    :type message: str
    
    :return: A dictionary of status and message
    """
    
    payload = {
        "status": status,
        "message": message
    }
    return payload


def success_response(status:str, message:str, data:dict):
    """
    Custom success response
    
    :param status: The status code of the response
    :type status: str
    
    :param message: The message you want to show to the end user
    :type message: str
    
    :param data: dict
    :type data: dict
    
    :return: A dictionary of status, message, data of whatever object that was serialized
    """

    
    payload = {
        "status": status,
        "message": message,
        "data": data
    }
    return payload
