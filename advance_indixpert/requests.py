import requests 

data=requests.get("http://universities.hipolabs.com/search?country=India")


listdata=[]

for d in data.json():
    if d["state-province"]=="Haryana":
        listdata.append(d)


print(listdata)