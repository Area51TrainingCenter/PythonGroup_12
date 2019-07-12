#Los decoradores alteran de manera dinámica la funcionalidad de una función,
#método o clase sin tener que hacer subclases o cambiar el código fuente de la clase decorada


# Decoradores en forma de función

# El nombre de la funcion es el nombre del decorador y recibe la funcion que decora (print_text).
def decor(func):
    def wrap():
        print("="*12)
        func()
        print("="*12)
    return wrap

@decor
def print_text():
    print("Hola Mundo!!!")




def decorador(func): #Creamos la función decorador (A) con el arg func
    def nueva_funcion(): #Creamos la nueva función (C)
        print ("Perro dice:")#Añadimos una modificación a la función (B) dentro de (C)
        func() #Aquí estamos incluyendo la función (B) que le dimos como argumento a (A)

    return nueva_funcion #Para crear (C)

@decorador #Decoramos la función
def saluda():
    print("Guau!")
saluda()



# Define decorador
def decorador1(funcion):
    # Define función decorada
    def funciondecorada(*param1, **param2):
        print('Inicio', funcion.__name__)
        funcion(*param1, **param2)
        print('Fin', funcion.__name__)
    return funciondecorada
    
def suma(a, b):
    print(a + b)

suma2 = decorador1(suma)
suma2(1,2)
suma3 = decorador1(suma)
suma3(2,2)

# Otra forma más elegante, usando @:

@decorador1
def producto(arg1, arg2):
    print(arg1 * arg2)

producto(5,5)
