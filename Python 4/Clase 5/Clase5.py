    self.ruedas =  ruedas

class Vehiculo(object):
  def __init__(self, *args, **kwargs):
      self.placa = args[0]
      self.color = kwargs['color']
      self.tipo = kwargs['tipo']
  def get_placa(self):
    print(self.placa, self.ruedas)
  
  def get_color(self):
    return self.color

  def get_tipo(self):
    return self.tipo
###########

# vehiculo = Vehiculo('A8G025',color="Negro", tipo="Sedan")
# print(vehiculo.get_color())
# print(vehiculo.get_tipo())
# vehiculo.get_placa()

#####################################3

class Propietario(object):

  def __init__(self, name, last_name, document_number):
    self.name = name
    self.last_name = last_name
    self.document_number = document_number

  def get_owner_info(self):
    return f'{self.name} {self.last_name} {self.document_number}'



class Automovil(Vehiculo, Propietario):
  def __init__(self, ruedas, cilindrada, pasajeros, color, placa, tipo, *args):
    #super().__init__(placa,color=color, tipo=tipo)
    Vehiculo.__init__(self,placa,color=color, tipo=tipo)
    Propietario.__init__(self,args[0], args[1], args[2])
    self.ruedas =  ruedas
    self.cilindrada = cilindrada
    self.pasajeros = pasajeros

  def get_information(self):
    return f'la cantidad de ruedas es {self.ruedas} puede soportar {self.pasajeros} pasajeros y es de color {self.get_color()}, el dueño es {self.get_owner_info()}'



automovil = Automovil("4", "2000", "5", "Negro", "A8g025", "Sedan", "Jorger", "Suerez", "99999999")
print(automovil.get_information())
#automovil.get_placa()

#### Propiesta
## 1 Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones
#Añadir contacto X
#Lista de contactos X
#Eliminar contatos X
#Buscar contacto X
#Editar contacto X
#Cerrar agenda 

class Information(object):
  def __init__(self, *args,**kwargs):
    self.memory = []
    self.bye = "Bye"
    self.options = {
      1: self.add_contanct,
      2: self.delete_contact,
      3: self.list_contacts,
      4: self.search_contact,
      5: self.edit_contact,
      6: print(self.bye)
    }
  
  def add_contanct(self):
      name = input("Ingresar nombre de contacto : ")
      number = input("Ingresar numero de contacto : ")
      print("Guardando...")
      self.memory.append({number: name})
  
  def delete_contact(self):
    number = input("Ingresar numero de contacto : ")
    
    if len(self.memory) == 0:
      print("Sin contactos")
    else:
      for index, contact in enumerate(self.memory):
        if contact[number]:
          self.memory.remove(contact)
    print("Se elimino contacto")
  
  def list_contacts(self):
    if len(self.memory) == 0:
      print("Sin contactos")
    else:
      for contact in self.memory:
        print(f'los datos del contacto son {contact}')
  
  def search_contact(self):
    if len(self.memory) == 0:
      print("Sin contactos")
    else:
      number = input("Ingrese numero de contacto a buscar")
      for contact in self.memory:
        if contact[number]:
          print(contact)
  
  def edit_contact(self):
    if len(self.memory) == 0:
      print("Sin contactos")
    else:
      number_edit = input("Ingrese numero de contacto a editar")
      name_edit = input("Ingrese nuevo nombre de contacto")
      for contact in self.memory:
        if contact[number_edit]:
          contact[number_edit] = name_edit
      print("Contacto Editado")

  def options_menu(self):
    text_options = ["Agregar", "Borrar", "Listar", "Buscar", "Editar", "Salir"]
    for num in range(6):
      print(f'{num + 1} | {text_options[num]} contacto')
    
    while True:
      option = int(input("Seleccione Opcion : "))
      if option == 6:
        False
      else:
        temp = self.options[option]
        temp()


information =  Information().options_menu()
information.options_menu()



###############



from abc import ABC, abstractclassmethod

class AbstractClass(ABC):
  @abstractclassmethod
  def hacer_algo(self):
    print("Estoy haciendo algo ....")

  def hacer_otra_cosa(self):
    print("hice otra cosa")

class AnthoerClass(AbstractClass):
  def otra_cosa(self):
    print("hola")
  def hacer_algo(self):
    super().hacer_algo()
    print("Hicer algito mas ")

sonclass = AnthoerClass()
sonclass.hacer_algo()


http://notepad.pw/clase5python