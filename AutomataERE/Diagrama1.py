from tkinter import *

ventana =  Tk()
ventana.geometry("900x500")  #geometry(widthxheight)
ventana.title("Automata ERE")
AreaDibujo=Canvas(ventana,width=890,height=490)
AreaDibujo.pack()

#Creacion de arcos para transicion
AreaDibujo.create_arc(315,115,385,185,start=-25,extent=250)
AreaDibujo.create_arc(550,115,750,185,start=8,extent=180,style=ARC)
AreaDibujo.create_arc(350,200,750,290,start=180,extent=168,style=ARC)

#Creacion de Circulos de estado
AreaDibujo.create_oval(695,145,805,255,fill="white")
AreaDibujo.create_oval(100,150,200,250,fill="red")
AreaDibujo.create_oval(300,150,400,250,fill="red")
AreaDibujo.create_oval(500,150,600,250,fill="red")
AreaDibujo.create_oval(700,150,800,250,fill="red")
#Creacion de circulo de referencia


AreaDibujo.create_oval(95,195,105,205,fill="black")
AreaDibujo.create_oval(295,195,305,205,fill="black")
AreaDibujo.create_oval(495,195,505,205,fill="black")
AreaDibujo.create_oval(690,195,700,205,fill="black")
AreaDibujo.create_oval(313,157,323,167,fill="black")
AreaDibujo.create_oval(545,145,555,155,fill="black")
AreaDibujo.create_oval(345,245,355,255,fill="black")


#Creacion de lineas para transicion

AreaDibujo.create_line(50,200,100,200)
AreaDibujo.create_line(200,200,300,200)
AreaDibujo.create_line(400,200,500,200)
AreaDibujo.create_line(600,200,700,200)


#Creacion de etiquetas

#estados
qo=Label(ventana,text="q0",background="red",font="Verdana 10 italic").place(x=143,y=210)
q1=Label(ventana,text="q1",background="red",font="Verdana 10 italic").place(x=345,y=210)
q2=Label(ventana,text="q2",background="red",font="Verdana 10 italic").place(x=545,y=210)
q3=Label(ventana,text="q3",background="red",font="Verdana 10 italic").place(x=745,y=210)

qoe=Label(ventana,text="e",background="red",font="Verdana 10 roman").place(x=345,y=180)
qo=Label(ventana,text="er",background="red",font="Verdana 10 roman").place(x=545,y=180)
qo=Label(ventana,text="ere",background="red",font="Verdana 10 roman").place(x=740,y=180)

#transiciones
letra_e=Label(ventana,text="e",font="Verdana 10 roman").place(x=250,y=175)
letra_r=Label(ventana,text="r",font="Verdana 10 roman").place(x=450,y=175)
letra_eFinal=Label(ventana,text="e",font="Verdana 10 roman").place(x=650,y=175)
letra_eQ0=Label(ventana,text="e",font="Verdana 10 roman").place(x=347,y=90)
letra_rQ3Q2=Label(ventana,text="r",font="Verdana 10 roman").place(x=650,y=90)
letra_eQ3Q1=Label(ventana,text="r",font="Verdana 10 roman").place(x=550,y=294)

ventana.mainloop()

