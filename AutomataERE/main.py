import automata

while True:
	try:
		opcion=input('1.-Introducir Texto\n2.-Leer un texto\n3.-Grafico del automata\nElige una opcion: ')
		opcion=int(opcion)
	except:
		print("Introduce una opcion valida")
		continue

	if (opcion==1):
		texto=input('Introduce un texto\n')
		palabras = automata.automata_ere(texto)
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
	elif(opcion==2):
		pass
	elif(opcion==3):
		pass
	else:
		print('Introduce una opcion valida')
		continue



