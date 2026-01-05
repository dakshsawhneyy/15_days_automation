import subprocess
import time

# Ticket 1: run uname -r and then strip output [stripped] if returcode == 0
# result = subprocess.run(["uname", "-r"], capture_output=True, text=True)
# if result.returncode == 0:
#     print("Kernel Version:", result.stdout.split()[0])
# else:
#     print("Command failed!")


## Ticket 2: run df -h / then remove % to get int value and if usage > 80, then print alert
# result = subprocess.run(["df", "-h", "/"], text=True, capture_output=True)
## cpu_usage = result.stdout.strip().split()[11].split('%')[0]       ### Bad Usage -- divide by lines first

# lines = result.stdout.strip().split("\n")   # Split by line
# row_we_needed = lines[1]        # Fetch required line
# cpu_usage = row_we_needed.split()[4].strip("%")     # fetch cpu_usage

# if int(cpu_usage) > 80:
#     print("ALERT: Disk space critical!")
# else:
#     print("Disk space normal")
    
    
# Ticket 3: check if nginx is running, and if its not running then try to start it 
result = subprocess.run(["systemctl", "is-active", "nginx"], text=True, capture_output=True)
while True:
    if result.stdout.strip() == "active":
        print("Nginx is running")
        break
    else:
        print("Nginx is not running, trying to run it")
        verify = subprocess.run(["systemctl", "is-active", "nginx"], text=True, capture_output=True)
        
        if result.stdout.strip() == "active":
            print("Success: Nginx is back online.")
        else:
            print("Critical: Nginx failed to restart.")
        time.sleep(5)