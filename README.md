# event-driven minecraft

## Overview 

This project serves as an Event-Driven Ansible demo and is also how I run my kids' Minecraft server.

This stack stands up Minecraft and allows for responding to events in Minecraft with some actions. This currently deploys the bedrock server because that's supported on the kinds of devices my kids play Minecraft on. There are not a whole lot of actions that can be performed in bedrock worlds afaik, but you can run some nice party tricks. For instance, when my son joins the world, I can have the server send him a nice message even if I'm not playing the game with him.

Events in this stack are generated by log lines from the minecraft-server container (filebeat.yml actually harvests all container logs but drops anything not from minecraft-server). They are collected and shipped by filebeat to logstash. Logstash forwards the log output to mqtt on a topic called “messages.” From there, ansible-rulebook (CLI component of Event-Driven Ansible) is running an mqtt source plugin which acts as a consumer pulling event data from mqtt. When a new message arrives on the topic whose data matches certain conditions, ansible-rulebook runs an action. 

### Run it

Some of the Minecraft server configuration can be overridden by host environment variables. To set a Minecraft server name for example, you can run:
```
$ sudo MC_SERVER_NAME=Cloin docker compose up -d
```
Check `docker-compose.yml` for others that can be overridden.

### `docker-compose.yml` stands up a minecraft bedrock server with some complementary services
  - [`mincraft-server`](https://github.com/itzg/docker-minecraft-bedrock-server): Minecraft bedrock server 
  - [`minecraft-rest`](https://github.com/macchie/minecraft-bedrock-server-bridge): REST API that can be used to send commands to minecraft (e.g. `say Welcome, new user!` where `say` is the command being executed)
  - [`filebeat`](https://github.com/elastic/beats): Ships `minecraft-server` logs to logstash
  - [`logstash`](https://github.com/elastic/logstash): Receives `minecraft-server` logs from `filebeat` and sends them to an mqtt topic
    - This is optional. You could probably just use the [http output](https://www.elastic.co/guide/en/logstash/master/plugins-outputs-http.html) from filebeat, but I wanted to configure Logstash to send log events to MQTT to showcase a custom event source plugin. 
  - [`mosquitto`](https://github.com/eclipse/mosquitto): Minimal MQTT broker 
  - `mosquitto_messages`: Runs a command to subscribe to all topics on mqtt broker and print messages to stdout. Useful to see if log output is received by mosquitto.
  - [`ansible-rulebook`](https://github.com/ansible/ansible-rulebook): ansible-rulebook CLI running a rulebook that waits for messages on mqtt topic and executes some action in response. The rulebook loaded by default (configured in `docker-compose.yml`) waits for new player spawn events and then executes an action to send a welcome chat visible to all players.
  
### Event-Driven Ansible

Event-Driven Ansible is a scalable, responsive automation solution that can process events containing discrete, actionable intelligence; determine the appropriate response to the event; then execute automated actions to address or remediate the event.

The `ansible-rulebook` service mounts the contents of `/eda/` and runs the ansible-rulebook CLI against an inventory and rulebook. Additionally, by passing `--source-dir` to the ansible-rulebook command, the `mqtt.py` source plugin is loaded from the `/eda` directory to read and act on messages on the mqtt topic referenced by the rulebook.

Check out the `/eda` README for me.
