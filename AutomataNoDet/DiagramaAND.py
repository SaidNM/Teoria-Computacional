from tkinter import *
ventana =  Tk()
ventana.geometry("650x500")  #geometry(widthxheight)
ventana.title("Automata no deterministico")
ventana.resizable(width=False,height=False)
AreaDibujo=Canvas(ventana,width=650,height=500)
AreaDibujo.pack()

#circulo transicion
AreaDibujo.create_oval(105,140,195,230)

#Circulos de estado
AreaDibujo.create_oval(100,200,200,300,fill="DarkSeaGreen1")
AreaDibujo.create_oval(300,200,400,300,fill="DarkSeaGreen1")
AreaDibujo.create_oval(490,190,610,310,fill="white")
AreaDibujo.create_oval(500,200,600,300,fill="DarkSeaGreen1")

#lineas de transicion

AreaDibujo.create_line(35,250,100,250)
AreaDibujo.create_line(200,250,300,250)
AreaDibujo.create_line(400,250,490,250)

#Circulos de sentido

AreaDibujo.create_oval(90,245,100,255,fill="black")
AreaDibujo.create_oval(290,245,300,255,fill="black")
AreaDibujo.create_oval(480,245,490,255,fill="black")
AreaDibujo.create_oval(110,206,120,216,fill="black")

#Etiquetas
inicio=Label(ventana,text="Inicio").place(x=30,y=220)
q0=Label(ventana,text="q0",background="DarkSeaGreen1").place(x=142,y=245)
q1=Label(ventana,text="q1",background="DarkSeaGreen1").place(x=342,y=245)
q2=Label(ventana,text="q2",background="DarkSeaGreen1").place(x=542,y=245)
cero=Label(ventana,text="0").place(x=248,y=220)
uno=Label(ventana,text="1").place(x=448,y=220)
cero_uno=Label(ventana,text="0,1").place(x=142,y=112)






ventana.mainloop()