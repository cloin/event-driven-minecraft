# event-driven minecraft super fun kids time excellent

This is sort of a limited test-run of responding to events in Minecraft with some actions. This currently deploys the bedrock server because that's supported on the kinds of devices my kids play Minecraft on. There are not a whole lot of actions that can be performed in bedrock worlds afaik, but you can run some nice party tricks. For instance, when my son joins the world, I can have the server send him a nice message even if I'm not playing the game with him.

### `docker-compose.yml` stands up a minecraft bedrock server with some complementary services
  - `minecraft-rest`: REST API that can be used to send commands to minecraft (e.g. `say Welcome, new user!` where `say` is the command being executed)
  - `webhook`: Prints server events to webhook and/or mqtt
  - `mosquitto`: Minimal MQTT broker
  - `mosquitto_test`: Subscribes to all topics on mqtt broker and prints messages

### Event-Driven Ansible

Additionally, in the eda directory there is an Event-Driven Ansible source plugin for mqtt that consumes messages from a topic on the mqtt broker. 

I could have just used webhooks but mqtt is a little more fun!
