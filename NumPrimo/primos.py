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

	primos = [2,3,5,7,11,13,17,19,23,29,31,47,53]
	binario = []	
	obtener_primos(primos,binario,archivo,numero)
	escribir_archivo_binario(archivo,binario)
	archivo.close()

def obtener_primos(primos,binario,archivo,numero):
	archivo.write("{ ")
	if (numero >= 2):
		for numero in range(2,numero+1):
			cont=0
			for valor in primos:
				if (numero == valor):
					archivo.write(str(numero)+", ")
					binario.append(bin(numero))
					break
				else:
					mod = numero % valor
					if(mod == 0):
						break
					else:
						if(cont<len(primos)):
							cont = cont +1
							if (cont == (len(primos)-1)):
								archivo.write(str(numero))
								archivo.write(", ")
								binario.append(bin(numero))
								break
							else: 
								continue

		archivo.write(" }\n")
			
	else:
		print("no tiene numeros primos")

def escribir_archivo_binario(archivo,binario):
	archivo.write("{ ")
	for num_bin in binario:
		archivo.write(str(num_bin)+",")
	archivo.write("}\n")

