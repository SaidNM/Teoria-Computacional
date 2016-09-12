import random
import automataPar
import time


def IniciarArchivo():
	archivo=open("cadenasGeneradas.txt","w")
	archivo.close
def IniciarArchivoValidas():
	archivo1=open("cadenasValidas.txt","w")
	archivo1.close

def num_aleatorio():
	bit = random.randrange(0,2)
	return bit

def generarCadena():
	cardinalidad=32
	tamanio=0
	cadena=""
	while (tamanio<cardinalidad):
		num=num_aleatorio()
		num=str(num)
		cadena=cadena+num
		tamanio=tamanio + 1
	return cadena



def IniciarProtocolo():
	
	IniciarArchivoValidas()
	encendido=True
	if(encendido==True):
		print("encendido")
	while encendido:
		IniciarArchivo()
		print("---Iniciando Protocolo---")
		archivo=open("cadenasGeneradas.txt","a")
		for x in range(1,51):
			cadena=generarCadena()
			archivo.write(cadena)
			archivo.write(" ")
		archivo.close()
		print("---Enviando datos generados---")
		try:
			archivo=open("cadenasGeneradas.txt","r")
		except:
			print("Error al enviar el archivo")
			exit()
		texto=archivo.read()
		archivo.close()
		print("---Esperando---")
		time.sleep(1)
		print("---Validando archivo---")
		archivo1=open("cadenasValidas.txt","a")
		archivo1.write("\n\n")
		palabra=""
		for bit in texto:
			if(bit != " "):
				palabra=palabra+bit
			if(bit == " "):
				escribir=automataPar.automata(palabra)
				if(escribir==1):
					archivo1.write(palabra)
					archivo1.write("\n")
					palabra=""
				elif(escribir==0):
					palabra=""
				else:
					continue
		archivo1.close
		print("Validando estado(encendido/apagado)")
		encendido=random.choice([True,False])
		if(encendido==True):
			print("encendido")
		else:
			print("Apagado")













