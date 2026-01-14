import yaml

yaml_file = "./deployment.yaml"

with open(yaml_file, "r") as f:
    data = yaml.safe_load(f)    # safe_load is preferred over load
    
    data["spec"]["replicas"] = 5
    
    # Write back to deployment
    with open(yaml_file, "w") as f:
        yaml.dump(data, f, default_flow_style=False)