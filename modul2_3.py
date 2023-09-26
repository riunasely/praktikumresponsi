import json

#Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}

#serealisasi dictionary ke dalam file bernama 'friends.json' dengan indention
#cek poin 3, perhatikan hasilnya pada file friends.json
with open('friends.json', 'wt') as f:
	json.dump(friends, f, indent=4)
