import json
import requests

#requests JSON file ke REST API
respons = requests.get('https://jsonplaceholder.typicode.com/todos')


#membaca JSON file dengan JSON dalam format text
todos = json.loads(respons.text)

#PERHATIKAN tipe datanya, tipe data apa yang digunakan?
print(type(todos))
print(todos)

#menampilkan data yang sesuai dengan konteksnya
#dicontohkan adalah daftar yang telah selesai mengerjakan tugas
#completed == True
#perhatikan hasilnya dan jelaskan
for tugas in todos:
	if tugas['completed'] == True:
		print(tugas)