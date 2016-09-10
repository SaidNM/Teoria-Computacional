import random

def menu():
	try:
		opcion=input("\t\t Paridad\n1.-Modo manual\n2.-Modo Automatico\n3.-Mostrar Diagrama\nElige una opcion: ")
		opcion=int(opcion)
		return opcion
	except:
		exit()
def nueva_cadena():
	try:
		conteo = input("1.-Nuevo conteo\n2.-salir ")
		conteo = int(conteo)
		return conteo
	except:
		print("opcion invalida")

def generarCadena():
	cardinalidad=cardinalidad_aleatoria()
	tamanio=0
	cadena=""
	while (tamanio<cardinalidad):
		num=num_aleatorio()
		num=str(num)
		cadena=cadena+num
		tamanio=tamanio + 1
	return cadena


	



def cardinalidad_aleatoria():
	numero = random.randrange(1,100)
	return numero
def num_aleatorio():
	bit = random.randrange(0,2)
	return bit