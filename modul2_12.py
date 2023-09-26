import json
import requests

#requests JSON file ke REST API
respons = requests.get('https://jsonplaceholder.typicode.com/todos')

#membaca JSON file dengan JSON dalam format text
todos = json.loads(respons.text)

#PERHATIKAN tipe datanya, tipe data apa yang digunakan?
#Jelaskan tipe data tersebut
print(type(todos))
print(todos)