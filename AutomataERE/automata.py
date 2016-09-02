def automata_ere(texto):
	estado=0
	palabras_ere=[]
	auxiliar_palabra = ''

	for caracter in texto:
		aux_caracter = caracter.lower()

		if (estado ==0):
			estado = estadoCero(aux_caracter)
		elif(estado==1):
			estado= estadoUno(aux_caracter)
		elif(estado==2):
			estado= estadoDos(aux_caracter)
		elif(estado==3):
			estado= estadoTres(aux_caracter)

		if(ord(aux_caracter)>=97 and ord(aux_caracter)<=122):
			auxiliar_palabra = auxiliar_palabra + aux_caracter
			if (estado==-1):
				estado =0
				auxiliar_palabra=''
		else:
			if(estado ==-1):
				palabras_ere.append(auxiliar_palabra)
				auxiliar_palabra=''
				estado=0	
			else:
				estado=0
				auxiliar_palabra = ''
	if(estado==3):
		palabras_ere.append(auxiliar_palabra)
	return palabras_ere

def estadoCero(caracter):
	if(caracter =='e'):
		print('Q0--->Q1')
		return 1
	else:
		print('Q0--->Q0')
		return 0
	
def estadoUno(caracter):
	if(caracter == 'e'):
		print('Q1--->Q1')
		return 1
	elif(caracter == 'r'):
		print('Q1--->Q2')
		return 2
	else:
		print('Q1--->Q0')
		return 0

def estadoDos(caracter):
	if(caracter == 'e'):
		print('Q2--->Q3')
		return 3
	else:
		print('Q2--->Q0')
		return 0
	
def estadoTres(caracter):
	if(caracter == 'r'):
		print('Q3--->Q2')
		return 2
	elif(caracter == 'e'):
		print('Q3--->Q1')
		return 1
	else:
		return -1


#ASCII letras minusculas 97-122