#1 Escribir la función titulo(), la cual recibe un string y 
#lo retorna convirtiendo la primera letra de cada palabra a 
#mayúscula y las demás letras a minúscula, dejando inalterados 
#los demás caracteres. Precondición: el separador de palabras es 
#el espacio: " ". Agregar doctests con suficientes casos de 
#prueba para validar que la función retorna el valor esperado 
#ante distintos argumentos.

# listar archivos windowns "dir", otros "ls"
# acceder a carpeta "cd nombre_de_carpeta"

def titulo(palabra):
	resultado = ''
	if len(palabra.split(" ")) > 1:
		for p in palabra.split(" "):
			resultado += f'{p.capitalize()} ' # Primer caracter en mayuscula y el resto minuscula
	return resultado if resultado != '' else palabra.capitalize()

lista_palabras = ["hola zentrun", "mundo", "area51"]

resultado = map(titulo, lista_palabras)

print("Ejecutando....")
print(" ".join(list(resultado)))

http://notepad.pw/clasesyobjectospython


class Person(object):

  def __init__(self, name, school, last_name):
    self.name = name
    self.school = school
    self.last_name = last_name
    
  def print_name(self):
        print(self.name)
  def print_school(self):
        print(self.school)

jorge = Person("Jorge", "universidad de la vida", "Quispe")

jorge.print_name()
# jorge.name = 'Jorge'
# jorge.school = 'Universidad de la vida'
# jorge.last_name = 'Quispe'


class Person(object):

  def __init__(self, name, school, last_name):
    self.name = name
    self.school = school
    self.last_name = last_name
    
  def print_name(self):
        print(self.name)
  def print_school(self):
        print(self.school)

jorge = Person("Jorge", "universidad de la vida", "Quispe")

jorge.print_name()
# jorge.name = 'Jorge'
# jorge.school = 'Universidad de la vida'
# jorge.last_name = 'Quispe'



# 1 y 2 propuesta resumida
class Number(object):
  def __init__(self, param):
    self.param = param
    self.dict_rome = {1: "I"}
    self.dict_ara = {"I": 1}
  
  def convert_to_rome(self):
    return self.dict_ara[self.param]
  
  def convert_to_ara(self):
    return self.dict_rome[self.param]

number_ara = Number("I")
number_rome = Number(1)

print(number_ara.convert_to_rome())
print(number_rome.convert_to_ara())


#### Bonus

class Support(object):
  def __init__(self, *args):
    self.param = args[0][0]
    self.param2 = args[0][1]

  def get_par(self):
    return f'{self.param} {self.param2}' 


support = Support( [input(f"Ingreso de informacion {i}") for i in range(2)] )
print(support.get_par())




# 3 propuesta

#Escribir una clase en python para encontrar la validez de una cadena de paréntesis, '(', ')', '{', '}', '['  ']. Los paréntesis deben aparecer en el orden correcto, por ejemplo "()" y "()[]{}" son validos, pero "[)", "({[)]" y "{{{" son inválidos.


# 3 propuesta

#Escribir una clase en python para encontrar la validez de una cadena de paréntesis, '(', ')', '{', '}', '['  ']. Los paréntesis deben aparecer en el orden correcto, por ejemplo "()" y "()[]{}" son validos, pero "[)", "({[)]" y "{{{" son inválidos.

import random

class Support(object):
  def __init__(self, *args):
    self.param = args[0]

  def get_par(self):
    list_objective_left = ["{", "[", "("]
    list_objective_right = ["}", "]", ")"]
    chain = ''
    for element in self.param:
      if element in list_objective_left:
        chain += element
      elif element in list_objective_right:
        chain += element

    return chain
  #Salida: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
  def combination(self):
    list_result = [[]]
    while True:
      element = random.choice(self.param)
      element2=  random.choice(self.param)
      element3=  random.choice(self.param)

      if [element] not in list_result:
        list_result.append([element])
      elif [element, element2] not in list_result:
        list_result.append([element, element2])
      elif [element, element2, element3] not in list_result:
        list_result.append([element, element2, element3])

      if len(list_result) == 8:
        break
    return list_result

#Ejer 3
support = Support("'(', ')', '{', '}', '['  ']")
print(support.get_par())

#Ejer 4

support = Support( [4, 5, 6] )
print(sorted(support.combination()))


class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

      
class Seguro():

  def __init__(self, placa, precio):
    self.placa = placa
    self.precio = precio

class Coche(Vehiculo, Seguro):

  def __init__(self,color, ruedas, velocidad, cilindrada, placa, precio):
    super().__init__(color, ruedas)
    Vehiculo.__init__(self, color, ruedas)
    Seguro.__init__(self, placa, precio)
    self.velocidad = velocidad
    self.cilindrada = cilindrada

  def get_choche_attr(self):
    return f'{self.color} {self.ruedas}'
  

coche = Coche("negro", "4", "120", "2000")
print( coche.get_choche_attr() ) 