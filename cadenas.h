#ifndef __CADENAS__
#define __CADENAS__

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int random_potencia(void);
int random_decision(void);

void iniciar_cadena(char **);
int obtener_cadenas(char *, int);
int escribir_cadena(FILE **, int *,char*, int);


#endif