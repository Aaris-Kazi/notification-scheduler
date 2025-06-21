import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from json import dumps
from loggings.CustomLogging import logger

class NotificationConsumers(AsyncWebsocketConsumer):
    username = ""
    group_name = ""

    async def connect(self):
        self.username =  self.scope['url_route']['kwargs']['username']
        self.group_name = f"user_{self.username}"

        print(self.username)
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        logger.info("Websocket Connected!")

    async def discconect(self, close_code):
        logger.info("Websocket DisConnected!")
        await self.channel_layer.group_discard(self.group_name, self.channel_name)


    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json["message"]

            await self.send(text_data=json.dumps({"message": message}))
        except Exception as e:
            logger.error(str(e))
            await self.send(text_data=json.dumps({"message": "INVALID JSON"}))
        

    async def send_notification(self, event: dict):
        await self.send(text_data = dumps(event['message']))


