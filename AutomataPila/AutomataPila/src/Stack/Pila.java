
package Stack;

public class Pila {
    private Nodo tope;

    public Pila() {
        this.tope = null;
    }
    
public void push(String dato){
    Nodo nuevo = new Nodo();
    nuevo.setDato(dato);
    
    if(is_empty()){
        tope=nuevo;
    }
    else{
        nuevo.setSiguiente(tope);
        tope=nuevo;
    }
}
 
public String pop(){
    Nodo auxiliar;
    String dato="";
    if(!is_empty()){
        auxiliar=tope;
        tope=tope.getSiguiente();
        dato=auxiliar.getDato();
        auxiliar=null;
        
    }
    else{
        System.out.println("Pila vacia");
    }
    return dato;
}  

public boolean is_empty(){
    if(tope==null){
        return true;
    }
    else{
        return false;
    }
}


}
