import json

# Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", ]}

# serialisasi dictionary ke dalam String terkode JSON
# cek poin 2, perhatikan hasilnya
json_string = json.dumps(friends)
print(json_string)
