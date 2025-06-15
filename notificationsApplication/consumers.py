from channels.generic.websocket import AsyncConsumer
from json import dumps

class NotificationConsumers(AsyncConsumer):
    username = ""
    group_name = ""

    async def connect(self):
        print("connect")
        self.user_id =  self.scope['url_route']['kwargs']['username']
        self.group_name = f"user_{self.username}"

        print(self.username)
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


