import json
import os

config_file = "./config.json"

new_config = {
    "app_name": "backend",
    "port": 8000,
    "debug_mode": True
}


# Check if file is empty, if yes then append [] else append data
if os.path.exists(config_file) and os.path.getsize(config_file) > 0:
    with open(config_file, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
        
        data.append(new_config)
        
        with open(config_file, "w") as f:
            json.dump(data, f, indent=4)