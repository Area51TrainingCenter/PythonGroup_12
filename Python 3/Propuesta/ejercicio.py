hasta el momento dos trasacciones de tarea


info_personas = []

Data = ['nombre', 'apellido', 'dni', 'estado']

Tipos = {
	0 : 'Estudiante',
	1 : 'Profesores',
	2 : 'Servicio',
	3 : 'Salir'
}

curso = {
	0 : 'Matematica',
	1 : 'Lenguaje', 
	2 : 'Calculo' 
}

Departamento = {
	0 : 'Ciencias',
	1 : 'Idiomas'
}

Asignado = {
	0 : 'Blibioteca',
	1 : 'Entrada',
}


class Persona(object):
	def __init__(self, nombre, apellido, dni, estado):
		self.nombre =  nombre
		self.apellido = apellido
		self.dni = dni
		self.estado = estado


class Estudiante(Persona):
	def __init__(self, nombre, apellido, dni, estado, curso)
		Persona.__init__(self,nombre, apellido, dni, estado)
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

while bolean:
	print("Selecciona Tipo")
	for k,v in Tipos:
		print("Selecciona {1} [{0}]".format(k, v))
	
	tipo_data = str(input("Ingrese {} : ".format("tipo")))

	if tipo_data == '3':
		bolean = False

	for i in Data:
		temp_data.append(str(input("Ingrese {} : ".format(i)))

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
		
	elif tipo_data == '1':
		for k, v in Departamento:
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
		for k, v in Asignado:
			print("Selecciona {1} [{0}]".format(k, v))
		temp_value = input("Ingrese Asignatura :")
		
		servicio = Servicio(lista[0], lista[1], lista[2], lista[3], temp_value)
		servicio.registro()

		cambiar = input("Cambiar despacho 'Si' - 'No' :")
		if cambiar.upper() == 'SI':
			for k, v in Asignado:
				print("Selecciona {1} [{0}]".format(k, v))
			temp_value = input("Ingrese Departamento :")
			profesor.cambiar_despacho(temp_value)
	

	print(info_personas)	
