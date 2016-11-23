
package sources;

public class Pila {
    private Nodo tope;

    public Pila() {
        this.tope = null;
    }
    
public void push(int dato){
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

public void pop(){
    Nodo auxiliar;
    if(!is_empty()){
        auxiliar=tope;
        tope=tope.getSiguiente();
        auxiliar=null;
        
    }
    else{
        System.out.println("Pila vacia");
    }
    
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
