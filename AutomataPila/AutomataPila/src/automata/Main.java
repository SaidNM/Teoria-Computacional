
package automata;
import java.util.Scanner;
import javax.swing.JOptionPane;


public class Main {
    
    

    public static void main(String[] args) {
       String cadena;
       String bin_aux;
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
                bin_aux=cadena; 
                for(int i=0;i<cadena.length();i++){
                    cadena_aux=cadena.charAt(i);
                    automata.IniciarArchivo("("+estado+", "+bin_aux+", "+automata.getCadena()+")");
                    System.out.println("("+estado+", "+bin_aux+", "+automata.getCadena()+")");
                    estado=automata.evaluar(cadena_aux,estado);
                    
                    bin_aux=bin_aux.substring(1);
                    //System.out.println(estado);
                    if(estado.equals("")){
                        break;
                    }
 
                }
                if(automata.fin() && estado.equals("q1")){
                automata.IniciarArchivo("("+estado+", e ,"+automata.getCadena()+")");
                System.out.println("("+estado+", e ,"+automata.getCadena()+")");
                estado="f";
                automata.IniciarArchivo("("+estado+", e ,"+automata.getCadena()+")\n\n");
                System.out.println("("+estado+", e ,"+automata.getCadena()+")");
                System.out.println("Cadena aceptada");
                }
                else{
                    System.out.println("Cadena no aceptada");
                }
                estado="q0";
                automata.vaciarPila();
                automata.setCadena("Z0");
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
           while(true){
                cadena=automata.generarCadena();
                bin_aux=cadena;
                System.out.println(bin_aux);
                for(int i=0;i<cadena.length();i++){
                    cadena_aux=cadena.charAt(i);
                    automata.IniciarArchivo("("+estado+", "+bin_aux+", "+automata.getCadena()+")");
                    System.out.println("("+estado+", "+bin_aux+", "+automata.getCadena()+")");
                    estado=automata.evaluar(cadena_aux,estado);
                    
                    bin_aux=bin_aux.substring(1);
                    //System.out.println(estado);
                    if(estado.equals("")){
                        break;
                    }
 
                }
                if(automata.fin() && estado.equals("q1")){
                automata.IniciarArchivo("("+estado+", e ,"+automata.getCadena()+")");
                System.out.println("("+estado+", e ,"+automata.getCadena()+")");
                estado="f";
                automata.IniciarArchivo("("+estado+", e ,"+automata.getCadena()+")\n\n");
                System.out.println("("+estado+", e ,"+automata.getCadena()+")");
                System.out.println("Cadena aceptada");
                }
                else{
                    System.out.println("Cadena no aceptada");
                }
                estado="q0";
                automata.vaciarPila();
                automata.setCadena("Z0");
                while(true){
                System.out.println("Desea evaluar otra cadena\n1.-Si\n2.-No\nElija una opcion: ");
                int reop=automata.Generarbit();
                    System.out.println(reop+1);
                if(reop==0){
                    break;
                }
                else if(reop==1){
                    System.exit(0);
                    }
                }        
            }
       }
       else if(opcion.equals("3")){
           System.exit(0);
       }
       else{
           System.out.println("Opcion Invalida");
       }
       
       
       
    }
       
      
}



