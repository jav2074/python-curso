####################################################
######################LISTAS########################
####################################################
demo_list = [1, 2, 3, 4, 5]
print(demo_list)

r = list(range(1, 10))#Rango de una lista del 1 al 10
print(r)

print(demo_list[2])#Acceder al dato que se encuetra en la posicion seleccionada


colors = ['Blue', 'Yellow', 'Red', 'Black']
print(colors)

colors[1] = 'White'#Modifica el archivo que se encuentra en dicha posicion
print(colors)

colors.append('Green')#Metodo para agregar  un dato a la lista
print(colors)

colors.extend(['Pink', 'Brown'])#Metodo para agregar  varios datos a la lista
print(colors)

colors.insert(1, 'Purple')#Metodo para insertar en una posicion el cual se asigne ademas de que elemento va a asignar
print(colors)

colors.insert(len(colors), 'Gold')#Metodo para insertar en la ULTIMA posicion
print(colors)

colors.pop()#Metodo para eliminar algun elemento de la lista
print(colors)

colors.remove('Purple')#Metodo para eliminar el elemento asignado de la lista
print(colors)

#colors.clear()#Metodo para limpiar la lista
#print(colors)

colors.sort()#Metodo para ordenar alfabeticamente
print(colors)

colors.sort(reverse=True)#Metodo para ordenar de manera ordenada
print(colors)
