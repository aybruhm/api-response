# Stdlib Imports
from typing import Dict, Union, List, Any


def error_response(message: str, meta: dict = {}) -> Dict[str, Any]:
    """
    Custom error response

    :param message: The error message you want to send to the user
    :type message: str

    :param meta: Additional information/context to the error
    :type meta: dict

    :return: response
    :rtype: dict
    """

    response = {"status": False, "message": message, "meta": meta}
    return response


def success_response(
    message: str, data: Union[List[Any], Dict[str, Any]] = {}
) -> Dict[str, Any]:
    """
    Custom success response

    :param message: The success message you want to send to the user
    :type message: str

    :param data: Data that you would be returned to the client
    :type data: dict or list

    :return: response
    :rtype: dict
    """

    response = {"status": True, "message": message, "data": data}
    return response
