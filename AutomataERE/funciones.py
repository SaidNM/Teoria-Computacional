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

def imprimir_palabras_ere(palabras,fila,palabra):
	i=0
	for pala in palabras:
		fil=fila[i]
		fil=str(fil)
		pal=palabra[i]
		pal=str(pal)
		print("Palabra: " + pala+" fila: "+fil+" palabra numero: "+pal)
		i=i+1

def leer_archivo():
	archivo=open("archivo.txt","r")
	lineas=str(archivo.read())
	archivo.close()
	return lineas
