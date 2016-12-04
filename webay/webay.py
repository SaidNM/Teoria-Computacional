def automataWebay(caracter,estado,archivo):
	if(estado==0):
		estado=estadoCero(caracter,archivo)
	elif(estado==1):
		estado=estadoUno(caracter,archivo)
	elif(estado==2):
		estado=estadoDos(caracter,archivo)
	elif(estado==3):
		estado=estadoTres(caracter,archivo)
	elif(estado==4):
		estado=estadoCuatro(caracter,archivo)
	elif(estado==5):
		estado=estadoCinco(caracter,archivo)
	elif(estado==6):
		estado=estadoSeis(caracter,archivo)
	elif(estado==7):
		estado=estadoSiete(caracter,archivo)

	return estado

def estadoCero(caracter,archivo):
	if (caracter=='w'):
		archivo.write('q0--w-->q1\t')
		return 1
	elif (caracter=='e'):
		archivo.write('q0--e-->q4\t')
		return 4
	else:
		archivo.write('q0--%s-->q0\t' %caracter)
		return 0

def estadoUno(caracter,archivo):
	if(caracter=='w'):
		archivo.write('q1--w-->q1\t')
		return 1
	elif(caracter=='e'):
		archivo.write('q1--e-->q2\t')
		return 2
	else:
		archivo.write('q1--%s-->q0\t' % caracter)
		return 0

def estadoDos(caracter,archivo):
	if(caracter=='w'):
		archivo.write('q2--w-->q1\t')
		return 1
	elif(caracter=='e'):
		archivo.write('q2--e-->q4\t')
		return 4
	elif(caracter=='b'):
		archivo.write('q2--b-->q3\t')
		return 3
	else:
		archivo.write('q2--%s-->q0\t' % caracter)
		return 0

def estadoTres(caracter,archivo):
	if(caracter=='w'):
		archivo.write('q3--w-->q1\t')
		return 1
	elif(caracter=='e'):
		archivo.write('q3--e-->q4\t')
		return 4
	elif(caracter=='a'):
		archivo.write('q3--a-->q6\t')
		return 6
	else:
		archivo.write('q3--%s-->q0\t' % caracter)
		return 0

def estadoCuatro(caracter,archivo):
	if(caracter=='w'):
		archivo.write('q4--2-->q1\t')
		return 1
	elif(caracter=='e'):
		archivo.write('q4--e-->q4\t')
		return 4
	elif(caracter=='b'):
		archivo.write('q4--b-->q5\t')
		return 5
	else:
		archivo.write('q4--%s-->q0\t' % caracter)
		return 0

def estadoCinco(caracter,archivo):
	if(caracter=='w'):
		archivo.write('q5--w-->q1\t')
		return 1
	elif(caracter=='e'):
		archivo.write('q5--e-->q4\t')
		return 4
	elif(caracter=='a'):
		archivo.write('q5--a-->q6\t')
		return 6
	else:
		archivo.write('q5--%s-->q0\t' % caracter)
		return 0

def estadoSeis(caracter,archivo):
	if(caracter=='w'):
		archivo.write('q6--w-->q1\t')
		return 1
	elif(caracter=='e'):
		archivo.write('q6--e-->q4\t')
		return 4
	elif(caracter=='y'):
		archivo.write('q6--y-->q7\t')
		return 7
	else:
		archivo.write('q6--%s-->q0\t' % caracter)
		return 0

def estadoSiete(caracter,archivo):
	if(caracter=='w'):
		archivo.write('q7--w-->q1\t')
		return 1
	elif(caracter=='e'):
		archivo.write('q7--e-->q4\t')
		return 4
	else:
		archivo.write('q7--%s-->q0\t' % caracter)
		return 0
