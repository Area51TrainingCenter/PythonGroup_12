#Las funciones lambda tienen como finalidad ser funciones de corta sentencia, es decir son funciones creadas sobre la marcha
# el esiguente ejemplo refleja como definir esta funcion que no posee una estructura tipica de funciones

lambda argumentos: resultado

doblar = lambda num: num*2

doblar(2)

#Resultado:
	4


#La funcion map toma una función y un iterable como argumentos, y devuelve un nuevo iterable con la función 
#aplicada a cada argumento . 

#Ejemplo del operador Map
def add_five(x):
    return x + 5

nums = [11, 25, 34, 100, 23]
result = list(map(add_five, nums))
print(result)

#Resultado:
[16, 30, 39, 105, 28]



#La funcion filter  ofrece una forma elegante de filtrar todos los elementos de una lista, para los que la función de 
#función devuelve True.  

#Usando el operador Filter
nums = [0, 2, 5, 8, 10, 23, 31, 35, 36, 47, 50, 77, 93]
result = filter(lambda x: x % 2 == 0, nums)
print(result)

#Resultado:
[2, 8, 10, 36, 50]


#La funcion reduce toma como argumentos una funcion con dos o mas parametros y una lista de elementos y obtiene
#Usando el operado filter
from functools import reduce #en python3 reduce se encuentra en modulo functools

nums = [47,11,42,13]
result = reduce(lambda x, y: x + y, nums)
print(result)




#Los generadores son funciones que nos permitirán obtener sus resultados poco a poco. Es decir, 
#cada vez que llamemos a la función nos darán un nuevo resultado. 

# Definimos nuestra función
def pares():
    index = 1
    # En este caso definimos un bucle infinito
    while True:
        # Devolvemos un valor
        yield index*2
        index = index + 1


for i in pares():
    print(i)


