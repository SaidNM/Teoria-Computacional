#include "cadenas.h"

int random_potencia(void){
	int r=0;
	srand(time(NULL));
	r=rand() % 10;
	return r;
}

int random_decision(void){
	int r=0;
	srand(time(NULL));
	r= 1 + (rand() % 2);
	return r;
}

void iniciar_cadena(char ** cadena){
	int i;
    for(i = 0; i < 2; i++){
        *(*cadena + i) = i + '0';
    }
    return ;
}

int obtener_cadenas(char *cadena,int n){
	int *cadena_auxiliar = NULL;
	int i=0;
    int j=0;
    int salir = 0;
    FILE *archivo = NULL;

    archivo = fopen("cadenabinaria.txt", "w");
    if (archivo == NULL) {
		printf("%s\n", "Error");
		exit(0);
	}

	fputs("Σ*= { e ",archivo);
	fclose(archivo);
}