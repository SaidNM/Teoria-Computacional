from tkinter import *


ventana1 = Tk()
ventana1.geometry("600x600+400+50")  #geometry(widthxheight)
ventana1.title("Automata Paridad")
ventana1.resizable(width=False,height=False)
AreaDibujo1=Canvas(ventana1,width=595,height=595)
AreaDibujo1.pack()

#Circulos transicion
AreaDibujo1.create_oval(100,100,500,500)
AreaDibujo1.create_oval(150,150,450,450)


#Circulos de estado
AreaDibujo1.create_oval(110,110,240,240,fill="white")
AreaDibujo1.create_oval(115,115,235,235,fill="light sky blue")
AreaDibujo1.create_oval(365,115,485,235,fill="light sky blue")
AreaDibujo1.create_oval(115,365,235,485,fill="light sky blue")
AreaDibujo1.create_oval(365,365,485,485,fill="light sky blue")

#Linea de inicio
AreaDibujo1.create_line(50,175,110,175)

#Circulos de sentido
AreaDibujo1.create_oval(105,170,115,180, fill="black")
AreaDibujo1.create_oval(385,118,395,128,fill="black")
AreaDibujo1.create_oval(470,385,480,395,fill="black")
AreaDibujo1.create_oval(203,470,213,480,fill="black")
AreaDibujo1.create_oval(115,210,125,220,fill="black")

AreaDibujo1.create_oval(237,156,247,166,fill="black")
AreaDibujo1.create_oval(160,360,170,370,fill="black")
AreaDibujo1.create_oval(357,430,367,440,fill="black")
AreaDibujo1.create_oval(430,232,440,242,fill="black")

#etiquetas
inicio=Label(ventana1,text="Inicio",font="Verdana 12 roman").place(x=40,y=140)
qo=Label(ventana1,text="q0",font="Verdana 12 italic",background="light sky blue").place(x=165,y=165)
q1=Label(ventana1,text="q1",font="Verdana 12 italic",background="light sky blue").place(x=415,y=165)
q2=Label(ventana1,text="q2",font="Verdana 12 italic",background="light sky blue").place(x=165,y=415)
q3=Label(ventana1,text="q3",font="Verdana 12 italic",background="light sky blue").place(x=415,y=415)

#etiquetas transicion
qoq1=Label(ventana1,text="1",font="Verdana 12 roman").place(x=210,y=85)
q1q0=Label(ventana1,text="1",font="Verdana 12 roman").place(x=345,y=130)

q2q3=Label(ventana1,text="1",font="Verdana 12 roman").place(x=250,y=410)
q3q2=Label(ventana1,text="1",font="Verdana 12 roman").place(x=350,y=454)

qoq2=Label(ventana1,text="0",font="Verdana 12 roman").place(x=170,y=250)
q2qo=Label(ventana1,text="0",font="Verdana 12 roman").place(x=90,y=365)

q1q3=Label(ventana1,text="0",font="Verdana 12 roman").place(x=500,y=210)
q3q1=Label(ventana1,text="0",font="Verdana 12 roman").place(x=410,y=325)

ventana1.mainloop()