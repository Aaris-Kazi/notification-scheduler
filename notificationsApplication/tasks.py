from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def send_real_time_notification(user_id: str, title: str, body: str):
    channel_layers = get_channel_layer()

    message = {
        "title": title,
        "body": body
    }

    print(message)

    async_to_sync(channel_layers.group_send)(
        f"user_{user_id}",
        {
            "type": "send_notification",
            "messsage" : message
        }
    )
