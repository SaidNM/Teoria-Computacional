import random;

def IniciarArchivo():
	archivo=open("palindromo.txt","w")
	archivo.close
	historia=open("historiaPal.txt","w")
	historia.close

def Run(pal,longitud,par):
	try:
		archivo=open("palindromo.txt","a")
		historia=open("historiaPal.txt","a")
	except:
		exit()
	archivo.write("S")
	exito=generar_palindromo1(archivo,pal,longitud,par,historia)
	archivo.write("\n\n")
	historia.write("------\n\n")
	archivo.close
	historia.close
	return exito

def opcion_fin(par):
	if(par==True):
		op=1
	else:
		op=random.randint(2,3)
	return op

def opcion_inicio():
	op=random.randint(4,5)
	return op

def regla1(pal,historia):
	pal=pal.replace("S","")
	historia.write("\n1.-S-->e")
	return pal

def regla2(pal,historia):
	pal=pal.replace("S",'0')
	historia.write("\n2.-S-->0")
	return pal

def regla3(pal,historia):
	pal=pal.replace("S",'1')
	historia.write("\n3.-S-->1")
	return pal

def regla4(pal,historia):
	pal=pal.replace("S","0S0")
	historia.write("\n4.-S-->0S0")
	return pal
def regla5(pal,historia):
	pal=pal.replace("S","1S1")
	historia.write("\n5.-S-->1S1")
	return pal

def generar_palindromo1(archivo,pal,longitud,par,historia):
	
	if(longitud>1):
		
		opcion=opcion_inicio()
		if(opcion==4):
			pal=regla4(pal,historia)
			archivo.write("\n"+pal)
		if(opcion==5):
			pal=regla5(pal,historia)
			archivo.write("\n"+pal)

	if(longitud==1):
		opcion=opcion_fin(par)
		if(opcion==1):
			pal=regla1(pal,historia)
			archivo.write("\n"+pal)
		if(opcion==2):
			pal=regla2(pal,historia)
			archivo.write("\n"+pal)
		if(opcion==3):
			pal=regla3(pal,historia)
			archivo.write("\n"+pal)
	if (longitud==0):
		print(pal)
		return 1
	longitud=longitud-1
	pal=generar_palindromo1(archivo,pal,longitud,par,historia)


