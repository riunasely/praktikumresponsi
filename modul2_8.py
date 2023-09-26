import json

# Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria": (25, "Madrid", 34232424)}

# Serialisasi dictionary ke dalam string terkode JSON menggunakan indention
# Cek poin 8, perhatikan tipe data dari hasil print bandingkan dengan objek Python friends
json_string = json.dumps(friends, indent=4)
print(json_string)