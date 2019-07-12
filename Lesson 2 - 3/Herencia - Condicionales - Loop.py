class Alumno():
  def __init__(self,nombre,edad,sexo):
    self.nombre=nombre
    self.edad=int(edad)
    self.sexo=sexo

class Universidad(Alumno):
  def __init__(self,Alumno,uni):
    super().__init__(Alumno.nombre,Alumno.edad,Alumno.sexo)
    self.nombreUni=uni
  def getDatos(self):
    dicc={"Nombre": self.nombre,"Edad":self.edad,"Sexo": self.sexo,"Universidad": self.nombreUni}
    return dicc

lista=[]
num=0

a=input("Ingrese su nombre: ")
b=int(input("Ingrese su edad: "))
c=input("Ingrese su sexo: ")
d=input("Nombre de su universidad: ")

x=Alumno(a,b,c)
y=Universidad(x,d)

for i in range(5):
 lista.append(y)

for j in lista:
 #print(j.getDatos())
 print("---------------")
 for k,v in j.getDatos().items():
  print(str(k)+" : ",v)