"""
mqtt.py

An ansible-rulebook event source plugin for receiving events via a mqtt topic.

Arguments:
    host:      The host where the mqtt topic is hosted
    topic:     The mqtt topic
    
Test script stand-alone by exporting MQTT_HOST and MQTT_TOPIC as environment variables
    - $ export MQTT_HOST=localhost
    - $ export MQTT_TOPIC=messages
    
In an EDA rulebook (note: fake collection, cloin.minecraft does not exist): 

    - name: Minecraft events
      hosts: localhost
      sources:
        - cloin.minecraft.mqtt:
            host: localhost
            topic: messages

      rules:
        - name: New minecraft event
          condition: event.type is defined
          action:
            debug:
            
"""

import asyncio
import json
import logging
import os
from typing import Any, Dict

from asyncio_mqtt import Client

async def main(queue: asyncio.Queue, args: Dict[str, Any]):
    logger = logging.getLogger()
    topic = args.get("topic")
    host = args.get("host")

    async with Client(host) as client:
        async with client.messages() as messages:
            await client.subscribe(f'{topic}/#')
            async for message in messages:
                await queue.put(message.payload.decode())

if __name__ == "__main__":
    topic = os.environ.get('MQTT_TOPIC')
    host = os.environ.get('MQTT_HOST')

    class MockQueue:
        print(f"Waiting for messages on '{topic}'...")
        async def put(self, event):
            print(event)

    asyncio.run(main(MockQueue(), {"topic": topic, "host": host}))
