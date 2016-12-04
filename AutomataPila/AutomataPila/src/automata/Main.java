
package automata;
import java.util.Scanner;
import javax.swing.JOptionPane;


public class Main {
    
    

    public static void main(String[] args) {
       String cadena;
       String estado="q0";
       char cadena_aux;
       AutomataPila automata=new AutomataPila();
       String opcion;
       String opcion2;
       //Menu
       
       
       System.out.println("Menu\n1.-Modo manual\n2.-Modo Automatico\n3.-Salir\nElija una opcion: ");
       Scanner entrada = new Scanner(System.in);
       opcion=entrada.nextLine();
       
       if(opcion.equals("1")){
           while(true){
                cadena=JOptionPane.showInputDialog(null,"Introduzca una cadena binaria");
                 
                
                for(int i=0;i<cadena.length();i++){
                    
                    cadena_aux=cadena.charAt(i);
                    estado=automata.evaluar(cadena_aux,estado);
                    System.out.println(estado);
                    if(estado.equals("")){
                        break;
                    }
 
                }
                if(automata.fin() && estado.equals("q1")){
                estado="f";
                System.out.println("Cadena aceptada");
                }
                else{
                    System.out.println("Cadena no aceptada");
                }
                estado="q0";
                automata.vaciarPila();
                while(true){
                System.out.println("Desea evaluar otra cadena\n1.-Si\n2.-No\nElija una opcion: ");
                Scanner rentrada = new Scanner(System.in);
                opcion2=rentrada.nextLine(); 
                if(opcion2.equals("1")){
                    break;
                }
                else if(opcion2.equals("2")){
                    System.exit(0);
                    }
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
           System.out.println("Opcion Invalida");
       }
       
       
       
    }
       
      
}



