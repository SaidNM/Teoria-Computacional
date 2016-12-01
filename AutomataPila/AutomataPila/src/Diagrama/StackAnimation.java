
package Diagrama;

import java.awt.Color;
import javax.swing.JFrame;


public class StackAnimation {
    public static void main(String[] args) {
        JFrame ventana = new JFrame("Automata de Pila");
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        Rectangle r= new Rectangle();
        r.setBackground(Color.WHITE);
        ventana.add(r);
        ventana.setSize(500,500);
        ventana.setResizable(false);
        ventana.setVisible(true);
    }
}
