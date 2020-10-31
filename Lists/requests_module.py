import requests
# s=requests.get("https://reqres.in/api/users/2")
# print(s.text)
# print(s.status_code)
url="https://reqres.in/api/users/2"
data = {
    "name":"xxxx",
    "job":"yyyy"
}
r=requests.post(url=url,data=data)
print(r.json())
