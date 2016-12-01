
package Diagrama;

import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JPanel;


public class Rectangle extends JPanel{
    
    public void paintRectangle(Graphics r){
        super.paintComponent(r);
        this.setBackground(Color.WHITE);
        
        r.setColor(Color.LIGHT_GRAY);
        r.fillRect(225,200,100,100);
        
    }
    
}
