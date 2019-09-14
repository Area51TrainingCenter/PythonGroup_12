class Gato():
  def __init__(self):
    self.paso = 0

  def trepar(self):
    pass
  
  def caminar(self):
    print('Camine 20 pasos')

  
  def maullar(self):
    print('Miau')


class Perro():
  def __init__(self):
    self.paso = 0

  def caminar(self):
    self.paso = self.paso + 20

  def ladra (self):
    print('Guau')
  

def pasearMascotas(mascota):
  for i in range(5):
    mascota.caminar()
  print("La mascota quedo en " + str(mascota.paso))

perro = Perro()
gato = Gato()

pasearMascotas(perro)
pasearMascotas(gato)


#Desarrollar lo siguente:
  #Ingreso de informacion sea hombre o  mujer (Clases)
  # que retorne datos en formato string (Funcion externa)
  #utilizar condificionales de validacion

class Hombre():
  def __init__(self, nombre, apellido, sexo, edad):
    self.nombre =  nombre
    self.apellido = apellido
    self.sexo = sexo
    self.edad = edad

  def concat_data(self):
    print("Hola mi nombre es " + str(self.nombre + " " + self.apellido) + " soy " + str(self.sexo) + " y tengo " + self.edad + " años")

  def get_sexo(self):
      print(self.sexo)


class Mujer():
  def __init__(self, nombre, apellido, sexo, edad):
    self.nombre =  nombre
    self.apellido = apellido
    self.sexo = sexo
    self.edad = edad

  def concat_data(self):
    print("Hola mi nombre es " + str(self.nombre + " " + self.apellido) + " soy " + str(self.sexo) + " y tengo " + self.edad + " años")

def get_data(element):
  element.concat_data()

mujer = Mujer('Carla', 'Ontaneda', 'Mujer', '18')
hombre = Hombre('Juan', 'Ontaneda', 'Hombre', '20')

get_data(mujer)
get_data(hombre)



from abc import ABC, abstractmethod

class abstracClassExample(ABC):
  @abstractmethod
  def do_something(self):
    print("Codigo - Codigo")


class OtherAbstractClass(abstracClassExample):
  def do_something(self):
    super().do_something()
    print("Main Code")

x = OtherAbstractClass()
x.do_something()







def multiplcar(num):
  return num*2

print(multiplcar(4))

response = lambda num, num2: (num*2)+num2
print(response(4, 5))





def multiplo(x):
  return True if x % 5 == 0 else False

numero = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(multiplo, numero)))


print(list(filter(lambda x: x % 5 == 0, numero)))


# Generar desarrollo que contemple lo siguente:

  #Clase Persona que reciba nombre, apellido y edad
  #Lista de objectos Persona
  #funcion filter para detectar a los mayores de 18


class Persona ():
  def __init__(self, nombre, apellido, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
  
  def __str__(self):
    return "{} de {} años".format(self.nombre, self.edad)

personas = [

  Persona('Leo','Edu', 19),
  Persona('Leo1','Edu', 17),
  Persona('Leo2','Edu', 20)

]

menores = filter(lambda persona: persona.edad < 18, personas)

for menor in menores:
  print(menor)


numero = [1,2,3,4,5,6,7,8,9,10]

def multiplicar(x):
  return x * 2

response = list(map(multiplicar,numero))

print(response)

response = list(map(lambda num: num * 2, numero))

print(response)

#########################333

from functools import reduce

Elements = [1,2,3,4,5,6,7,8,9,10]

def  do_sum(x1, x2):
  return( x1 + x2)

response = (reduce(do_sum,Elements))

print(response)

#############
print("Decorador")

def funcion(enviado):
  def nueva_funcion(a,b):
    print("Funcion suma llamada")
    return enviado(a, b)
  return nueva_funcion

@funcion
def agregar(a,b):
  return a+b
print(agregar(7, 5))


class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __add__(self, other):
    return Vector2D(self.x + other.x,  self.y + other.y)

  
first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

##################################

class SpecialString:
  def __init__(self, count):
    self.count = count

  def __truediv__(self, other):
    line = " = " * len(other.count)
    return "\n".join([self.count, line, other.count])

spam = SpecialString("spam")
hello = SpecialString("Hello Word")

print(spam / hello)


  class Vector2D:
    def __init__(self, x, y):
      self.x = x
      self.y = y
    
    def __add__(self, other):
      return Vector2D(self.x + other.x,  self.y + other.y)

    
  first = Vector2D(5, 7)
  second = Vector2D(3, 9)
  result = first + second
  print(result.x)
  print(result.y)

  ##################################

  class SpecialString:
    def __init__(self, count):
      self.count = count

    def __truediv__(self, other):
      line = " = " * len(other.count)
      return "\n".join([self.count, line, other.count])

  spam = SpecialString("spam")
  hello = SpecialString("Hello Word")

  print(spam / hello)





lista = [1, 2, 3, 4, 5, 6]
  
cubos = [valor **  3 for valor in lista]
print('Cubos de 1 al 4', cubos)


################################################


def pares():
  index = 1
  #Definimos un bucle infinito
  while True:
    #devolvemos un valor
    yield index*2
    index = index + 1


for i in pares():
  print(i)

  f = open("read.txt", "r")
print(f.read())
f.close()



f = open("write.txt","w")
print(f.write("Hola Mundo3"))
f.close()
