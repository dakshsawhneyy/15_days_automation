import subprocess
import json
import re

hostname_output = subprocess.run(["hostname"], capture_output=True, text=True)
hostname = hostname_output.stdout.strip()

disc_usage_output = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
disc_usage_out = disc_usage_output.stdout.splitlines()[1]
disc_usage = disc_usage_out.split()[4].split("%")[0]

log_file = "./app.log"
error_count = 0
with open(log_file, "r") as f:
    for line in f:
        if re.search("error", line, re.IGNORECASE):
            error_count += 1
print(error_count)

payload = {
    "hostname": hostname,
    "disc_usage": disc_usage,
    "error_count": error_count,
}

json_file = "./server_health.json"
with open(json_file, "w") as f:
    f.write(json.dumps(payload))