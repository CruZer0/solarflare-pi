import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from .tempclient import getTempTCP

class TempConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type" : "websocket.accept"
        })
        i = 0
        while (i < 10000):
            await self.send({
                "type" : "websocket.send",
                "text" : getTempTCP('192.168.178.48',5005)
                })
            i = i+1
            await asyncio.sleep(3)
        await self.send({
            "type" : "websocket.close"
        })
    
    async def websocket_receive(self, event):
        print("recieve", event)
    
    async def websocket_disconnect(self, event):
        print("disconnected", event)