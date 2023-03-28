# event-driven minecraft super fun kids time excellent

This stack stands up Minecraft bedrock and allows for responding to events in Minecraft with some actions. This currently deploys the bedrock server because that's supported on the kinds of devices my kids play Minecraft on. There are not a whole lot of actions that can be performed in bedrock worlds afaik, but you can run some nice party tricks. For instance, when my son joins the world, I can have the server send him a nice message even if I'm not playing the game with him.

### `docker-compose.yml` stands up a minecraft bedrock server with some complementary services
  - `mincraft-server`: Minecraft bedrock server  [itzg/docker-minecraft-bedrock-server](https://github.com/itzg/docker-minecraft-bedrock-server) 
  - `minecraft-rest`: REST API that can be used to send commands to minecraft (e.g. `say Welcome, new user!` where `say` is the command being executed) [macchie/minecraft-bedrock-server-bridge](https://github.com/macchie/minecraft-bedrock-server-bridge)
  - `webhook`: Prints server events to webhook and/or mqtt [edward3h/minecraft-webhook](https://github.com/edward3h/minecraft-webhook)
  - `mosquitto`: Minimal MQTT broker [eclipse/mosquitto](https://github.com/eclipse/mosquitto)
  - `mosquitto_test`: Subscribes to all topics on mqtt broker and prints messages [edward3h/minecraft-webhook](https://github.com/edward3h/docker-bds-integration-test/blob/029cd5f62241dc79d05d5fe5d584f7d246844385/docker-compose.yml#L71-L76)

### Event-Driven Ansible

Additionally, in the eda directory there is an Event-Driven Ansible source plugin for mqtt that consumes messages from a topic on the mqtt broker. 

I could have just used webhooks but mqtt is a little more fun!
