import webay

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

def Manual(estado,no_palabra,no_fila):
    palabra_aux=''
    palabra=input("Introduzca un pequeño texto: ")
    for caracter in palabra:
        caracter.lower()
        if(caracter==' '):
            no_palabra=no_palabra+1
            if(estado==3 or estado==7):
                print(palabra+' numero de palabra= '+str(no_palabra))
                palabra_aux=''
            else:
                palabra_aux=''
        if(caracter=='\n'):
            no_fila=no_fila+1
        palabra_aux=palabra_aux+caracter
        estado=webay.automataWebay(caracter,estado)

def main():
    IniciarArchivo()
    palabra_aux=''
    estado=0
    no_fila=0
    no_palabra=0

    try:
        archivo=open("Palabras.txt","a")
    except:
        print("Error al abrirel archivo")
        exit()

    while True:
        eleccion=menu()
        if(eleccion==1):
                Manual(estado,no_palabra,no_fila)
        elif(eleccion==2):
            pass
        elif(eleccion==3):
            pass
        elif(eleccion==4):
            exit()
        else:
            continue
    archivo.close
main()
