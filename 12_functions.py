print('########################################################################')
print('FUNCTIONs')
# def funcion():
# 	print("Hello dude!!")    ## Declaración normal
# sumar = lambda n1, n2: n1 + n2		## Declaración más cool
# print(f"La suma de 10 + 30 = {sumar(10,30)}")
print('########################################################################')
def hello(text="none"):
	print(f"Hello {text}")    ## Declaración normal
hello('PEPEPE')
hello()
print('########################################################################')
def add(n1, n2):
	return n1 + n2
print(add(10, 20))
print(add(100, 20))
print('########################################################################')
sumar = lambda n1, n2: n1 + n2		## Funsion 'suma' - Declaración más cool
print(f"La suma de 10 + 30 = {sumar(10,30)}")
print('########################################################################')