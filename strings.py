myStr = 'Hello world'

# print(dir(myStr))

print(myStr.title())                    #Metodo para poner la letra capital de cada palabra del texto

print(myStr.upper())                    #Metodo para poner en mayusculas
print(myStr.lower())                    #Metodo para poner en minusculas
print(myStr.swapcase())                 #Metodo para poner las letras al contrario de como se escriben
print(myStr.capitalize())               #Metodo para poner la letra capital de la primera palabra del texto
print(myStr.replace('Hello', 'Bye'))    #Metodo para remplazar las palabras
print(myStr.count('l'))                 #Metodo para contar cuantas veces esta escrito la letra 'l'
print(myStr.startswith('hola'))         # Empieza con la palabra 'hola'
print(myStr.endswith('world'))          # Termina con la palabra 'world'

print(myStr.split(' '))                 # separa por el caracter ' ' --> Lista

print(myStr.find(' '))                  # busca el caracter ' ' --> Integer
print(myStr.find('o'))                  # busca el primer caracter 'o' --> Integer
print(myStr.index('o'))                 # busca el primer caracter 'o' --> Integer

print(len(myStr))                       # tamaño del String --> Integer

print(myStr[2], myStr[7], myStr[-1])

print("myStr: " + myStr)
print(f"myStr: {myStr}")
print("myStr: {0}".format(myStr))
