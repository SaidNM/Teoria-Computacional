import automataPar
import Diagrama2
import funcionesPar

archivo=open("paridad.txt","w")
archivo.close



#menu
opcion=funcionesPar.menu()


if(opcion==1):
	while True:
		archivo=open("paridad.txt","a")
		cadena=input("Introduce una cadena binaria: ")
		print(cadena)
		print("numero de ceros: " + str(cadena.count("0")))
		print("numero de unos: " + str(cadena.count("1")))
		resultado=automataPar.automata(cadena,archivo)
		if(resultado==1):
			print("Es una cadena con paridad")
		elif(resultado==0):
			print("No es una cadena con paridad")
		else:
			print("no es una cadena binaria")
		archivo.close
		while True:
			nC=funcionesPar.nueva_cadena()
			if(nC==1):
				break
			elif(nC==2):
				exit()
			else:
				continue

elif(opcion==2):
	while True:
		archivo=open("paridad.txt","a")
		cadena=funcionesPar.generarCadena()
		print(cadena)
		print("numero de ceros: " + str(cadena.count("0")))
		print("numero de unos: " + str(cadena.count("1")))
		resultado=automataPar.automata(cadena,archivo)
		if(resultado==1):
			print("Es una cadena con paridad")
		elif(resultado==0):
			print("No es una cadena con paridad")
		archivo.close
		while True:
			nC=funcionesPar.nueva_cadena()
			if(nC==1):
				break
			elif(nC==2):
				exit()
			else:
				continue

elif(opcion==3):
	Diagrama2.mostarDiagrama()
	
else:
	print("opcion invalida")