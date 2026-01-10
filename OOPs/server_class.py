import subprocess

class Server:
    def __init__(self, ip, hostname, state):
        self.ip = ip
        self.hostname = hostname
        self.state = state
        
    def ping(self):
        if self.state.upper() == "STOPPED":
            print(f"{self.hostname} is dead. Turn it on first.")
        else:
            print(f"Pinging {self.hostname} at {self.ip}...")
        
    def power_on(self):
        self.state = "RUNNING"
        print(f"Starting {self.hostname}...")
        
s1 = Server("10.0.0.1", "web-server-01", "stopped")
# s1.power_on()
s1.ping()