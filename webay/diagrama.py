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
    AreaDibujo.create_oval(53,346,59,352,fill="black")
    AreaDibujo.create_oval(72,365,78,371,fill="black")
    AreaDibujo.create_oval(102,372,108,378,fill="black")
    AreaDibujo.create_oval(117,368,123,374,fill="black")

    AreaDibujo.create_oval(199,436,205,442,fill="black")
    AreaDibujo.create_oval(206,476,212,482,fill="black")
    AreaDibujo.create_oval(297,447,303,453,fill="black")

    AreaDibujo.create_oval(259,495,265,501,fill="black")
    AreaDibujo.create_oval(278,411,284,417,fill="black")
    AreaDibujo.create_oval(247,247,253,253,fill="black")
    AreaDibujo.create_oval(399,427,405,433,fill="black")

    AreaDibujo.create_oval(263,245,269,251,fill="black")
    AreaDibujo.create_oval(597,447,603,453,fill="black")

    AreaDibujo.create_oval(276,238,282,244,fill="black")
    AreaDibujo.create_oval(768,447,774,453,fill="black")

    AreaDibujo.create_oval(292,223,298,229,fill="black")

    #etiquetas
    #inicio
    inicio=Label(ventana,text="inicio",font="Verdana 6").place(x=20,y=305)
    #estados
    q0=Label(ventana,text="q0",font="Verdana 10",background="sky blue").place(x=90,y=317)
    q1=Label(ventana,text="q1",font="Verdana 10",background="sky blue").place(x=240,y=190)
    q2=Label(ventana,text="q2",font="Verdana 10",background="sky blue").place(x=440,y=190)
    q3=Label(ventana,text="q3",font="Verdana 10",background="sky blue").place(x=640,y=190)
    q4=Label(ventana,text="q4",font="Verdana 10",background="sky blue").place(x=240,y=440)
    q5=Label(ventana,text="q5",font="Verdana 10",background="sky blue").place(x=440,y=440)
    q6=Label(ventana,text="q6",font="Verdana 10",background="sky blue").place(x=640,y=440)
    q7=Label(ventana,text="q7",font="Verdana 10",background="sky blue").place(x=820,y=440)
    #web
    w1=Label(ventana,text="w",font="Verdana 7").place(x=165,y=285)
    w2=Label(ventana,text="no es w,e",font="Verdana 7").place(x=125,y=212)
    w3=Label(ventana,text="e",font="Verdana 7").place(x=165,y=345)
    w4=Label(ventana,text="w",font="Verdana 7").place(x=390,y=160)
    w5=Label(ventana,text="e",font="Verdana 7").place(x=310,y=190)
    w6=Label(ventana,text="w",font="Verdana 7").place(x=220,y=120)
    w7=Label(ventana,text="w",font="Verdana 7").place(x=455,y=105)

    w8=Label(ventana,text="b",font="Verdana 7").place(x=510,y=190)
    w9=Label(ventana,text="no es w,e,a",font="Verdana 7").place(x=455,y=40)
    w10=Label(ventana,text="no es w,e,b",font="Verdana 7").place(x=245,y=95)
    w11=Label(ventana,text="e",font="Verdana 7").place(x=390,y=215)
    w12=Label(ventana,text="e",font="Verdana 7").place(x=580,y=215)
    w13=Label(ventana,text="a",font="Verdana 7").place(x=660,y=270)
    #ebay
    e1=Label(ventana,text="no es w,e,b",font="Verdana 6").place(x=120,y=385)
    e2=Label(ventana,text="e",font="Verdana 7").place(x=263,y=525)
    e3=Label(ventana,text="b",font="Verdana 7").place(x=310,y=412)
    e4=Label(ventana,text="e",font="Verdana 7").place(x=380,y=455)
    e5=Label(ventana,text="a",font="Verdana 7").place(x=510,y=430)
    e6=Label(ventana,text="y",font="Verdana 7").place(x=710,y=430)

    e7=Label(ventana,text="e",font="Verdana 7").place(x=710,y=400)
    e8=Label(ventana,text="e",font="Verdana 7").place(x=580,y=476)
    e9=Label(ventana,text="w",font="Verdana 7").place(x=710,y=355)
    e10=Label(ventana,text="w",font="Verdana 7").place(x=550,y=355)
    e11=Label(ventana,text="w",font="Verdana 7").place(x=370,y=360)
    e12=Label(ventana,text="w",font="Verdana 7").place(x=230,y=370)

    e13=Label(ventana,text="no es w,e",font="Verdana 7").place(x=450,y=605)
    e14=Label(ventana,text="no es w,e,a",font="Verdana 7").place(x=425,y=505)
    e15=Label(ventana,text="no es e,y,w",font="Verdana 7").place(x=470,y=570)
    e16=Label(ventana,text="no es w,e",font="Verdana 6").place(x=35,y=220)




    ventana.mainloop()
