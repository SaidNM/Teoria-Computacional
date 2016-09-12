def automata(cadena):
	estados=[]
	trayectoria=[]
	estado=0
	for elemento in cadena:
		if (estado==0):
			estado=estadoCero(elemento,trayectoria)
			estados.append(trayectoria)
			print
		elif(estado==1):
			estado=estadoUno(elemento,trayectoria)
			estados.append(trayectoria)
		elif(estado==2):
			estado=estadoDOs(elemento,trayectoria)
			estados.append(trayectoria)

		else:
			return -1
	return estados

def estadoCero(elemento,trayectoria):
	if(elemento=='0'):
		trayectoria.append("q0")
		trayectoria.append("q1")
		return 1
	elif(elemento=='1'):
		trayectoria=[]
		trayectoria.append("q0")
		return 0
	else:
		return -1
def estadoUno(elemento,trayectoria):
	if(elemento=='0'):
		trayectoria=[]
		trayectoria.append("q0")
		return 0
	elif(elemento=='1'):
		trayectoria.append("q2")
		return 2
	else:
		return -1
def estadoDos(elemento,trayectoria):
	if(elemento=="0"):
		trayectoria=[]
		trayectoria.append("q0")
		return 0
	elif(elemento=="1"):
		trayectoria=[]
		trayectoria.append("q0")
		return 0
	else:
		return -1



