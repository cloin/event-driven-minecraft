# event-driven minecraft super fun kids time excellent

### `docker-compose.yml` stands up a minecraft bedrock server with some complementary services
  - `minecraft-rest`: REST API that can be used to send commands to minecraft (e.g. `say Welcome, new user!` where `say` is the command being executed)
  - `webhook`: Prints server events to webhook and/or mqtt
  - `mosquitto`: Minimal MQTT broker
  - `mosquitto_test`: Subscribes to all topics on mqtt broker and prints messages

### Event-Driven Ansible

Additionally, in the eda directory there is an Event-Driven Ansible source plugin for mqtt that consumes messages from a topic on the mqtt broker.
