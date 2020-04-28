print('########################################################################')
print('LOOPs')
collection = ['Enrique', 'Franco', 'Alexia', 'Diego', 'Teko']
for i in collection:
	if i == 'Diego':
		break
	print(i)
print('########################################################################')
for j in collection:
	print(f'indice: {collection.index(j)} - nombre: {j}')
print('########################################################################')