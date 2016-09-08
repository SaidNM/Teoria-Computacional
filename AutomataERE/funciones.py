import tkinter as tk
def texto():
	texto=input('Introduce un texto\n')
	return texto
def nuevo_texto():
	while True:
			try:
				seguir=input('1.-Si\n2.-No\nDesea iniciar el automata de nuevo: ')
				seguir=int(seguir)
			except:
				print('Introduce una opcion valida')
				continue
			if(seguir==1):
				break
			elif(seguir==2):
				exit()
			else:
				continue

def imprimir_palabras_ere(palabras):
	for palabra in palabras:
		print(palabra)

def leer_archivo():
	archivo=open("archivo.txt","r")
	lineas=str(archivo.readlines())
	archivo.close()
	return lineas
