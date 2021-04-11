import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer

class TempConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type" : "websocket.accept"
        })
        await self.send({
            "type" : "websocket.send",
            "text" : "Allahu Ackbar"
        })
        await asyncio.sleep(10)
        await self.send({
            "type" : "websocket.close"
        }
        )
    
    async def websocket_receive(self, event):
        print("recieve", event)
    
    async def websocket_disconnect(self, event):
        print("disconnected", event)