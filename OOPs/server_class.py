import subprocess

class Server:
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname
        
    def ping(self):
        print(f"Pinging {self.hostname} at {self.ip}...")
        
s1 = Server("10.0.0.1", "web-server-01")
s1.ping()