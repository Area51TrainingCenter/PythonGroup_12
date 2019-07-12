# Las clases abstractas tiene como objetivo servir de estructuras base para 
# las herencias, es decir, generar metodos y atributos que los hijos puedan consumir y 
# mantener un orden, un ejemplo claro pueden ser el ejemplo de polimorfismo visto en clase
# a las clases Perro y Gato podrian heredar clases abstractas que a su vez puedan ser heredadas
# por la clase Pasear_Mascotas.

# En el ejemplo inferior vemos que se tiene una clase abstracta 'AbstractClassExample'
# con un metodo abstracto 'do_someting' y dentro del metodo una sentencia basica
# por herencia podemos acceder a atributos y metodos del padre en la clase AnotherSubclass
# la caracteristica principal de una clase abstracta es que nos permite sobre escribir 
# el metodo abstracto, porque como se vio en clase al nosotros instanciar la clase padre
# abstracta nos retornaba un mensaje de error, pero al redefinir el metodo podiamos acceder
# de manera normal, ahora las clases abstractas nos permite definir piezas de codigo que
# pueden ser accedidas unicamente desde el hijo cuando hemos redefinido la clase abstracta
# en el ejemplo vemos que. 'do_someting' existe en la clase padre e hijo pero podemos
# acceder a la informacion del metodo en el padre a travez de la clase super() solo cuando 
# es redefinido les pido que hagan pruebas e intenten instanciar el metodo abstacto sin
# que sea redefinido en el hijo para que observen el potencial de la clase abstracta.


from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
    
    @abstractmethod
    def do_something(self):
        print("Some implementation!")
        
class AnotherSubclass(AbstractClassExample):
    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")
        
x = AnotherSubclass()
x.do_something()