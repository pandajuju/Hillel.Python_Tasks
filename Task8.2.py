data = {
 	'colors': ['red', 'green', 'blue', 'purple'],
 	'fruits': ['pineapple', 'orange', 'banana'],
 	'clothes': ['coat', 'tshirt'],
}


for k in list(data):
	val = data.pop(k)
	for v in val:
		data[v] = k

print(data)