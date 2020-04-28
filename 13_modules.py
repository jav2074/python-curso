# Modulos propios
# Modulos hechos por 3ros
# Modulos por defecto de Python

# PyPI - Modulos
# docs.python.org - Modulos o Library
print('########################################################################')
import datetime

print(datetime.date.today())        # fecha
print('########################################################################')
from datetime import timedelta, date      # importar modulos

print(timedelta(minutes=170))       # convert min a hs.
print(date.today())                 # fecha
print('########################################################################')
# Modulos propios
# https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/
from fmath import add, subs 

add(2, 4)
subs(2, 4)
print('########################################################################')
# Modulos hechos por 3ros # PyPI - Modulos
# pip --version
# python -m pip install --upgrade pip
# pip install colorama
from colorama import Fore, Style, init
init()
print(Fore.RED + 'Hola Colorama')
print(Fore.GREEN + "Recursos Python")
print('########################################################################')