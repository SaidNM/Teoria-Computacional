def estado23(estado,cadena):
  estado[2]=2
  cadena="X"
  return 1


cadena='0011'
cadena=list(cadena)
estado=[0,"",0]
estado[0]=estado23(estado,cadena[2])
print(estado)
print(cadena)
