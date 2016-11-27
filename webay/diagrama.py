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
    #ebay
    AreaDibujo.create_line(149,332,203,440)
    AreaDibujo.create_line(300,450,400,450)
    AreaDibujo.create_line(500,450,600,450)
    AreaDibujo.create_line(700,450,770,450)

    #creacion de arcos de transicion
    #inicio
    AreaDibujo.create_arc(60,240,110,305,start=-8,extent=219,style=ARC)
    #web
    AreaDibujo.create_arc(210,125,260,185,start=2,extent=210,style=ARC)
    AreaDibujo.create_arc(110,190,400,450,start=112,extent=50,style=ARC)
    AreaDibujo.create_arc(150,100,750,650,start=55,extent=72,style=ARC)




    #ebay


    #creacion de circulos de indicacion
    #web
    #ebay



    ventana.mainloop()
