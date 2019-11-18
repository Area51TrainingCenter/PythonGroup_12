INTERBANK_ID = 2
BBVA_ID = 3
CREDISCOTIA_ID = 14

ERROR_MP = {
  'in_process': 'Error el pago se encuentra en proceso.',
  'pending_contingency': 'Estamos procesando el pago.',
  'pending_review_manual': 'En menos de 2 días hábiles te diremos por e-mail si se acreditó o si necesitamos más información.',
  'cc_rejected_bad_filled_card_number': 'Revisa el número de tarjeta.',
  'cc_rejected_bad_filled_date': 'Revisa la fecha de vencimiento.',
  'cc_rejected_bad_filled_other': 'Revisa los datos.',
  'cc_rejected_bad_filled_security_code': 'Revisa el código de seguridad.',
  'cc_rejected_blacklist': 'No pudimos procesar tu pago.',
  'cc_rejected_call_for_authorize': 'Debes autorizar al banco el pago del producto a Mercado Pago',
  'cc_rejected_card_disabled': '	Llama al banco para que active tu tarjeta.',
  'cc_rejected_card_error': 'No pudimos procesar tu pago.',
  'cc_rejected_duplicated_payment': 'Si necesitas volver a pagar usa otra tarjeta u otro medio de pago.',
  'cc_rejected_high_risk': 'Elige otro de los medios de pago, te recomendamos con medios en efectivo.',
  'cc_rejected_insufficient_amount': 'Tu tarjeta no tiene fondos suficientes.',
  'cc_rejected_invalid_installments': 'El banco no procesa pagos en cuotas.',
  'cc_rejected_max_attempts': 'Llegaste al límite de intentos permitidos.',
  'cc_rejected_other_reason': 'No se procesó el pago',
  'default': 'No se completo el pago'
}

ERROR_MP_STATUS = {
  106: 'Ingresa el número de tu tarjeta.',
  109: 'Elige un mes.',
  126: 'Elige un año.',
  129: 'Ingresa tu documento.',
  145: 'Ingresa el número de tu tarjeta.',
  150: 'Elige un mes.',
  151: 'Elige un año.',
  160: 'Ingresa tu documento.',
  204: 'Ingresa el número de tu tarjeta.',
  801: 'Elige un mes.',
  205: 'Ingresa el número de tu tarjeta.',
  208: 'Elige un mes.',
  209: 'Elige un año.',
  212: 'Ingresa tu documento.',
  213: 'Ingresa tu documento.',
  214: 'Ingresa tu documento.',
  220: 'Ingresa tu banco emisor.',
  221: 'Ingresa el nombre y apellido.',
  224: 'Ingresa el código de seguridad.',
  'E301': 'Hay algo mal en ese número. Vuelve a ingresarlo.',
  'E302': 'Revisa el código de seguridad.',
  316: 'Ingresa un nombre válido.',
  322: 'Revisa tu documento.',
  323: 'Revisa tu documento.',
  324: 'Revisa tu documento.',
  325: 'Revisa la fecha de expiración',
  326	: 'Revisa la fecha de expiración',
  'default': 'Error al realizar el pago vuelve a intentar',
}

info_personas = []

Data = ['nombre', 'apellido', 'dni', 'estado']

Tipos = {
  0: 'Estudiante',
  1: 'Profesores',
  2: 'Servicio',
  3: 'Salir'
}

curso = {
  0: 'Matematica',
  1: 'Lenguaje',
  2: 'Calculo'
}

Departamento = {
  0: 'Ciencias',
  1: 'Idiomas'
}

Asignado = {
  0: 'Blibioteca',
  1: 'Entrada',
}


class Persona(object):
  def __init__(self, nombre, apellido, dni, estado):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.estado = estado


