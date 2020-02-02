def method_example():
  input("Ingreso informacion : ")


#method_example()


#def sumar(parametro, parametro2): # 2 
#  print(parametro2 + parametro) # 3

#sumar(2, 1) #1 

resultado = lambda num, num2: print(num +num2)
resultado(1, 2)
#print(f"El resultado de agregar + 1 a 2 es {resultado(2, 1)}")

def Multiplicar(num):
  print(num*2)

print(Multiplicar(2))
#######################################
lista = list()

def method(param):
  obj = input(f'Ingrese informacion {param} :')
  lista.append(obj)
  print(lista)

print(method("Numerica "))
#######################################
multiplicar = lambda data: lista.append(input(f'ingrese dato {data} : '))

multiplicar('numerico')

print(lista)

########################################

def AddFive(param):
  return print(param + 5)

AddFive(4)
AddFive(3)
AddFive(2)

#######################################

def AddFive2(param):
  return param + 5

lista = list()
lista.append(4)
lista.append(3)
lista.append(2)
addfive = map(AddFive2, lista)

print(list(addfive))

lista # 500 elementos

count = 0
while count < 500:
  AddFive(lista[count])
  count += 1

for obj in lista:
  AddFive(obj)

addfive = map(AddFive2, lista)


def residuo(param):
  return param % 2 == 0

result = list(filter(residuo, lista))

print(result)




##################################
lista = list()
lista.append(4)
lista.append(3)
lista.append(2)
lista.append(2)
lista.append(16)

###################################
#from functools import reduce
import functools

def AddFive2(param, param2):
  print(f'el primer elemento es : {param}')
  print(f'el segundo elemento es : {param2}')
  print(  print(f'el resultado es : {param + param2}'))
  return param + param2

result = functools.reduce(AddFive2, lista)

result2 = functools.reduce((lambda param, param2: param + param2), lista )

print(result)
print(f'Funcion lambda : ')
print(result2)

import functools

# 1
listobj = list()
while len(listobj) <=5:
  word = input('Ingresa texto : ')
  for obj in word.split(" "):
    listobj.append(obj)

def concant(param):
  return len(param)

result = map(concant, listobj)

print(list(result))


# 2
lista2 = [1, 2, 3, 4 ,5 ]
print(lista2)
def concat_num(param, param2):
  num = f'{param}{param2}'
  print(num)
  return num

result_num = functools.reduce(concat_num, lista2)

# 3
cadena = 'Hola mundo este es un nuevo dia judas'.split(" ")
def find(param):
  return param if param.startswith('j') else ''

result = filter(find, cadena)

print(list(result))


