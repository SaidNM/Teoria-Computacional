
package automata;

import Stack.Pila;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;


public class AutomataPila {
    private Pila automata;
    private char estado;
    
    
    public AutomataPila() {
        automata=new Pila();
       
    }
    
    public void evaluar(char caracter){
        if(caracter=='0'){
            estado='q';
            automata.push("X");

        }
        else if(caracter=='1'){
            if(automata.is_empty()){
                System.out.println("Cadena no aceptada");
                System.exit(0);
            }
            else{
                estado='p';
                String dato=automata.pop();
            }
        }
        else{
            System.out.println("Cadena invalida");
            System.exit(0);
        }
    }
    
    public boolean fin(){
        if(automata.is_empty()){
            return true;
        }
        else{
            return false;
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
