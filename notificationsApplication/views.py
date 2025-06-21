from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.request import Request

from constants.AppConstants import USERNAME, DEVICE_TYPE
from exceptions import ApplicationExceptions, UserDeviceExceptions
from notificationsApplication.CommonOperations import CommonOperations
from notificationsApplication.tasks import send_real_time_notification


from .serializers import NotifictionPopUp, UserDevicesCreate


# Create your views here.
class NotificationViewsets(viewsets.ViewSet):
    def list(self, request: Request) -> JsonResponse:
        return JsonResponse({"status": "success"})
    
    def create(self, request: Request) -> JsonResponse:
        try:
            serializer = NotifictionPopUp(data = request.data)
            if serializer.is_valid():
                username = serializer.validated_data[USERNAME]
                deviceType = serializer.validated_data[DEVICE_TYPE]
                title = serializer.validated_data['title']
                body = serializer.validated_data['body']
                data:dict = CommonOperations.getUserDevices(username, deviceType)
                send_real_time_notification(username, title, body)
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"status": "failure", "message": serializer.error_messages}, status = status.HTTP_400_BAD_REQUEST)  
        except UserDeviceExceptions as e:
            return JsonResponse(status=e.status_code, data={"status": "failure", "message": e.default_detail})
    

class DeviceViewsets(viewsets.ViewSet):
    def retrieve(self, request: Request, pk: str =None) -> JsonResponse:
        '''
        this method allows you to fetch the user 
        '''
        try:
            data:dict = CommonOperations.getUserDevice(pk)
            return JsonResponse(data=data)
        except ApplicationExceptions as  e:
            return JsonResponse(status=e.status_code, data={"status": "failure", "message": e.default_detail})
        

    def create(self, request: Request) -> JsonResponse:
        """
        this method allow to create new records
        """
        serializer = UserDevicesCreate(data = request.data)

        if serializer.is_valid():
            username = serializer.validated_data[USERNAME]
            deviceType = serializer.validated_data[DEVICE_TYPE]
            CommonOperations.createUserDevice(username, deviceType)
            return JsonResponse(serializer.data)

        else :
            return JsonResponse({"status": "failure", "message": serializer.error_messages}, status = status.HTTP_400_BAD_REQUEST)  

