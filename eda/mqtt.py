"""
mqtt.py

An ansible-rulebook event source plugin for receiving events via a mqtt topic.

Arguments:
    host:      The host where the mqtt topic is hosted
    port:      The port where the mqtt server is listening
    topic:     The mqtt topic

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
        print(f"Waiting for messages on '{topic}' table...")
        async def put(self, event):
            print(event)

    asyncio.run(main(MockQueue(), {"topic": topic, "host": host}))