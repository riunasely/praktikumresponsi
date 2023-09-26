import json

# Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", ]}

# serialisasi dictionary ke dalam file bernama 'friends.json'
# cek poin 1, perhatikan hasilnya buka file friends.json
with open('friends.json', 'wt') as f:
	json.dump(friends, f)
