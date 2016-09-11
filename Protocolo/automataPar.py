#codigo ascii del 0-1   "48-49"
def automata(cadena):
	estado=0

	for bit in cadena:
		if(bit ==" "):
			break
		if(estado==0):
			estado=estadoCero(bit)
		elif(estado==1):
			estado=estadoUno(bit)
		elif(estado==2):
			estado=estadoDos(bit)
		elif(estado==3):
			estado=estadoTres(bit)
		
		

	if(estado==0):
		return 1
	elif(estado==-1):
		return -1
	else:
		return 0


def estadoCero(elemento):
	if(elemento=="0"):
		return 2
	elif(elemento=="1"):
		return 1
	else:
		return -1
def estadoUno(elemento):
	if (elemento=="0"):
		return 3
	elif(elemento=="1"):
		return 0
	else:
		return -1

	
def estadoDos(elemento):
	if(elemento=="0"):
		return 0
	elif(elemento=="1"):
		return 3
	else:
		return -1

def estadoTres(elemento):
	if(elemento=="0"):
		return 1
	elif(elemento=="1"):
		return 2
	else:
		return -1



