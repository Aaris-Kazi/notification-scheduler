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
            logger.error(f"CommonOperations :: createUserDevice :: Unable to create user : {e}")
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
            logger.error(f"CommonOperations :: getUserDevice :: Unable to find user : {username}")
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
            logger.error(f"CommonOperations :: getUserDevices :: Unable to find user or device: {username}")
            raise UserDeviceExceptions()
        return {username: data}

    def getUserDevicesV2(username: str, device_type: list) ->dict:
        '''
        This method allows you to get the Entry for users
        '''
        devices = User_Device.objects.raw(
            f"SELECT * from notificationsApplication_user_device where users = '{username}' AND device_type in {tuple(device_type)}"
        )
        data = [d.device_type for d in devices]
        if len(data) == 0:
            logger.error(f"CommonOperations :: getUserDevices :: Unable to find user or device: {username}")
            raise UserDeviceExceptions()
        return {username: data}

        