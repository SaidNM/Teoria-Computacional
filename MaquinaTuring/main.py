import random
import MaquinaTuring

def longitud():
  num=random.randint(1,1000)
  return num

def num_bin():
  bin=random.randint(0,1)
  return bin

def generar_cadena():
  lon=longitud()
  cadena=''
  for i in range(1,lon+1):
    bin=str(num_bin())
    cadena=cadena+bin
  return cadena

def menu():
    print("----------------------MAQUINA DE TURING----------------------")
    print("1.-Modo Manual")
    print("2.-Modo Automatico")
    print("3.-Salir")
    op=input("Elija una opcion: ")
    return op

def iniciarArchivo():
    archivo=open("historia.txt","w")
    archivo.close
    validas=open("Validas.txt","w")
    validas.close


def manual():
    cadena=input("Ingresa una cadena binaria: ")
    return cadena

def main():
    iniciarArchivo()
    estado=[0,'',0]
    try:
        archivo=open("historia.txt","a")
        validas=open("Validas.txt","a")
    except:
        print("Error al abrir el archivo")
    while True:
        opcion=menu()
        if(opcion=='1'):
            while True:
                cadena=manual()
                estado=MaquinaTuring.maquinaTuring(cadena,archivo)
                if(estado==4):
                    validas.write(cadena)
                    validas.write("\n")
                    print("Cadena Valida")
                else:
                    print("Cadena invalida")
                while True:
                    print("Desea evaluar otra cadena [s/n]: ")
                    reop=input("")
                    if(reop=='s'):
                        break
                    if(reop=='n'):
                        exit()
        elif(opcion=='2'):
            while True:
                cadena=generar_cadena()
                estado=MaquinaTuring.maquinaTuring(cadena,archivo)
                if(estado==4):
                    validas.write(cadena)
                    validas.write("\n")
                    print("Cadena Valida")
                else:
                    print("Cadena invalida")
                archivo.write("\n\n")
                while True:
                    print("Desea regresar al menu [s/n]: ")
                    reop=num_bin()
                    if(reop==0):
                        print("s")
                        break
                    if(reop==1):
                        print('n')
                        exit()
        elif(opcion=='3'):
            archivo.close
            validas.close
            exit()
        else:
            print("Selecciona una opcion correcta")
    archivo.close
    validas.close

main()
