# Strings

string = "hello world"

dir(string)  # Sirve para ver los modulos y metodos que se pueden utilizar con una string

## Metodos para strings ##

print(string.upper())					## Sirve para hacer todas las letras mayúsculas
print(string.lower())					## Sirve para hacer todas las letras minúsculas
print(string.swapcase())				## Las mayúsculas se vuelven minúsculas y viceversa
print(string.capitalize())				## La primera letra del String se vuelve mayúscula
print(string.replace('hello','bye'))	## Reemplaza una palabra del string por otra. .replace(Palabra,reemplazo)
print(string.count('l'))				## Cuenta las veces que aparece una letra o una palabra completa en el string
print(string.startswith('HELLO'))		## Devuele true o false dependiendo si el string comienza con dicha palabra o letra. ## Sensitive case
print(string.endswith('world')) 		## Devuele true o false dependiendo si el string termina con dicha palabra o letra. ## Sensitive case
print(string.split()) 					## Separa una string dependiendo del argumento que des ('' -> separa por espacios, ',' -> separa por comas)
print(string.find('d')) 				## Devuelve la posición en la que se encuentra una letra o una palabra dentro del string 
print(string.index('w'))				## Muestra el índice de la letra en función [contando desde 0] 
print(string.isnumeric())				## Devuelve true o false dependiendo si la string es enteramente numerica
print(string.isalpha())  				## Devuelve true o false dependiendo si la string es entermente alfanumerica


## Funciones para strings ##

print(len(string))						## Devuelve la longitud (numero) del string 
