

dict = {
	'0': 'banios',
	'1': 'salones'
}


class Persona:

	def __init__(self, nombre, apellido, dni, estado):
		self.nombre = nombre
		self.apellido = apellido
		self.dni = dni
		self.estado = estado


	def change_status(self, new):
		self.estado = new

class Empleado(Persona):

	def __init__(self, nombre, apellido, dni, estado, anio):
		super().__init__(nombre, apellido, dni, estado)
		self.anio = anio
		self.numero = numero
		self.curso = []

	def add_course(self, course):
		self.curso.append(course)


class Profesor(Persona):

	def __initi__(self, nombre, apellido, dni, estado, departamento):
		super().__init__(nombre, apellido, dni, estado)
		self.departamento = departamento

	def change_department(self, new):
		self.departamento = new



class Servicio(Persona):

	def __initi__(self, nombre, apellido, dni, estado, seccion):
		super().__init__(nombre, apellido, dni, estado)
		self.seccion = seccion

	def change_section(self, new):
		self.seccion = new


Empleado('Kevyn', 'Franco', 'XXXXXXX', '')




