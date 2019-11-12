#Numero = 932588880
#Correo = Bl4ze89@gmail.com


#def Sumar(parametro1, parametro2):
#  return parametro1 + parametro2


#print(Sumar(2, 2))


def Multiplicar(num):
  return num*2
print ("Esta es una funcion normal", str(Multiplicar(2)))



doblar = lambda num: num*2

print("Esta es una funcion de orden superior", str(doblar(2)))

sumar = lambda p1, p2 : p1 + p2

print(sumar(2, 2))

#Funcion Map
def add_five(x):
  return x + 5

#nums = []
nums = [11, 25, 34, 100, 23]

result = map(add_five, nums)
list()
tuple()
dict()
print(list(result))

##Funcion Filter
nums = [11, 25, 34, 100, 23]

def dividir(x):
  return x % 2 == 0

result = filter(lambda x: x % 2 == 0, nums)

#result = filter(dividir, nums)

print(list(result))

##

# reduce
from functools import reduce

nums = [47, 11, 42, 13]
        #58 + 42 = 
def sumar(x, y):
  return x + y 

result = reduce(lambda x, y: x + y, nums)

result = reduce(sumar, nums)

print(result)

#Funcion Compresora

if 2 == 2:
  print ("Hola Mundo")
else:
  print("Hola Luna")

result = "Hola Mundo" if 2 == 2 else "Hola Luna"

lista = []

for valor in nums:
    lista.append(valor ** 3)

cubos = [valor ** 3 for valor in nums]

print(list(cubos))


from functools import reduce
############# Ej. Tipo #####################
#1 - Utilizar la función incorporada map() para crear una función que retorne una lista con la longitud de cada palabra (separas por espacios) de una frase. La función recibe una cadena de texto y retornara una lista. # .split()
"""lista = []
while len(lista) < 5 :
  variable = str(input("Ingresar palabra:"))
  variable = variable.split(" ")
  for y in variable:
    lista.append(y)

def contar_caracteres(x):
  return len(x)

result = map(contar_caracteres, lista)

print(list(result)) """

#2 - Crear una función que tome una lista de dígitos y devuelva al número al que corresponden. Por ejemplo [1,2,3] corresponde a el numero ciento veintitrés (123). Utilizar la función reduce.
lista = []
while len(lista) < 5 :
  variable = int(input("Ingresar Numero :"))
  lista.append(variable)

num = ''

def concatenar_numeros(x, y):
  num = str(x) + str(y)
  return num

result = reduce(concatenar_numeros, lista)

print(result)


#3 - Crear una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Utilizar la función filter.

lista = []
while len(lista) < 5 :
  variable = str(input("Ingresar palabra:"))
  variable = variable.split(" ")
  for y in variable:
    lista.append(y)

def palabras(x):
  return x.startswith("k") 

result = filter(palabras, lista)

print(list(result))


# Decorador

def decorador(func):
  def nueva_funcion(): #C
    print("El perro dice :") #D
    func() #E
  return nueva_funcion #B

#Funcion decorada
@decorador
def saluda(): #F
  print("Guau!") #G

saluda() #A

#Funcion decorada traducida
decorador(saluda())

def decorador(func):
  def nueva_funcion(parametro1, parametro2):
    print("=" * 12)
    func(parametro1, parametro2)
    print("=" * 12)
  return nueva_funcion


def suma(a, b):
  print(a + b)

suma_parametro = decorador(suma)
suma_parametro(2,4)

@decorador
def suma(a, b):
  print(a + b)

suma(2, 4)
