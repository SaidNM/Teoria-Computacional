import automata
import funciones
import Diagrama1


while True:
	try:
		opcion=input('1.-Introducir Texto\n2.-Leer un texto\n3.-Grafico del automata\nElige una opcion: ')
		opcion=int(opcion)
	except:
		print("Introduce una opcion valida")
		continue

	if (opcion==1):
		texto=funciones.texto()
		palabras = automata.automata_ere(texto)
		funciones.imprimir_palabras_ere(palabras)
		funciones.nuevo_texto()

	elif(opcion==2):
		texto=funciones.leer_archivo()
		palabras = automata.automata_ere(texto)
		funciones.imprimir_palabras_ere(palabras)
		funciones.nuevo_texto()
	elif(opcion==3):
		Diagrama1.crearDiagrama()
		

	else:
		print('Introduce una opcion valida')
		continue



