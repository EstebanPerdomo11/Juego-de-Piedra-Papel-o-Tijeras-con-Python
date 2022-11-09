import random
from tkinter import *# con el * de esta manera se importa todos los métodos de esta libreria, import tkinter --> también se puede importar así una libreria, la diferencia que cada método que vaya a llamar tiene que poner prinero tkinter. + el método, por ejemplo: tkinter.Tk()
from tkinter import messagebox
from PIL import Image, ImageTk #Esta libreria lo que permitirá es agregar imagenes, para poder agregarle a los botones como es en este caso. El método Image sirve para modificar el tamaño de la imagen.

victorias_jugador = 0
victorias_máquina = 0
rondas = 3 
print(rondas)
############################################# Creación de funciones ######################################################

def eleccion_maquina(): #Esta función permite saber que tiró la máquina 

    opcion = ['piedra','papel','tijera']
    return random.choice(opcion)

def Logica_juego(eleccion_jugador):
    
    global rondas, victorias_jugador, victorias_máquina

    if rondas != 0:
        eleccionMaquina= eleccion_maquina()
        # Lógica elección de la máquina
        if eleccionMaquina == "tijera":
            imagen_seleccion_maquina = Tijera_imagen_procesada
        elif eleccionMaquina == "piedra":
            imagen_seleccion_maquina = Piedra_imagen_procesada    
        else:
            imagen_seleccion_maquina = Papel_imagen_procesada
    
        eleccion_maquina_label.config(image=imagen_seleccion_maquina)

         # Condición de empate
        if eleccion_jugador == eleccionMaquina:
           #resultado_maquina.config(text="Es un empate")  
           aceptar = messagebox.showinfo(message="Empate")

        # Condición del jugador
        elif (eleccion_jugador == "piedra" and eleccionMaquina == "tijera") or (eleccion_jugador == "papel" and eleccionMaquina == "piedra") or (eleccion_jugador == "tijera" and eleccionMaquina =="papel"):
            #resultado_maquina.config(text ="¡¡ Gana el jugador !!")
            aceptar = messagebox.showinfo(message="Gana el jugador")
            victorias_jugador += 1

            if victorias_jugador ==3:
                ganador = "¡ Felicidades ganaste !"
            
        # Condición de la máquina
        elif (eleccion_jugador == "piedra" and eleccionMaquina == "papel") or (eleccion_jugador == "papel" and eleccionMaquina == "tijera") or (eleccion_jugador == "tijera" and eleccionMaquina == "piedra"):
            aceptar = messagebox.showinfo(message="Gana la máquina")
            rondas -=1 
            victorias_máquina +=1
            if victorias_máquina ==3:
                ganador = "Perdiste contra la máquina :c, lloremos!!"
    
    T_rondas.config(text=" Cantidad de rondas: " + str(rondas))
     
    resultado.config(text="______________________________\n  jugador             máquina  \n     "+ str(victorias_jugador) + "                            " +str(victorias_máquina)+ "     \n______________________________")

    if aceptar == "ok":
        eleccion_maquina_label.config(image=Incognita_imagen_procesada)

    if victorias_máquina == 3 or  victorias_jugador == 3:
        if not messagebox.askyesno(title="Fin del juego", message= ganador +"\n\n¿Quieres jugar de nuevo?"):
            # Este método (messagebox) lo que hace es que después de que el usuario haya elegido aparecerá una ventana emergente diciendo que si desea volver a jugar con 2 opciones si o no, si el usuario precionó no entonces la función exit(), saldrá de la ventana emergente y de la de juego haciendo que se cierre todo el juego.
            ventana_base.destroy()
        else:
            rondas = 3
            victorias_jugador = 0
            victorias_máquina = 0
            resultado.config(text="______________________________\n  jugador             máquina  \n     "+ str(victorias_jugador) + "                            " +str(victorias_máquina)+ "     \n______________________________")
            T_rondas.config(text= " Cantidad de rondas: " + str(rondas))
    
def eligio_tijera():
    Logica_juego("tijera")

def eligio_papel():
    Logica_juego("papel")
     
def eligio_piedra():
    Logica_juego("piedra")


#########################################################################################################################
ventana_base = Tk() #Esta función permite que de una ventana principal 
ventana_base.title("Play of stone, paper and scissor")

########################################################################################################################
                  # Creación del objeto tipo imagen --> Estaa parte es solo de la libreria de PILOT 

#Tijera_imagen = PhotoImage(file="./tijera.png") PhotoImage sirve para procesar la imagen, pero usaremos otra para hacer la modifcación del tamaño. 
Tijera_imagen = Image.open("./tijera.png") # Esta linea sirve para traer la imagen en la programación.
Tijera_imagen_redimensionada = Tijera_imagen.resize((120, 160), Image.ANTIALIAS) # Ajustar el tamaño de la imagen, Image.NEAREST sirve para ajustar la visualización de la imagen si quiere pixeleadas o no, hay más métodos aparte de NEAREST.
Tijera_imagen_procesada = ImageTk.PhotoImage(Tijera_imagen_redimensionada)#Ahora debe que unir esta parte con la libreria de Tkinter

