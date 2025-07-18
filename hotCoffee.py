import requests 
import json 

data=requests.get("https://api.sampleapis.com/coffee/hot")


listdata=[]

for d in data.json():
    if "Espresso" and "Expresso" not in d["ingredients"]:
        listdata.append(d)

print(json.dumps(listdata, indent=4))