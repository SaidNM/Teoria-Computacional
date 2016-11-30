import random
import balanceo

def IniciarArchivo():
    archivo=open("Gramatica.txt","w")
    archivo.close
def Menu():
    print("------Menu-----")
    print("1.-Modo Manual")
    print("2.-Modo Automatico")
    print("3.-Salir")
def Eleccion():
    op=input("Elige una opcion: ")
    try:
        op=int(op)
    except:
        print("Introduzca una opcion valida")
    return op
def longitud():
    lon=random.randint(1,100)
    return lon

def generarCadena():
    lon=longitud()
    cadena=''
    for c in range(1,lon+1):
        o=random.randint(1,2)
        if(o==1):
            cadena=cadena+'('
        else:
            cadena=cadena+')'
    return cadena

def Manual():
    try:
        archivo=open("Gramatica.txt","a")
    except:
        print("Error al abrir el archivo")
        exit()

    cadena=input("Introduce una cadena de parentesis: ")
    balanceo.VerificarBalanceo(cadena,archivo)

def Automatico():
    try:
        archivo=open("Gramatica.txt","a")
    except:
        print("Error al abrir el archivo")
        exit()
    cadena=generarCadena()
    print(cadena)
    balanceo.VerificarBalanceo(cadena,archivo)

def VerificarDeNuevo():
    opcion=input("Desea ingresar una nueva cadena [s/n]: ")
    return opcion
def main():
    IniciarArchivo()
    Menu()
    op=Eleccion()
    while True:
        if(op==1):
            Manual()
            while True:
                rop=VerificarDeNuevo()
                if(rop=='s'):
                    break
                elif(rop=='n'):
                    exit()
                else:
                    continue
        elif(op==2):
            Automatico()
            while True:
                rop=random.randint(1,2)
                if(rop==1):
                    break
                elif(rop==2):
                    exit()
                else:
                    continue
        elif(op==3):
            exit()
        else:
            continue

main()
