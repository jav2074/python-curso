test_list = list(range(0,10))

# print(dir(numbers_list))

## Métodos de una lista ##

print(f"Número de elementos de la lista: {len(test_list)}")				# Cuenta el numero de elementos de una lista
print(f"Existe el numero 5 en la lista: test_list {5 in test_list}")	# Devuelve true o false dependiendo de la sentencia <in> 
#test_list.append('francois')											# Inserta al final un elemento de cualquier tipo a la lista
#test_list.extend(['Pip','Merge'])										# Inserta uno o varios elementos de lista a una lista sin crear sub-listas
#test_list.insert(1, 'violet')											# Inserta un elemento dependiendo del índice
#test_list.pop()														# Elimina el último elemento de la lista
test_list.sort(reverse=True)											# Ordena la lista. ## No puede haber elementos de diferentes tipos para ordernar. ## 'reverse=True' ordena a la inversa
print(test_list.index(5))												# Devuelve el índice del elemento que se busca
print(test_list.count(0))												# Cuenta las veces en que aparece cierto elemento 