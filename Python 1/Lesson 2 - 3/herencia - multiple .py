#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#La herencia multiple como le explique en clase se hereda dentro del hijo y para iniciarlizar
#el hijo se realizar siguendo la nomeclatura clase.__init__(self,parametros). En el siguente 
#ejemplo se muestra lo aprendido en clase. 

class Estudiante(object): 
    def __init__(self, edad, nombre):
        self.edad = edad 
        self.nombre = nombre 
 
class Instituto(object):
    def __init__(self, nombre_insti):
      self.insti = nombre_insti
    def presentarinstituto (self):
        print("""Estudio en el Instituto """ + self.insti)
 
class Derecho (Estudiante, Instituto):
    def __init__(self, edad, nombre, insti): 
      Estudiante.__init__(self,edad,nombre)
      Instituto.__init__(self, insti)
    def presentarse(self): 
       print (("""Soy"""), (self.nombre), 
       ('tengo'), (self.edad), ('años'),("""y estudio Derecho"""))
       
 
 
Manuel = Derecho(26, 'Manuel Contreras', 'Area51')
Manuel.presentarse()
Manuel.presentarinstituto()