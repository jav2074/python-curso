print('########################################################################')
print('LOOPs')
collection = ['Enrique', 'Franco', 'Alexia', 'Diego', 'Toto', 'Tito', 'Chelo']
for i in collection:
	if i == 'Diego':
		break
	print(i)
print('########################################################################')
for j in collection:
	print(f'indice: {collection.index(j)} - nombre: {j}')
print('########################################################################')
for x in range(1,8):
	print(x)
print('########################################################################')
for y in 'Hola':
	print(y)
print('########################################################################')
cont = 4
while cont <= 10:
	print(cont)
	cont = cont + 1
print('########################################################################')