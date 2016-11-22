def automataWebay(caracter,estado):
	if(estado==0):
		estado=estadoCero(caracter)
	elif(estado==1):
		estado=estadoUno(caracter)
	elif(estado==2):
		estado=estadoDos(caracter)
	elif(estado==3):
		estado=estadoTres(caracter)
	elif(estado==4):
		estado=estadoCuatro(caracter)
	elif(estado==5):
		estado=estadoCinco(caracter)
	elif(estado==6):
		estado=estadoSeis(caracter)
	elif(estado==7):
		estado=estadoSiete(caracter)

	return estado

def estadoCero(caracter):
	if (caracter=='w'):
		return 1
	elif (caracter=='e'):
		return 4
	else:
		return 0

def estadoUno(caracter):
	if(caracter=='w'):
		return 1
	elif(caracter=='e'):
		return 2
	else:
		return 0

def estadoDos(caracter):
	if(caracter=='w'):
		return 1
	elif(caracter=='e'):
		return 4
	elif(caracter=='b'):
		return 3
	else:
		return 0

def estadoTres(caracter):
	if(caracter=='w'):
		return 1
	elif(caracter=='e'):
		return 4
	elif(caracter=='a'):
		return 6
	else:
		return 0

def estadoCuatro(caracter):
	if(caracter=='w'):
		return 1
	elif(caracter=='e'):
		return 4
	elif(caracter=='b'):
		return 5
	else:
		return 0

def estadoCinco(caracter):
	if(caracter=='w'):
		return 1
	elif(caracter=='e'):
		return 4
	elif(caracter=='a'):
		return 6
	else:
		return 0

def estadoSeis(caracter):
	if(caracter=='w'):
		return 1
	elif(caracter=='e'):
		return 4
	elif(caracter=='y'):
		return 7
	else:
		return 0

def estadoSiete(caracter):
	if(caracter=='w'):
		return 1
	elif(caracter=='e'):
		return 4
	else:
		return 0
