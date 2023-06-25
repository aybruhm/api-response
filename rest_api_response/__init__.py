# Typing Imports
from typing import Dict, Union


def error_response(
    message: str, meta: dict = {}
) -> Dict[str, Union[bool, str, dict]]:
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
    message: str, data: dict = {}
) -> Dict[str, Union[bool, str, dict]]:
    """
    Custom success response

    :param message: The success message you want to send to the user
    :type message: str

    :param data: Data that you would be returned to the client
    :type data: dict

    :return: response
    :rtype: dict
    """

    response = {"status": True, "message": message, "data": data}
    return response
