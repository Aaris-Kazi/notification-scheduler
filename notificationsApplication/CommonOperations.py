from exceptions import ApplicationExceptions, UserDeviceExceptions
from .models import User_Device
from loggings.CustomLogging import logger

class CommonOperations:


    def createUserDevice(username: str, device_type: str) ->None:
        '''
        This method allows you to create new Entry for users
        '''
        try:
            User_Device.objects.create(
                users = username,
                device_type = device_type,
            )
        except Exception as e:
            logger.error(str(e))
            raise Exception

    def getUserDevice(username: str) ->dict:
        '''
        This method allows you to get the Entry for users
        '''
        devices = User_Device.objects.filter(
            users = username
        )
        data = [d.device_type for d in devices]
        if len(data) == 0:
            raise ApplicationExceptions()
        return {username: data}

    def getUserDevices(username: str, device_type: str) ->dict:
        '''
        This method allows you to get the Entry for users
        '''
        devices = User_Device.objects.filter(
            users = username,
            device_type = device_type
        )
        data = [d.device_type for d in devices]
        if len(data) == 0:
            raise UserDeviceExceptions()
        return {username: data}

        