#codigo ascii del 0-1   "48-49"
def automata(cadena,archivo):
	estado=0

	for bit in cadena:
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
		print("Q0 -- %s -->Q2" %elemento)
		return 2
	elif(elemento=="1"):
		print("Q0 -- %s -->Q1" %elemento)
		return 1
	else:
		return -1
def estadoUno(elemento):
	if (elemento=="0"):
		print("Q1 -- %s -->Q3" %elemento)
		return 3
	elif(elemento=="1"):
		print("Q1 -- %s -->Q0" %elemento)
		return 0
	else:
		return -1

	
def estadoDos(elemento):
	if(elemento=="0"):
		print("Q2 -- %s -->Q0" %elemento)
		return 0
	elif(elemento=="1"):
		print("Q2 -- %s -->Q3" %elemento)
		return 3
	else:
		return -1

def estadoTres(elemento):
	if(elemento=="0"):
		print("Q3 -- %s -->Q1" %elemento)
		return 1
	elif(elemento=="1"):
		print("Q3 -- %s -->Q2" %elemento)
		return 2
	else:
		return -1



