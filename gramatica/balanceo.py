#Reglas
#B->(RB  |  e
#R-> )  | (RR
# si sustituyo B y el simbolo es ( usar (RB
#si sustituyo R el simolo es ) usar ) y si es ( usar (RR


def VerificarBalanceo(cadena,archivo):
    exp='B'
    i=-1;
    cadena_aux=''
    archivo.write(exp)
    while True:
        try:
            i=i+1
            archivo.write('\n')
            if(cadena[i]=='('):
                cadena_aux=cadena_aux+'('
                if(exp[0]=='B'):
                    exp=exp.replace('B','RB',1)
                    cadena_aux=cadena_aux.replace('B','RB',1)
                    archivo.write(cadena_aux+exp)
                    archivo.write('\t\t\tB->(RB')
                    continue
                if(exp[0]=='R'):
                    exp=exp.replace('R','RR',1)
                    cadena_aux=cadena_aux.replace('R','RR',1)
                    archivo.write(cadena_aux+exp)
                    archivo.write('\t\t\tR->(RR')
                    continue
            if(cadena[i]==')'):
                if(exp[0]=='R'):
                    exp=exp[1:]
                    cadena_aux=cadena_aux+')'
                    archivo.write(cadena_aux+exp)
                    archivo.write('\t\t\tR-> )')
                    continue
                elif(exp[0]=='B'):
                    exp=''
                    print('Cadena no balanceada')
                    break
                else:
                    exp=''
                    continue
        except:
            if(exp=='B'):
                archivo.write(cadena_aux)
                archivo.write('\t\t\tB-> e \n')
                print('Cadena balanceada')
            else:
                print('Cadena no balanceada')
            break
