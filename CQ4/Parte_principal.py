from tkinter import *
import CONFIGURACION
import Utilidades


ventana = Tk()
ventana.configure(bg="black")   
ventana.geometry(f'{CONFIGURACION.ANCHO}x{CONFIGURACION.ALTO}')  #
ventana.title("Juego Buscaminas")  
ventana.resizable(False, False)  


marco_superior = Frame(
    ventana,
    bg='black',
    width=CONFIGURACION.ANCHO,
    height=Utilidades.altura_pct(25)  
)
marco_superior.place(x=0, y=0)


marco_izquierdo = Frame(
    ventana,
    bg='black',
    width=Utilidades.ancho_pct(25),   
    height=Utilidades.altura_pct(75)  
)
marco_izquierdo.place(x=0, y=Utilidades.altura_pct(25))


marco_central = Frame(
    ventana,
    bg='black',
    width=Utilidades.ancho_pct(75),   
    height=Utilidades.altura_pct(75)  
)
marco_central.place(
    x=Utilidades.ancho_pct(25),       
    y=Utilidades.altura_pct(25),      
)

ventana.mainloop()
