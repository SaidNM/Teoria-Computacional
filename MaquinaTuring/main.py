import random

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
def main():
    iniciarArchivo()

def manual():
    cadena=input("Ingresa una cadena binaria: ")
    return cadena

    while True:
        opcion=menu()
        if(opcion=='1'):
            cadena=manual()
        elif(opcion=='2'):
            cadena=generar_cadena()
        elif(opcion=='3'):
            exit()
        else:
            print("Selecciona una opcion correcta")
            continue
