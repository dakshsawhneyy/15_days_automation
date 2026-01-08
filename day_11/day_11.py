# SSH Into Servers using paramiko
import paramiko

# Define the servers
servers = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
key_path = "./mykey"
user = "ubuntu"

# Set the client (do this once)
ssh = paramiko.SSHClient()
# This line is crucial: it auto-accepts unknown host keys (like typing "yes" in shell)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Start ssh in servers
for ip in servers:
    print(f"Connecting to ip: {ip}")
    try:
        # connect
        ssh.connect(ip, username=user, key_filename=key_path, timeout=5)
        
        # Run the command # stdin, stdout, stderr are file-like objects
        stdin, stdout, stderr = ssh.exec_command("uptime")
        
        # 5. Get the output (decode bytes to string)
        output = stdout.read().decode().strip()
        
        print(f"✅ {ip} uptime: {output}")
    except Exception as e:
        print(f"❌ Failed to connect to {ip}: {e}")
    finally:
        # Always close the connection to free up ports
        ssh.close()