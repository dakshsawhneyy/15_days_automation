import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    print("API is Online")
    json_res = response.json()
    title = json_res["title"]
    print("title: ", title)
else:
    print("API is not Online")