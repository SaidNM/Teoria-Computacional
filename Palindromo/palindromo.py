import random;

def IniciarArchivo():
	archivo=open("palindromo.txt","w")
	archivo.close

def Run(pal,longitud,par):
	try:
		archivo=open("palindromo.txt","a")
	except:
		exit()
	exito=generar_palindromo1(archivo,pal,longitud,par)
	archivo.close
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

def regla1(pal):
	pal=pal.replace("S","")
	return pal

def regla2(pal):
	pal=pal.replace("S",'0')
	return pal

def regla3(pal):
	pal=pal.replace("S",'1')
	return pal

def regla4(pal):
	pal="0"+pal+"0"
	return pal
def regla5(pal):
	pal="1"+pal+"1"
	return pal

def generar_palindromo1(archivo,pal,longitud,par):
	
	if(longitud>1):
		
		opcion=opcion_inicio()
		if(opcion==4):
			pal=regla4(pal)
			archivo.write("\n"+pal)
		if(opcion==5):
			pal=regla5(pal)
			archivo.write("\n"+pal)

	if(longitud==1):
		opcion=opcion_fin(par)
		if(opcion==1):
			pal=regla1(pal)
			archivo.write("\n"+pal)
		if(opcion==2):
			pal=regla2(pal)
			archivo.write("\n"+pal)
		if(opcion==3):
			pal=regla3(pal)
			archivo.write("\n"+pal)
	if (longitud==0):
		return 1
	longitud=longitud-1
	pal=generar_palindromo1(archivo,pal,longitud,par)


