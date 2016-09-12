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
	numero = random.randrange(30)
	return numero
def opcion_aleatoria():
	opcion = random.randrange(1,3)
	return opcion

def iniciar_archivo ():
	try:
		archivo = open("cadenas.txt","w")
		archivo.close()
	except:
		exit()
def tamanio():
	try:
		tam = input("Introduce el tamaño de la cadena:")
		tam = int(tam)
		return tam
	except:
		print("No es un numero")
		exit()

def iniciar_programa(tamanio):
	cadena=['0','1']
	cad_aux=[]
	cont=0
	continuar = True

	archivo = open("cadenas.txt","a")
	archivo.write("S = { e")

	for indice in range (1,tamanio+1):
		print ("Va en ",indice)
		cad_aux = [0] * indice

		while continuar:
			archivo.write(", ")

			for i in range(indice):
				archivo.write(cadena[cad_aux[i]])
			cont = 0
			while (cont < indice):
				cad_aux[cont]=cad_aux[cont] + 1
				if (cad_aux[cont] > 1):
					cad_aux[cont] = 0
				else:
					break
				cont = cont +1
			if (cont>=indice):
				cad_aux=[]
				break
	archivo.write(" }\n")
	archivo.close() 

		
