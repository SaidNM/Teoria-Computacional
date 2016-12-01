
package automata;
import java.util.Scanner;
import javax.swing.JOptionPane;


public class Main {
    
    

    public static void main(String[] args) {
       String cadena;
       char cadena_aux;
       AutomataPila automata=new AutomataPila();
       int index=0;
       String opcion;
       //Menu
       
       
       System.out.println("Menu\n1.-Modo manual\n2.-Modo Automatico\n3.-Salir\nElija una opcion: ");
       Scanner entrada = new Scanner(System.in);
       opcion=entrada.nextLine();
       
       if(opcion.equals("1")){
            cadena=JOptionPane.showInputDialog(null,"Introduzca una cadena binaria");
            while(true){
                try{
                    cadena_aux=cadena.charAt(index);
                    automata.evaluar(cadena_aux);
                    index++;
                }
                catch(Exception e){
                    if(automata.fin()){
                    System.out.println("Cadena aceptada");
                    }
                    else{
                        System.out.println("Cadena no aceptada");
                     }
                    break;
                }
       
            }
       }
       else if(opcion.equals("2")){
           System.out.println("Aun no esta disponible");
       }
       else if(opcion.equals("3")){
           System.exit(0);
       }
       else{
           System.out.println("Opcion Invalida2"
                   + "");
       }
       
       
       
    }
       
      
}



