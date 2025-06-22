from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from loggings.CustomLogging import logger

@shared_task
def send_real_time_notification(username: str, title: str, body: str, deviceType: str, deviceId: str, project_name: str):
    logger.info("sending real time notification")
    channel_layers = get_channel_layer()

    message = {
        "title": title,
        "body": body,
        "device_type": deviceType,
        "device_id": deviceId,
        "project_name": project_name
    }

    logger.debug(username)
    logger.debug(message)
    

    async_to_sync(channel_layers.group_send)(
        f"user_{username}",
        {
            "type": "send_notification",
            "message" : message
        }
    )

@shared_task
def send_real_time_notificationV2(username: str, title: str, body: str, deviceType: list, deviceId: str, project_name: str):
    logger.info("sending real time notification")
    channel_layers = get_channel_layer()

    message = {
        "title": title,
        "body": body,
        "device_type": deviceType,
        "device_id": deviceId,
        "project_name": project_name
    }

    logger.debug(username)
    logger.debug(message)
    

    async_to_sync(channel_layers.group_send)(
        f"user_{username}",
        {
            "type": "send_notification",
            "message" : message
        }
    )
