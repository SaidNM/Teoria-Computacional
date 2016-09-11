from tkinter import *

def mostrarDiagrama():
	ventana =  Tk()
	ventana.geometry("700x500")  #geometry(widthxheight)
	ventana.title("Protocolo")
	ventana.resizable(width=False,height=False)
	AreaDibujo=Canvas(ventana,width=700,height=500)
	AreaDibujo.pack()

	#Ovalo transicion
	AreaDibujo.create_oval(165,120,530,385)
	AreaDibujo.create_oval(560,170,660,270)


	#Estados del protocolo
	AreaDibujo.create_oval(100,185,230,315,fill="bisque2")
	AreaDibujo.create_oval(465,185,595,315,fill="bisque2")

	#linea de inicio
	AreaDibujo.create_line(30,250,100,250)
	AreaDibujo.create_oval(95,245,105,255,fill="black")

	#circulos de sentido
	AreaDibujo.create_oval(180,310,190,320,fill="black")
	AreaDibujo.create_oval(500,180,510,190,fill="black")
	AreaDibujo.create_oval(590,263,600,273,fill="black")



	#etiqueta inicio
	start=Label(ventana,text="Start",font="Verdana 11 roman").place(x=40,y=220)
	#etiquetas
	datain=Label(ventana,text="Data in",font="Verdana 11 roman").place(x=325,y=90)
	timeout=Label(ventana,text="Time out",font="Verdana 11 roman").place(x=590,y=140)
	ACK=Label(ventana,text="ACK",font="Verdana 11 roman").place(x=335,y=405)

	#etiquetas de estado del protocolo
	ready=Label(ventana,text="Ready",font="Verdana 11 italic",background="bisque2").place(x=138,y=235)
	sending=Label(ventana,text="Sending",font="Verdana 11 italic",background="bisque2").place(x=498,y=235)

	ventana.mainloop()