Papel_imagen = Image.open("./papel.png")
Papel_imagen_redimensionada = Papel_imagen.resize((120, 160), Image.ANTIALIAS)
Papel_imagen_procesada = ImageTk.PhotoImage(Papel_imagen_redimensionada)

Piedra_imagen = Image.open("./piedra.png")
Piedra_imagen_redimensionada = Piedra_imagen.resize((120, 160), Image.ANTIALIAS)
Piedra_imagen_procesada = ImageTk.PhotoImage(Piedra_imagen_redimensionada)

Incognita_imagen = Image.open("./incognita.png")
Incognita_imagen_redimensionada = Incognita_imagen.resize((120, 160), Image.ANTIALIAS)
Incognita_imagen_procesada = ImageTk.PhotoImage(Incognita_imagen_redimensionada)
########################################################################################################################
                                           #De la liberia Tkinter 

contenedor = Frame(ventana_base, bg= "gold", width= 1100, height= 600, cursor="dot #0BF3E8") # -->Los Frames son una capa que se hace encina de la ventana base(Los Frames son marcos contenedores de otros widgets. Pueden tener tamaño propio y posicionarse en distintos lugares).
contenedor.pack()#--> pack es una función que permite empaquetar todo lo que hay dentro de la variable contenedor,dentro de esta función se le agrega 2 argumentos (fill and expand) fill = llenar y se puede hacer un llenado x, y both y none pero por defecto viene en none al momento de declararlo, el expand lo que hace es ajustarse al tamaño de la pantalla en este caso es (contenedor).También se le puede dar un tamaño al contenedor para que no se expanda en todo el contenedor, para esto se hace esto: contenedor.config(width="1100", height="600").

#Etiqueta 
#Las etiquetas es la forma en la que podemos ver texto en las interfaces gráficas
titulo =Label(contenedor, text="                      Bienvenido al juego de piedra, papel o tijera", bg="gold", fg="red", font= ("Agency FB",24))
titulo.grid(row=0, column=1)#El grid es una forma para posicionar lo que usted quiera en la venta para que se vea mejor al momento de correrlo
descripcion= Label(contenedor, text= "A continuación se muestran 3 botones donde podrás elegir entre piedra, papel o tijera,\nla máquina también hará su elección. Las reglas son:\n    1.Piedra le gana a tijera.      2.Papel le gana a piedra.      3.Tijera le gana a papel      \n", bg="gold",fg="black",  font=("Agency FB",24))
descripcion.grid(row=1, column=0, columnspan=3)

#Botones
tijera = Button(contenedor, command= eligio_tijera, image= Tijera_imagen_procesada, bg= "Gray", border=10, text = "tijera")#La función command sirve para darle como prametro una función y así darle un funcionamiento al boton.
tijera.grid(row=2, column=0)

papel = Button(contenedor, command= eligio_papel, image= Papel_imagen_procesada, bg="Gray", bd = 10, text= "papel")
papel.grid(row=2, column=1)

piedra = Button(contenedor, command= eligio_piedra, image= Piedra_imagen_procesada, bg="Gray", bd = 10, text= "piedra")
piedra.grid(row=2, column=2)

######################################### ELECCION MAQUINA Y SU RESULTADO ################################################
maquina = Label(contenedor, text="La máquina eligió: ", bg ="gold", font=("Agency FB", 24), fg="black", justify="center", padx = 40)
maquina.grid(row=3, column=0)
eleccion_maquina_label = Label(contenedor, image =Incognita_imagen_procesada,bg="gold", border=30, pady= 20 )#El pady es un espacio que va a estar entre el objeto y la margen del objeto.
eleccion_maquina_label.grid(row=3, column=1) 
##########################################################################################################################
resultado = Label(contenedor, text="______________________________\n  jugador             máquina  \n     "+ str(victorias_jugador) + "                            " +str(victorias_máquina)+ "     \n______________________________", bg="gold", font=("Agency FB",24), fg="black", justify="center",padx= 40)
resultado.grid(row=3, column=2)
################################################# RONDAS DE JUEGO ########################################################

T_rondas= Label(contenedor, text= " Cantidad de rondas: " + str(rondas), bg= "gold", font=("Agency FB", 24), fg= "black", justify="center", pady= -250, padx= 40)
T_rondas.grid(row=4, column=0)

##########################################################################################################################
ventana_base.mainloop()# -->mainloop es una función de la libreria y es una clase de bucle en la que se encierra un programa. Y es necesario para que se esté ejecutando constantemente.Cada ventana se necesita de evento, los eventos son lo que sucede dentro de la ventana.
