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
# modo automarico
elif(opcion == 2):
	while True:
		numero = primos.num_aleatorio()
		print(numero)
		primos.iniciar_programa(numero)
		while True:
			op = primos.opcion_aleatoria()
			print("1.-Nuevo conteo\n2.-salir ")
			if (op == 1):
				break
			elif(op==2):
				exit()
			else:
				continue









