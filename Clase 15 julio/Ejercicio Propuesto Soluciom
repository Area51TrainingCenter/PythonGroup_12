class Persona():
  __propiedades=[]
  def setNombre(self,a):
    self.__nombre=a

  def setAniosEgreso(self,a):
    self.__aniosEgreso=a

  def setPropiedades(self,a):
    prop={'direccion': a}
    self.__propiedades.append(prop)
  
  def getDatos(self):
    datos={'nombre':self.__nombre,'anios Egresado':self.__aniosEgreso,'propiedades':self.__propiedades}
    return datos

def aniosEgreso(a):
  while True:
    anios=input("Es Egresado (si/no): ")
    if anios=="si":
      anios=True
      break
    if anios=="no":
      anios=False
      a.setAniosEgreso(0)
      break  
  while anios:
    try:
     dif=int(input("hace cuantos anios: "))
     a.setAniosEgreso(dif)
     break
    except:
      print("Ingrese los anios")

x=input("Ingrese su nombre: ")
persona=Persona()
persona.setNombre(x)
x=input("direccion de su propiedad: ")
persona.setPropiedades(x)
aniosEgreso(persona)

print(dict(persona.getDatos()))