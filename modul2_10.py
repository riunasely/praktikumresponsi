import json
#declaring a dictionary
friends = {"Dan": (20, "Londan", 13242252), "Maria":[25,"Madrid",34232424], 4 : list({1,2})}

#serialisasi dictionary ke dalam string terkode JSN menggunakan indention
#cek poin 10, perhatikan tipe data dari objek python dan perhatikan hasil eksekusi
#berikan penjelasan

json_string = json.dumps(friends, indent=4)
print(json_string)