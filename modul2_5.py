import json

#Deserializing from file into a Python Object
#cek poin 5 perhatikan tipe datanya
with open('friends.json') as f:
	obj = json.load(f)

	print(type(obj))	# => dict
	print(obj)	# => friends = {"Dan": (20, "London", 13242252),
			# "Maria":[25, "Madrid", 34232424]}
