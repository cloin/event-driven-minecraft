# Event-Driven Ansible

As select events occur on the Minecraft server, the webhook service will forward these events to a topic called "messages" on the mqtt broker service (mosquitto). 

The Event-Driven Ansible service (ansible-rulebook) is running a rulebook (`minecraft-rulebook.yml`) which is configured to use a custom source plugin (`mqtt.py`) to consume messages from the mqtt topic. 

```
    - name: Respond to player spawn events
      condition: event.container.name == "minecraft-server" and event.mc_event_type == "Spawned"
      action:
        run_playbook:
          name: /eda/minecraft-playbook.yml
```

When a new message is recieved that matches the condition specified in the rulebook (event coming from "minecraft-server and mc_event_type is "Spawned"), `minecraft-playbook.yml` is called which sends a command (e.g. say Hello, {{ ansible_eda.event.mc_player_name }}) back to the Minecraft REST service (minecraft-rest).
