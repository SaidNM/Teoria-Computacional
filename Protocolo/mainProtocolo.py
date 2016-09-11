import protocolo
import DiagramaProtocolo



try:
	opcion=input("1.-Iniciar Protocolo\n2.-Mostrar diagrama del protocolo\n Elija una opcion: ")
	opcion=int(opcion)
except:
	exit()

if(opcion==1):
	protocolo.IniciarProtocolo()
elif(opcion==2):
	DiagramaProtocolo.mostrarDiagrama()
else:
	print("Opcion invalida")



