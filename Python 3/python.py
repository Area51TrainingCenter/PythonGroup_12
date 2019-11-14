def funtion():
  pass

class name_class(object):
  def __init__(self, name, last_name):
    self.name = name
    self.last_name = last_name

  def support(self):
    print(self.name)


class_object = name_class('Kevyn', 'Franco')
class_object.support()


def funtion():
  pass

class name_class(object):
  def __init__(self, name, last_name):
    self.name = name
    self.last_name = last_name

  def support(self):
    print(self.name)


class_object = name_class('Kevyn', 'Franco')
class_object.support()


#Escribir una clase con un metodo de soporte que permita contar la cantidad de caracteres que contiene el texto ingresado.

class ejercicio1(object):

  def __init__(self, text):
    self.text = text
  
  def support(self):
    print(len(self.text))
  

val =  str(input("Ingrese texto: "))
class_object = ejercicio1(val)
class_object.support()

#Desarrollar dos clases que almacenen numeros pares y numeros impares en una lista. La clase par debe contener un metodo de soporte que retorne el valor al cubo y la clase impar debe contener un metodo de soporte que retorne el valor al cuadrado 

lista_par = []
lista_impar = []

class par:
  def __init__(self, par):
    self.value = par
  
  def cubo(self):
    print(self.value ** 3)


class impar:
  def __init__(self, impar):
    self.value = impar

  def cuadrado(self):
    print(self.value ** 2)


val = int(input('Ingrese numero: '))

if val % 2 == 0:
  par(val).cubo()
else:
  impar(val).cuadrado()

#Desarralloar lo siguente:
  #- Ingreso de informacion para hombres y mujeres (clases)
  #que retorne datos en formato string (metodo)
  # deben validar si es hombre o mujer



  

class Persona(object):
  def __init__(self, altura):
    self.altura = altura


class Alumno(object):
  def __init__(self, nombre, edad, sexo):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo


class Universidad(Alumno, Persona):
  def __init__(self, nombre, edad, sexo, uni, altura):
    #Herencia 1 padre
    #super().__init__(nombre, edad, sexo)
    #Herencia 2 padres
    Alumno.__init__(self,nombre, edad, sexo)
    Persona.__init__(self,altura)
    self.uni = uni

  def get_data(self):
    print("Nombre: {0} Edad : {1} Sexo: {2} Universidad: {3} Altura {4}".format(self.nombre, self.edad, self.sexo, self.uni, self.altura))

Universidad("Kevyn", "XX", "M", "Lima", "1.8M").get_data()

