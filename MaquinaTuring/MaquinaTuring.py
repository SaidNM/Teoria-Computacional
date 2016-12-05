def maquinaTuring(cadena,archivo):
    estado=[0,"",0]
    cadena=list(cadena)
    index=0
    while True:
        for e in cadena:
            archivo.write(e)
        archivo.write("\n")
        for i in range(index):
            archivo.write(" ")
        archivo.write("|")
        archivo.write("\n")
        for i in range(index):
            archivo.write(" ")
        archivo.write("q"+str(estado[0])+"\n")
        try:
            if(index<0):
                raise Exception
            elif(estado[0]==0):
                estado[0]=estadoCero(cadena,index,estado)
                index=estado[2]
            elif(estado[0]==1):

                estado[0]=estadoUno(cadena,index,estado)
                index=estado[2]

            elif(estado[0]==2):
                estado[0]=estadoDos(cadena,index,estado)
                index=estado[2]
            elif(estado[0]==3):
                estado[0]=estadoTres(cadena,index,estado)
                index=estado[2]
            elif(estado[0]==4 or estado[0]==-1):
                break
            else:
                break
        except Exception as ex:
            if(estado[0]==3):
                estado[0]=4
            else:
                break
    return estado[0]
def estadoCero(cadena,index,estado):
    if(cadena[index]=='0'):
        cadena[index]='X'
        estado[1]="X"
        estado[2]=estado[2]+1
        return 1
    elif(cadena[index]=='Y'):
        cadena[index]='Y'
        estado[1]="Y"
        estado[2]=estado[2]+1
        return 3
    else:
        return -1

def estadoUno(cadena,index,estado):
    if(cadena[index]=='0'):
        cadena[index]='0'
        estado[1]="0"
        estado[2]=estado[2]+1
        return 1
    elif(cadena[index]=='1'):
        cadena[index]='Y'
        estado[1]="Y"
        estado[2]=estado[2]-1
        return 2
    elif(cadena[index]=='Y'):
        cadena[index]='Y'
        estado[2]=estado[2]+1
        return 1
    else:
        return -1

def estadoDos(cadena,index,estado):
    if(cadena[index]=='0'):
        cadena[index]='0'
        estado[1]="0"
        estado[2]=estado[2]-1
        return 2
    elif(cadena[index]=='X'):
        cadena[index]='X'
        estado[1]="X"
        estado[2]=estado[2]+1
        return 0
    elif(cadena[index]=='Y'):
        cadena[index]='Y'
        estado[2]=estado[2]-1
        return 2
    else:
        return -1

def estadoTres(cadena,index,estado):
    if(cadena[index]=='Y'):
        cadena[index]='Y'
        estado[1]="Y"
        estado[2]=estado[2]+1
        return 3
    elif(cadena[index]=='B'):
        cadena[index]='B'
        estado[1]="B"
        estado[2]=estado[2]+1
        return 4
    else:
        return -1
