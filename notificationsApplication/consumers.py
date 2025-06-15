from channels.generic.websocket import AsyncConsumer
from json import dumps

class NotificationConsumers(AsyncConsumer):
    user_id = ""
    group_name = ""

    async def connect(self):
        print("connect")
        self.user_id =  self.scope['url_route']['kwargs']['user_id']
        self.group_name = f"user_{self.user_id}"

        print(self.user_id)
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def discconect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)


    async def receive(self, text_data):
        pass  # Clients don’t send messages in this case

    async def send_notification(self, event: dict):
        print("event")
        print(event['message'])
        await self.send(text_data = dumps(event['message']))


