from tkinter import *

def mostrarDiagrama():
    ventana=Tk()
    ventana.geometry("900x650")
    ventana.resizable(width=False,height=False)
    ventana.title("Automata WEBAY")
    AreaDibujo=Canvas(ventana, width=900,height=650)
    AreaDibujo.pack()

    #Creacion de circulos de estados
    #inicio
    AreaDibujo.create_oval(50,275,150,375,fill="sky blue")

    #web
    AreaDibujo.create_oval(200,150,300,250,fill="sky blue")
    AreaDibujo.create_oval(400,150,500,250,fill="sky blue")
    AreaDibujo.create_oval(590,140,710,260,fill="white")
    AreaDibujo.create_oval(600,150,700,250,fill="sky blue")

    #ebay
    AreaDibujo.create_oval(200,400,300,500,fill="sky blue")
    AreaDibujo.create_oval(400,400,500,500,fill="sky blue")
    AreaDibujo.create_oval(600,400,700,500,fill="sky blue")
    AreaDibujo.create_oval(770,390,890,510,fill="white")
    AreaDibujo.create_oval(780,400,880,500,fill="sky blue")

    #creacion de lineas de transicion
    #inicio
    AreaDibujo.create_line(20,325,50,325)
    #web
    AreaDibujo.create_line(149,318,203,210)
    AreaDibujo.create_line(300,200,400,200)
    AreaDibujo.create_line(500,200,590,200)

    AreaDibujo.create_line(650,260,650,400)
    AreaDibujo.create_line(296,180,404,180)
    AreaDibujo.create_line(407,230,253,402)
    AreaDibujo.create_line(600,230,269,408)
    #ebay
    AreaDibujo.create_line(149,332,203,440)
    AreaDibujo.create_line(300,450,400,450)
    AreaDibujo.create_line(500,450,600,450)
    AreaDibujo.create_line(700,450,770,450)

    AreaDibujo.create_line(250,400,250,250)
    AreaDibujo.create_line(405,424,265,247)
    AreaDibujo.create_line(298,430,403,430)
    AreaDibujo.create_line(618,410,280,240)
    AreaDibujo.create_line(787,405,294,225)

    #creacion de arcos de transicion
    #inicio
    AreaDibujo.create_arc(60,240,110,305,start=-8,extent=219,style=ARC)
    #web
    AreaDibujo.create_arc(210,125,260,185,start=2,extent=210,style=ARC)
    AreaDibujo.create_arc(110,190,400,450,start=112,extent=50,style=ARC)
    AreaDibujo.create_arc(150,100,750,650,start=55,extent=72,style=ARC)
    AreaDibujo.create_arc(20,55,720,395,start=26,extent=181,style=ARC)
    AreaDibujo.create_arc(78,85,480,500,start=41,extent=137,style=ARC)

    #ebay
    AreaDibujo.create_arc(110,190,400,460,start=200,extent=48,style=ARC)
    AreaDibujo.create_arc(20,240,880,600,start=157,extent=173,style=ARC)
    AreaDibujo.create_arc(200,385,890,550,start=45,extent=95,style=ARC)
    AreaDibujo.create_arc(70,85,770,571,start=189,extent=128,style=ARC)
    AreaDibujo.create_arc(90,85,560,520,start=199,extent=98,style=ARC)
    AreaDibujo.create_arc(250,390,625,550,start=200,extent=146,style=ARC)
    AreaDibujo.create_arc(208,442,285,530,start=172,extent=185,style=ARC)


    #creacion de circulos de indicacion
    #inicio
    AreaDibujo.create_oval(47,322,53,328,fill="black")
    #web
    AreaDibujo.create_oval(52,296,58,302,fill="black")
    AreaDibujo.create_oval(61,285,67,291,fill="black")
    AreaDibujo.create_oval(76,278,82,284,fill="black")
    AreaDibujo.create_oval(115,275,121,281,fill="black")

    AreaDibujo.create_oval(198,209,204,215,fill="black")
    AreaDibujo.create_oval(397,197,403,203,fill="black")
    AreaDibujo.create_oval(587,197,593,203,fill="black")
    AreaDibujo.create_oval(210,166,216,172,fill="black")

    AreaDibujo.create_oval(293,177,299,183,fill="black")
    AreaDibujo.create_oval(269,152,275,158,fill="black")
    AreaDibujo.create_oval(647,397,653,403,fill="black")

    AreaDibujo.create_oval(253,397,259,403,fill="black")
    AreaDibujo.create_oval(268,403,274,409,fill="black")
    #ebay

    #etiquetas
    #inicio
    inicio=Label(ventana,text="inicio",font="Verdana 6").place(x=20,y=305)
    #estados
    #web
    #ebay


    ventana.mainloop()
