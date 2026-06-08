import requests 
data ={
    "name" : "piyush",
    "age" : [21]
}

response = requests.post( "https://jsonplaceholder.typicode.com/users", json=data)


print(response.json())
