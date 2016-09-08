from tkinter import *

ventana =  Tk()
ventana.geometry("900x500")  #geometry(widthxheight)
ventana.title("Automata ERE")
AreaDibujo=Canvas(ventana,width=890,height=490)
AreaDibujo.pack()

#Creacion de arcos para transicion
AreaDibujo.create_arc(315,115,385,185,start=-25,extent=250)

#Creacion de Circulos de estado
AreaDibujo.create_oval(100,150,200,250,fill="red")
AreaDibujo.create_oval(300,150,400,250,fill="red")
AreaDibujo.create_oval(500,150,600,250,fill="red")
AreaDibujo.create_oval(700,150,800,250,fill="red")
#Creacion de circulo de referencia

AreaDibujo.create_oval(695,145,805,255)
AreaDibujo.create_oval(95,195,105,205,fill="black")
AreaDibujo.create_oval(295,195,305,205,fill="black")
AreaDibujo.create_oval(495,195,505,205,fill="black")
AreaDibujo.create_oval(690,195,700,205,fill="black")
AreaDibujo.create_oval(313,157,323,167,fill="black")


#Creacion de lineas para transicion

AreaDibujo.create_line(50,200,100,200)
AreaDibujo.create_line(200,200,300,200)
AreaDibujo.create_line(400,200,500,200)
AreaDibujo.create_line(600,200,700,200)

#crear poligono
AreaDibujo.create_polygon(100,100,200,150,300,200)





#Creacion de etiquetas
qo=Label(ventana,text="q0").place(x=145,y=185)
q1=Label(ventana,text="q1").place(x=345,y=185)
q2=Label(ventana,text="q2").place(x=545,y=185)
q3=Label(ventana,text="q3").place(x=745,y=185)
letra_e=Label(ventana,text="e").place(x=250,y=175)
letra_r=Label(ventana,text="r").place(x=450,y=175)
letra_eFinal=Label(ventana,text="e").place(x=650,y=175)
letra_eQ0=Label(ventana,text="e").place(x=347,y=90)

ventana.mainloop()

