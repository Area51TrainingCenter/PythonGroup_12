# Tenemos diferentes metodos magicos por ejemplo el mas comun __call__ puede ser llamado cuando se instancia una variable
# que contenga una clase declarada

class A():

     def __init__(self):
              print "init"

     def __call__(self):
              print "call"
        
          

a = A()
init
a()
call


#El metodo magico __add__ permite redefinir + lo que nos permite hacer una sumatoria de clases

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
first = Vector2D(5, 7)
second = Vector2D(3,9)
result = first + second
print(result.x)
print(result.y)

la traduccion seria x.__add__(y)



#El metodo magico __truediv__ nos permite redefinir la accion de dividir variable 

class SpecialString:
    def __init__(self, count):
        self.count = count
        
    def __truediv__(self, other):
        line = "=" * len(other.count)
        return "\n".join([self.count, line, other.count])
spam = SpecialString("spam")
hello = SpecialString("hello world!")
print(spam / hello)




#Ejemplo de otro metodo pagicos

__it__ para <
__le__ para <=
__eq__ para ==
__ne__ para !=
__gt__ para >
__ge__ para >=

