import requests
import json
import uuid

# Ticket 1:
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# if response.status_code == 200:
#     print("API is Online")
#     json_res = response.json()
#     title = json_res["title"]
#     print("title: ", title)
# else:
#     print("API is not Online")


# Ticket 2:
payload = {
    "title": "Shubu saying hello",
    "Age": "99",
    "Lungi_Size": "XXXXXL"
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
print(response.json())

if response.status_code == 201:
    print(f"Alert Sent! Ticket ID: {uuid.uuid4()}")
else:
    print("Error Occurred")