import webay
import diagrama

def menu():
    try:
        opcion=input('\t\t-------------WEBAY------------\n1.-Modo manual\n2.-Leer texto\n3.-Diagrama\n4.-Salir\nElija una opcion: ')
        opcion=int(opcion)
    except:
        print('\nIntroduzca una opcion correcta\n')

    return opcion

def IniciarArchivo():
    archivo=open("Palabras.txt","w")
    archivo.close
    archivoH=open("Historia.txt","w")
    archivo.close

def AbrirArchivo():
    try:
        archivo=open("Palabras.txt","a")
    except:
        print("\nError al abrir el archivo")
        exit()
    return archivo

def AbrirHistoria():
    try:
        archivo=open("Historia.txt","a")
    except:
        print("\nError al abrir el archivo")
        exit()
    return archivo

def escribir(archivo,palabra_aux,no_palabra,no_fila):
    archivo.write("Palabra: "+palabra_aux+" Numero de palabra: "+str(no_palabra)+" Numero de fila: "+str(no_fila))
    archivo.write("\n")


def Evaluar(texto):
    archivo=AbrirArchivo()
    historia=AbrirHistoria()
    palabra_aux=''
    final=False
    estado=0
    no_palabra=1
    no_fila=1

    historia.write("\n\n\n\n")
    for caracter in texto:
        caracter=caracter.lower()
        estado=webay.automataWebay(caracter,estado,historia)
        if(estado==3 or estado==7):
            final=True
        if(caracter=='\n'):
            if(final):
                escribir(archivo,palabra_aux,no_palabra,no_fila)
                historia.write("\n")
                palabra_aux=''
                final=False
            else:
                palabra_aux=''
            no_palabra=1
            no_fila=no_fila+1
            continue
        if (caracter==' '):
            if(final):
                escribir(archivo,palabra_aux,no_palabra,no_fila)
                historia.write("\n")
                palabra_aux=''
                final=False
            else:
                palabra_aux=''
            no_palabra=no_palabra+1

            continue
        palabra_aux=palabra_aux+caracter
    if(final):
        #no_palabra=no_palabra+1
        escribir(archivo,palabra_aux,no_palabra,no_fila)
        historia.write("\n")

    archivo.close
    historia.close
def leer_Archivo():
    try:
        archivo=open("archivo.txt","r")
        texto=str(archivo.read())
    except:
        print("\nError al abrir el archivo")
        exit()
    return texto

def main():
    IniciarArchivo()
    while True:
        eleccion=menu()
        if(eleccion==1):
            texto=input("Introduzca un pequeño texto: ")

            Evaluar(texto)
            print("Evaluacion terminada, cheque el archivo de texto")
            while True:
                reop=input("Desea regresar al menu\n1.-Si\n2.-No\nEleccion: ")
                if(reop=='1'):
                    break
                elif(reop=='2'):
                    exit()
                else:
                    continue
        elif(eleccion==2):
            texto=leer_Archivo()

            Evaluar(texto)
            print("Evaluacion terminada, cheque el archivo de texto")
            while True:
                reop=input("Desea regresar al menu\n1.-Si\n2.-No\nEleccion: ")
                if(reop=='1'):
                    break
                elif(reop=='2'):
                    exit()
                else:
                    continue
        elif(eleccion==3):
            diagrama.mostrarDiagrama()
            while True:
                reop=input("Desea regresar al menu\n1.-Si\n2.-No\nEleccion: ")
                if(reop=='1'):
                    break
                elif(reop=='2'):
                    exit()
                else:
                    continue
        elif(eleccion==4):
            exit()
        else:
            continue
main()
