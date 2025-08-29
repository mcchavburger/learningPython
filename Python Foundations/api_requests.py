import requests

response = requests.get("https://icanhazdadjoke.com",headers={"Accept":"application/json"})
json = response.json()
print(json["joke"])
