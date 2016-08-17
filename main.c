#include "cadenas.h"

int main(void){
	int n=0;
	int n2=0;
	char *cadena =NULL;
	
	while(n2!=2){
	n=random_potencia();
	printf("****%d",n);
	
 	cadena = (char*)malloc(2*sizeof(char));
 	iniciar_cadena(&cadena);
 	obtener_cadenas(cadena,n);
 	

 	printf("\n¿Desea hacer otra cadena? ");
 	n2=random_decision();
	printf("\n---- %d",n2);
	}
	
	getch();
	return 0;
}