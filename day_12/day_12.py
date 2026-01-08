import re

text = "The attack came from 192.168.1.1 at 4pm. Another source was 10.0.0.55 which failed."


##### \d = digit, ##### + means one or more ##### \. means actual dot
# pattern = r"\d+\.\d+\.\d+\.\d+"
# ips = re.findall(pattern, text)
# print(ips)


# Ticket 1
log_entry = "Error at 10.2.3.4: Connection refused by 192.168.1.105"
pattern = r"\d+\.\d+\.\d+\.\d+"
ips = re.findall(pattern, text)
print(ips)