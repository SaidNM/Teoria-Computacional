import cadenas

cadenas.iniciar_archivo()

opcion = cadenas.menu()

if (opcion == 1):
#Modo manual
	while True:
		tamanio = cadenas.tamanio()
		cadenas.iniciar_programa(tamanio)
		while True:
			op = cadenas.nuevo_conteo()
			if (op == 1):
				break
			elif (op == 2):
				exit()
			else:
				continue


elif(opcion == 2):
#Modo automatico
	while True:
		num = cadenas.num_aleatorio()
		print (num)
		cadenas.iniciar_programa(num)
		while True:
			opa=cadenas.opcion_aleatoria()
			print("1.-Nuevo conteo\n2.-salir ", opa)

			if (opa == 1):
				break
			elif (opa == 2):
				exit()
			else:
				continue

else:

	print("Introduce una opcion valida")
	exit()




