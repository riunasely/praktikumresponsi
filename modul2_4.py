import json

#Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}

#Serealisasi dictionary ke dalam String terkode JSON menggunakan indention
#cek poin 4, perhatikan hasilnya
json_string = json.dumps(friends, indent=4)
print(json_string)
