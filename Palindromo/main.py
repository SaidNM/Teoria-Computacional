import palindromo
import random

def longitud():
	x=random.randint(0,1000);
	return x

palindromo.IniciarArchivo()
def menu():
	print("-----Menu-----")
	print("1.-Modo Manual")
	print("2.-Modo Automatico")
	print("3.-Salir")

while True:
	menu()
	opcion=input("Seleccione una opcion: ")
	if(opcion=="1"):
		tamanio=input("Ingrese un tamanio de cadena: ")
		print(tamanio)
		tamanio=int(tamanio)
		if(tamanio%2==0):
			g=palindromo.Run("S",(tamanio/2)+1,True)
	
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
	elif(opcion=="2"):
		tamanio=longitud()
		print(tamanio)
		if(tamanio%2==0):
			g=palindromo.Run("S",(tamanio/2)+1,True)
		else:
			tamanio=int(tamanio/2)+1
			g=palindromo.Run("S",tamanio,False)


		while True:
			seln=random.randint(1,2)
			try:
				print("Desea regresar al menu\n1.-Si\n2.-No\n- %s" %seln)
				
			except:
				exit()

			if(seln==1):
				break
			elif(seln==2):
				exit()
			else:
				continue

	elif(opcion=="3"):
		exit()

	else:
		print("Seleccione una opcion correcta")
