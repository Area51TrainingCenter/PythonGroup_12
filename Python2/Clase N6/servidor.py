import sys, socket

ip = '127.0.0.1'

def enviar():
	s = socket.socket()
	s.connect((ip, 9996))
	mensaje = input("[>] ")
	s.send(mensaje.encode())
	if mensaje == 'quit':
		print('bye bye')
		s.close()
		sys.exit()

def recibir():
	s = socket.socket()
	s.bind(("", 9995))
	s.listen(1)
	sc, addr = s.accept()

	recibido = sc.recv(1024)
	if recibido == 'quit':
		print('bye bye')
		sc.close()
		s.close()
		sys.exit()
	print("Recibido:", recibido)
	sc.send(recibido)

def cambiar(word):
	if word == 'enviar':
		word = 'recibir'
	elif word == 'recibir':
		word = 'enviar'
	return word

accion = 'enviar'

while True:
	if accion == 'enviar':
		enviar()
	elif accion == 'recibir':
		recibir()
	accion = cambiar(accion)