
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
    System.out.println(tope.getDato());
}

public int pop(){
    Nodo auxiliar;
    int dato=0;
    if(!is_empty()){
        auxiliar=tope;
        tope=tope.getSiguiente();
        dato=auxiliar.getDato();
        auxiliar=null;
        
    }
    else{
        System.out.println("Pila vacia");
    }
    System.out.println(tope.getDato());
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
