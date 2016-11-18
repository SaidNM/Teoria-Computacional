import palindromo
import random

def longitud():
	x=random.randint(0,1000);
	return x

palindromo.IniciarArchivo()


while True:
	try:
		sel=input("\t\tMenu\n1.-Generar Palindromo\n2.-Salir\nElija una opcion: ")
		sel=int(sel)
	except:
		exit()
	if(sel==1):	
		tamanio=longitud()
		print(tamanio)
		if(tamanio%2==0):
			g=palindromo.generar_palindromo1("S",(tamanio/2)+1,True)
		else:
			tamanio=int(tamanio/2)+1
			g=palindromo.Run("S",tamanio,False)

		while True:
			try:
				seln=input("Desea regresar al menu\n1.-Si\n2.-No\n- ")
				seln=int(seln)
			except:
				exit()

			if(seln==1):
				break
			elif(seln==2):
				exit()
			else:
				continue

	if(sel==2):
		exit()
	
	else:
		continue





