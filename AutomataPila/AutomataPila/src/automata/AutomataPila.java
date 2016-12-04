
package automata;

import Stack.Pila;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;


public class AutomataPila {
    private Pila automata;
    private int tamanio;
    
    public AutomataPila() {
        automata=new Pila();
       
    }
    
    public String evaluar(char caracter,String estado){
        //System.out.println(estado);
        if(estado.equals("q0")){
            if(caracter=='1'){
                if(!automata.is_empty()){
                    estado="q1";
                    automata.pop();
                    tamanio--;
                }
                else{
                    return "";
                }
            }
            else if(caracter=='0'){
                estado="q0";
                automata.push("X");
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
    File archivo;
    FileWriter escribirArchivo;
   
    try{
        archivo=new File("Historia.txt");
        escribirArchivo= new FileWriter(archivo);
        BufferedWriter bw = new BufferedWriter(escribirArchivo);
        PrintWriter salida = new PrintWriter(bw);
        
        salida.write(texto);
        salida.close();
        bw.close();
        }
    
    catch(Exception e){
        System.out.println("Error al abrir el archivo");
    }
   }

}
