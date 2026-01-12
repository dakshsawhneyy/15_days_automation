import json

config_file = "./config.json"

with open(config_file, "r") as f:
    data = json.load(f)
    
    # Modify in-memory
    data["port"] = 8080
    data["debug_mode"] = True
    
    # Write back to disc
    with open(config_file, "w") as f:
        json.dump(data, f, indent=4)