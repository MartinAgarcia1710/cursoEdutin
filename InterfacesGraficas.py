from tkinter import *

root = Tk()
PADY = 10
PADX = 10
root.title("Catálogo de celulares")
#Recizable es para que no pueda ser modificado el tanaño de la ventana por el usuario
#raiz.resizable(width=False, height=False)

#Cambia el icono de la ventana
#raiz.iconbitmap("RUTA DEL ARCHIVO")

#geometry establece el tamaño de la ventana
root.geometry("800x600")

#Cambia el color del fondo
#root.config(bg = "Blue")

miFrame = Frame()

#Empaqueta el frame, en este caso los parametros enviados hacen que al expandir la ventana el frame tambien lo haga
#miFrame.pack(fill = BOTH, expand = "True")
miFrame.pack()
#Cambia el color del frame
#miFrame.config(bg = "Blue")
#establece el tamaño del frame
miFrame.config(width = 800, height = 600)

#cambia el tipo de borde y bd da el grosor
#miFrame.config(bd = 35)
#miFrame.config(relief = "groove")
#cambia el cursor cuando pasa sobre el frame
#miFrame.config(cursor = "pirate")

#miImagen = PhotoImage(file = "imagenes/mario.png")

#LABELS, son textos estaticos
#miLabel = Label(miFrame, text = "holiiii")
#miLabel.place(x = 100, y = 100)
#En este caso uso una imagen como Label
#miLabel2 = Label(miFrame, image=miImagen).place(x = 200, y = 100)
#Label(miFrame, text = "Mundillllllooooooooo", bg = "green", font =("Comic Sans MS", 25) ).place(x = 100, y =150)

#Cuadros de texto
#cuadroTexto = Entry(miFrame)
#cuadroTexto.place(x = 1, y = 1)

cuadroMarca = Entry(miFrame)
cuadroMarca.grid(row = 0, column = 1, padx = PADX, pady = PADY)
cuadroMarca.config(justify = "center")
cuadroModelo = Entry(miFrame)
cuadroModelo.grid(row = 1, column = 1, padx = PADX, pady = PADY)
cuadroModelo.config(justify = "center")
cuadroColor = Entry(miFrame)
cuadroColor.grid(row = 2, column = 1, padx = PADX, pady = PADY)
cuadroColor.config(justify = "center")
cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row = 3, column = 1)
cuadroPassword.config(justify = "center", show = "^")


labelMarca = Label(miFrame, text = "Marca:")
labelMarca.grid(row = 0, column = 0, padx = PADX, pady = PADY)
labelModelo = Label(miFrame, text = "Modelo:")
labelModelo.grid(row = 1, column = 0, padx = PADX, pady = PADY)
labelColor = Label(miFrame, text = "Color:")
labelColor.grid(row = 2, column = 0, padx = PADX, pady = PADY)
labelPassword = Label(miFrame, text = "Password:")
labelPassword.grid(row = 3, column = 0, padx = PADX, pady = PADY)
#Mainloop siempre tiene que quedar al final
root.mainloop()
