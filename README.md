# event-driven minecraft

## Overview 

This stack stands up Minecraft and allows for responding to events in Minecraft with some actions. This currently deploys the bedrock server because that's supported on the kinds of devices my kids play Minecraft on. There are not a whole lot of actions that can be performed in bedrock worlds afaik, but you can run some nice party tricks. For instance, when my son joins the world, I can have the server send him a nice message even if I'm not playing the game with him.

### Run it

Some of the Minecraft server configuration can be overridden by host environment variables. To set a Minecraft server name for example, you can run:
```
$ sudo MC_SERVER_NAME=Cloin docker compose up -d
```
Check `docker-compose.yml` for others that can be overridden.

### `docker-compose.yml` stands up a minecraft bedrock server with some complementary services
  - [`mincraft-server`]((https://github.com/itzg/docker-minecraft-bedrock-server)): Minecraft bedrock server 
  - [`minecraft-rest`](https://github.com/macchie/minecraft-bedrock-server-bridge): REST API that can be used to send commands to minecraft (e.g. `say Welcome, new user!` where `say` is the command being executed)
  - `filebeat`: Ships `minecraft-server` logs to logstash
  - `logstash`: Receives `minecraft-server` logs from `filebeat` and sends them to an mqtt topic
  - [`mosquitto`](https://github.com/eclipse/mosquitto): Minimal MQTT broker 
  - `mosquitto_messages`: Subscribes to all topics on mqtt broker and prints messages
  - [`ansible-rulebook`](https://github.com/ansible/ansible-rulebook): ansible-rulebook CLI that waits for messages on mqtt topic and executes some action in response 
  
### Event-Driven Ansible

Event-Driven Ansible is a scalable, responsive automation solution that can process events containing discrete, actionable intelligence; determine the appropriate response to the event; then execute automated actions to address or remediate the event.

The `ansible-rulebook` service mounts the contents of `/eda/` and runs the ansible-rulebook CLI against an inventory and rulebook. Additionally, by passing `--source-dir` to the ansible-rulebook command, the `mqtt.py` source plugin is loaded from the `/eda` directory to read and act on messages on the mqtt topic referenced by the rulebook.

Check out the `/eda` README for me.
