
package automata;

import Stack.Pila;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;


public class AutomataPila {
    private Pila automata;
    private int tamanio;
    private String cadena;
    
    public AutomataPila() {
        automata=new Pila();
       cadena="Z0";
    }
    
    public String evaluar(char caracter,String estado){
        //System.out.println(estado);
        if(estado.equals("q0")){
            if(caracter=='1'){
                if(!automata.is_empty()){
                    estado="q1";
                    automata.pop();
                    cadena=cadena.substring(1);
                    tamanio--;
                }
                else{
                    return "";
                }
            }
            else if(caracter=='0'){
                estado="q0";
                automata.push("X");
                cadena="X"+cadena;
                //System.out.println(automata.imprimirPila());
                tamanio++;
            }
            else{
                return "";
            }
        }
        else if(estado.equals("q1")){
            if(!automata.is_empty()){
                if(caracter=='1'){
                    estado="q1";
                    automata.pop();
                    cadena=cadena.substring(1);
                    tamanio--;
                }
                else if(caracter=='0'){
                    return "";
                }
                else{
                    return "";
                }
            
               }
            else{
                return "";
            }
        }
        return estado;
        }
   
    
    public boolean fin(){
        if(automata.is_empty()){
            return true;
        }
        else{
            return false;
        }
    }
    public void vaciarPila(){
  
        for(int i=0;i<tamanio;i++){
            automata.pop();
        }
        
        }
    
    
   public void IniciarArchivo(String texto){
    File f = new File ("archivo.txt");

        if ( !( f.exists ( ) ) ){
        try {
            FileWriter w = new FileWriter ( f, true );
            f.createNewFile ( );
            w.write (texto);
            } 
        catch ( Exception e ) {
        e.printStackTrace ( );
        }
        } 
        else {
        try{
        FileWriter w = new FileWriter ( f, true );
        w.write (texto);
        w.close ( );
        } 
        
        catch (Exception e ) {
        e.printStackTrace ( );
        }
}
   }
   

    public String getCadena() {
        return cadena;
    }

    public void setCadena(String cadena) {
        this.cadena = cadena;
    }
    
    public int GenerarNumero(){
        int numero;
        numero=(int)(Math.random()*100)+1;
        return numero;
        }
     public int Generarbit(){
        int numero;
        numero=(int)(Math.random()*2);
        return numero;
        }
   
     public String generarCadena(){
     String cadena="";
     int numero=GenerarNumero();
         for (int i = 0; i < numero; i++) {
             cadena=cadena+Generarbit();
         }
     
     return cadena;
     }
}


