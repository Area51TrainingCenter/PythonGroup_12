#var = 1
#var2 = 'String'
#var3= 1.2


#print(type(var))
#print(type(var2))
#print(type(var3))

#var = '1'
#print(type(var))
#print(type(var2))
#print(type(var3))


##### ################# ########
#numero1 = input('Ingresar primer numero :')

#numero2 = input('Ingresar segundo numero :')

#print(numero1)
#print(numero2)

#print('Los numero son iguales :', numero1 == numero2)

#print('Los numeros son diferentes :', numero1 != numero2)

#print('El primer numero es mayor que el segundo :', numero1 > numero2)

#print('El segundo numero es mayor o igual que el segundo :', numero1 <= numero2)

#Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False).

#Cadena = 'Hola Mundo'

#print(len(Cadena))

#cadena = input('Ingresar Cadena de texto: ')
#if( len(cadena) >=3 and
#    len(cadena) < 10):
#  print(True)
#else:
#  print(False)


#try:
#  var = int(input('Ingresar Numero : '))
#  print(var)
#except:
#  print('Valor Error')


#Realizar un desarrollo que permita ingresar una cadena de texto y validar si la cantidad de elementos en menor o igual que 15 caso contrario solicitar otra cadena de texto que cumpla con la condicion  

#boolean = True

#while boolean:

#  var = str(input('Ingresar Cadena de texto: '))

#  if len(var) <= 15 :
#    print('Cumple')
#    boolean = False
#  else:
#    print('No cumple')


#Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

#Guarda en una variable numero_magico el valor 12345679 (sin el 8)

#Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9

#Multiplica el numero_usuario por 9 en sí mismo

#Multiplica el numero_magico por el numero_usuario en sí mismo

#Finalmente muestra el valor final del numero_magico por pantalla


#numero_magico = 12345679

#numero_usuario = int( input("Introduce un número #del 1 al 9: "))

#numero_usuario *= 9

#print(numero_usuario)

#numero_magico *= numero_usuario


#print("El número mágico es: ", numero_magico)

# lista = []

# lista = ['1', '2', '3']

# print( lista )


# lista = ['1', 2, '3']

# print( lista[1] )

# lista = [1, 2, [3, 4]]

# print(lista[2][1])

# lista.append(5)

# print(lista)

# lista.append([6, 7])

# print(lista)

# lista[0] = 100

# print(lista)

# tupla = (1, '2', 3)

# print( "La tupla es : ", tupla)

# dictt = {}

# dictt['valor_1'] = 'primer valor'

# print("Este es un diccionario: ", dictt)

# print(dictt['valor_1'])

# dictt['valor_2'] = 'segundo valor'

# print("Este es un diccionario: ", dictt)
# print("Esta es un valor {0} y {1}".format('1', '2'))

# print(dictt['valor_2'])

# new_list = list()
# new_tuple = tuple()
# new_dict = dict()

# print(new_list)

#Crea una lista con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la lista, muestra el contenido de esa posición sino muestra un mensaje de error.

#El programa termina cuando el usuario introduce un cero.

# meses = ['Enero', "Febrero", "Marzo"]
# boolean = True
# while boolean:
#   var = int(input('Ingresar numero : '))

#   if var == 0 or len(meses) == var:
#     print("bye")
#     boolean = False
#   else:
#     print("El mes es: ", meses[var])

#Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
lista = []
while True:
  var = int(input('Ingresar elemento a lista: '))
  
  if var == 0:
    break

  lista.append(var)
lista.sort()
print(lista)

#Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán meter nombres repetidos.





