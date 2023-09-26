import json

#Loading a JSON encoded string intro a Python Object
#cek poin 6 perhatikan hasilnya
json_string = """{
	"Dan": [
		20,
		"London",
		13242252
	],
	"Maria": [
		25,
		"Madrid",
		34232424
	]
}"""

obj = json.loads(json_string)
print(type(obj))	# => dict
print(obj)	# => friends = {"Dan": (20, "London", 13242252),
		# "Maria":[25, "Madrid", 34232424]}