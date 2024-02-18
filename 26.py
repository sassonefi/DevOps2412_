import requests

#response = requests.delete("http://localhost:8081/items/1")

response = requests.get("http://localhost:8081/items")
actual = len(response.json())
expected = 2
assert expected == actual