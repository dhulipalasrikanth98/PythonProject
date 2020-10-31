import json

s='{"data":"1"}'
j=json.loads(s)
print(j)
print(type(j))

with open("values.json") as f:
    data=json.load(f)
print(data)
data1={
    "name":"srikanth",
    "salary":"900000",
    "age":"22"

}
print(json.dumps(data1,indent=3,sort_keys=True))