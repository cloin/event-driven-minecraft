# Event-Driven Ansible

As select events occur on the Minecraft server, the webhook service will forward these events to a topic called "messages" on the mqtt broker service (mosquitto). 

The Event-Driven Ansible service (ansible-rulebook) is running a rulebook (`minecraft-rulebook.yml`) which is configured to use a custom source plugin (`mqtt.py`) to consume messages from the mqtt topic. 

When a new message is recieved that matches the condition specified in the rulebook (e.g. event.type == "PLAYER_CONNECTED"), `minecraft_cmd.yml` is called which sends a command (e.g. say Hello, {{ ansible_eda.event.playerName }}) back to the Minecraft REST service (minecraft-rest).
