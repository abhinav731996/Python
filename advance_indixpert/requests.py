import requests
import json 

endpoint = "http://universities.hipolabs.com/search?country=India"

response = requests.get(endpoint)

data = response.json()

# print(json.dumps(data,indent=4))

# flag = 0
for university in data:
    if university["state-province"] == "Haryana":
        print(json.dumps(university, indent=4))
        # flag = 1
