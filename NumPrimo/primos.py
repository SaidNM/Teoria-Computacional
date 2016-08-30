import random

def menu():
	try:
		
			opcion = input("1.-Modo Manual\n2.-Modo Automatico ")
			opcion = int(opcion)
			return opcion
	except:
		print("Introduce una opcion valida")
def nuevo_conteo():
	try:
		conteo = input("1.-Nuevo conteo\n2.-salir ")
		conteo = int(conteo)
		return conteo
	except:
		print("opcion invalida")

def num_aleatorio():
	numero = random.randrange(1,1001)
	return numero
def opcion_aleatoria():
	opcion = random.randrange(1,3)
	return opcion
def iniciar_archivo():
	try:
		archivo = open("numprimo.txt","w")
		archivo.close
	except:
		exit()
def numero():
	try:
		num = input("Introduce un numero: ")
		num = int(num)
		return num
	except:
		print("No es un numero")
		exit()

def iniciar_programa(numero):
	archivo = open("numprimo.txt","a")

	primos = [2,3,5,7,11]
	lista = []
	binario = []
	
	if (numero >= 2):
		pass #aqui va la logica de saber si es numero primo o no xD xD
		
			
	else:
		print("no tiene numeros primos")
	
	archivo.close()

