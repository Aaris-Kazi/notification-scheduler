from rest_framework import status
from rest_framework.exceptions import APIException

class ApplicationExceptions(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "User not found"
    default_code = "User not found"

class UserDeviceExceptions(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "User or Device not found"
    default_code = "User or Device not found"