class Estudiante(Persona):
  def __init__(self, nombre, apellido, dni, estado, curso):
    Persona.__init__(self, nombre, apellido, dni, estado)
    self.curso = curso

  def registro(self):
    dic = {
      'Nombre': self.nombre,
      'Apellido': self.apellido,
      'DNI': self.dni,
      'Estado': self.estado,
      'Curso': self.curso
    }
    info_personas.append(dic)

  def cambiar_estado(self, estado_nuevo):
    for i in info_personas:
      if i['DNI'] == self.dni:
        i['Estado'] = estado_nuevo

  def matricular_curso(self, curso_nuevo):
    for i in info_personas:
      if i['DNI'] == self.dni:
        i['curso_' + self.dni] = curso_nuevo


class Profesores(Persona):
  def __init__(self, nombre, apellido, dni, estado, departamento):
    Persona.__init__(self, nombre, apellido, dni, estado)
    self.departamento = departamento

  def registro(self):
    dic = {
      'Nombre': self.nombre,
      'Apellido': self.apellido,
      'DNI': self.dni,
      'Estado': self.estado,
      'Departamento': self.departamento
    }
    info_personas.append(dic)

  def cambiar_despacho(self, departamento_nuevo):
    for i in info_personas:
      if i['DNI'] == self.dni:
        i['Departamento'] = departamento_nuevo


class Servicio(Persona):
  def __init__(self, nombre, apellido, dni, estado, asignado):
    Persona.__init__(self, nombre, apellido, dni, estado)
    self.asignado = asignado

  def registro(self):
    dic = {
      'Nombre': self.nombre,
      'Apellido': self.apellido,
      'DNI': self.dni,
      'Estado': self.estado,
      'asignado': self.asignado
    }
    info_personas.append(dic)

  def cambiar_despacho(self, asignado_nuevo):
    for i in info_personas:
      if i['DNI'] == self.dni:
        i['Departamento'] = asignado_nuevo


bolean = True
temp_data = []
lista = []

while bolean:
  print("Selecciona Tipo")
  for k, v in Tipos:
    print("Selecciona {1} [{0}]".format(k, v))

  tipo_data = str(input("Ingrese {} : ".format("tipo")))

  if tipo_data == '3':
    bolean = False

  for i in Data:
    lista.append(str(input("Ingrese {} : ".format(i))))

    if tipo_data == '0':
      for k, v in curso:
        print("Selecciona {1} [{0}]".format(k, v))
    temp_value = input("Ingrese curso :")

    estudiante = Estudiante(lista[0], lista[1], lista[2], lista[3], temp_value)
    estudiante.registro()

    cambiar = input("Cambiar estado 'Si' - 'No' :")
    if cambiar.upper() == 'SI':
      temp_value = input("Ingrese estado :")
      estudiante.cambiar_estado(temp_value)

    cambiar = input("Matricular Nuevo curso 'Si' - 'No' :")
    if cambiar.upper() == 'SI':
      for k, v in curso:
        print("Selecciona {1} [{0}]".format(k, v))

      temp_value = input("Ingrese curso :")
      estudiante.cambiar_estado(temp_value)

  elif tipo_data == '1' :
      for k, v in Departamento.items():
        print("Selecciona {1} [{0}]".format(k, v))
      temp_value = input("Ingrese Departamento :")

      profesor = Profesores(lista[0], lista[1], lista[2], lista[3], temp_value)
      profesor.registro()
      cambiar = input("Cambiar despacho 'Si' - 'No' :")
      if cambiar.upper() == 'SI':
        for k, v in Departamento:
          print("Selecciona {1} [{0}]".format(k, v))
      temp_value = input("Ingrese Departamento :")
      profesor.cambiar_despacho(temp_value)

  else tipo_data == '2':
      for k, v in Asignado.items():
        print("Selecciona {1} [{0}]".format(k, v))
      temp_value = input("Ingrese Asignatura :")

      servicio = Servicio(lista[0], lista[1], lista[2], lista[3], temp_value)
      servicio.registro()

      cambiar = input("Cambiar despacho 'Si' - 'No' :")
      if cambiar.upper() == 'SI':
        for k, v in Asignado.items():
          print("Selecciona {1} [{0}]".format(k, v))
        temp_value = input("Ingrese Departamento :")
        profesor.cambiar_despacho(temp_value)

  print(info_personas)

