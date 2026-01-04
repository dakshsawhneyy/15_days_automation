import os 
import json

config_file = "./config.json"

servers = [
    {"hostname": "web-01", "cpu_usage": 45, "status": "active"},
    {"hostname": "web-02", "cpu_usage": 92, "status": "active"},
    {"hostname": "db-01",  "cpu_usage": 85, "status": "maintenance"},
    {"hostname": "db-02",  "cpu_usage": 12, "status": "active"},
    {"hostname": "cache-01", "cpu_usage": 99, "status": "active"}
]

# try:
#     with open(config_file, 'r') as f:
#         content = f.read()
        
#         # Load as JSON
#         data = json.load(content)
        
#         # Extract HOSTS Key
#         db_hosts = data['database']['host']
#         print("DB_HOST: ", db_hosts)
# except FileNotFoundError as e:
#     print(f"Error: The file '{config_file}' was not found.")


# Ticket 2
print("----------------------------------------------------")
print("printing servers with usage > 80 and are active are:")
print("----------------------------------------------------")
for server in servers:
    usage = server["cpu_usage"]
    status = server["status"]
    
    if usage > 80 and status == "active":
        print(server["hostname"])
        
# ANother writing technique
problem_servers = [s["hostname"] for s in servers if s['cpu_usage'] > 80 and s['status'] == "active"]
print(problem_servers)