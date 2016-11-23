
package automata;

import sources.Pila;


public class AutomataPila {
    public static void main(String[] args) {
         Pila automata=new Pila();
         
         System.out.println(automata.is_empty());
         automata.push(0);
         automata.push(15);
         automata.push(3);
         automata.pop();
         automata.pop();

    }
    
}
