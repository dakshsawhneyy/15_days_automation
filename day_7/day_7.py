import os 
import json

config_file = "./config.json"
log_file = "./server.log"

servers = [
    {"hostname": "web-01", "cpu_usage": 45, "status": "active"},
    {"hostname": "web-02", "cpu_usage": 92, "status": "active"},
    {"hostname": "db-01",  "cpu_usage": 85, "status": "maintenance"},
    {"hostname": "db-02",  "cpu_usage": 12, "status": "active"},
    {"hostname": "cache-01", "cpu_usage": 99, "status": "active"}
]

logs = [
    "192.168.1.10 - - [10/Oct/2023] 'GET /home HTTP/1.1' 200",
    "10.0.0.5 - - [10/Oct/2023] 'POST /api/login HTTP/1.1' 500",
    "192.168.1.10 - - [10/Oct/2023] 'GET /about HTTP/1.1' 200",
    "172.16.0.4 - - [10/Oct/2023] 'POST /api/pay HTTP/1.1' 500"
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
# print("----------------------------------------------------")
# print("printing servers with usage > 80 and are active are:")
# print("----------------------------------------------------")
# for server in servers:
#     usage = server["cpu_usage"]
#     status = server["status"]
    
#     if usage > 80 and status == "active":
#         print(server["hostname"])
        
# # Another writing technique
# problem_servers = [s["hostname"] for s in servers if s['cpu_usage'] > 80 and s['status'] == "active"]
# print(problem_servers)

# Ticket 3
# for log in logs:
#     status_code = log.split()[-1]   # -1 = $NF
#     if status_code == "500":
#         print(log.split()[0])
        

# Ticket 4

# Question: Reads server.log.
#           Finds lines ending in 500.
#           Uses a Dictionary to count the occurrences per IP.
#           Prints the result (e.g., 192.168.1.10: 2).

ips = {}
try:
    with open(log_file, "r") as f:
        # content = f.read()

        # if we loop over content, it will loop over every word
        for line in f:  
            status_code = line.split()[1]
            ip = line.split()[0]
            if status_code == "500":
                print(ip)
                ips[ip] = ips.get(ip, 0) + 1
            
except FileNotFoundError as e:
    print(f"{log_file} not found", e)
    

# Looping over ips dictionary
print("printing ips from dictionary")
for ip, count in ips.items():
    print(ip, count)