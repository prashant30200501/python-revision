"""import requests 
data ={
    "name" : "piyush",
    "age" : 21
}

response = requests.post( "https://jsonplaceholder.typicode.com/users", json=data)


print(response.json())
print(response.status_code)


import json

user = {
    "name":"piyush",
    "age": 20
}

json_data = json.dumps(user)

print(json_data)

import json

data ='' \
'{ "name": "piyush","age": 21 }'

user = json.loads(data)
print(user["name"]) """


import requests
response=requests.get(" https://jsonplaceholder.typicode.com/users")
users = response.json()

for user in users:
    print(user["name"])