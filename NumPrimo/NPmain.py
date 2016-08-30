import primos
primos.iniciar_archivo()

opcion = primos.menu()

if (opcion == 1):
#Modo manual
	while True:
		numero = primos.numero()
		primos.iniciar_programa(numero)
		while True:
			op = primos.nuevo_conteo()
			if (op == 1):
				break
			elif (op == 2):
				exit()
			else:
				continue







