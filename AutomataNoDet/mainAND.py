import AND
import DiagramaAND
import random

def menu():
	try:
		opcion=input("1.-Ingresar cadena\n2-Generar cadena\n3.-Mostrar diagrama\nElija una opcion: ")
		opcion=int(opcion)
		return opcion
	except:
		print("Error")
		exit()

def ingresarCadena():
	cadena=input("Ingrese una cadena binaria: ")
	return cadena
def generarCadena():
	cardinalidad=random.randint(1,1000)
	tamanio=0
	cadena=""
	while (tamanio<cardinalidad):
		num=num_aleatorio()
		num=str(num)
		cadena=cadena+num
		tamanio=tamanio + 1
	return cadena
def num_aleatorio():
	num=random.randint(0,1)
	return num
#--------------------------------------
op=menu()
if(op==1):
	cadena=ingresarCadena()
	estados=AND.automata(cadena)
	if(estados==-1):
		print("no es cadena binaria")
		exit()
	for es in estados:
		print (es)

elif(op==2):
	cadena=generarCadena()
	print(cadena)
elif(op==3):
	DiagramaAND.mostrarAND()
else:
	print("opcion invalida")

