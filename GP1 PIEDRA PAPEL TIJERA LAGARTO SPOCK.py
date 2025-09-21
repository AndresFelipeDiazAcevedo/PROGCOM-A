import tkinter as tk
import random

# opciones de cada jugador con los emogis pa que se vea mas chimba
opciones = {
    "Piedra": "✊",
    "Papel": "✋",
    "Tijera": "✌️",
    "Lagarto": "🦎",
    "Spock": "🖖"
}

# Que le gana a que
reglas = {
    "Piedra": ["Tijera", "Lagarto"],
    "Papel": ["Piedra", "Spock"],
    "Tijera": ["Papel", "Lagarto"],
    "Lagarto": ["Papel", "Spock"],
    "Spock": ["Tijera", "Piedra"]
}

def jugar(eleccion_jugador):
    eleccion_pc = random.choice(list(opciones.keys()))
    if eleccion_jugador == eleccion_pc:
        resultado.set(f"Empate: ambos eligieron {opciones[eleccion_jugador]} {eleccion_jugador}")
    elif eleccion_pc in reglas[eleccion_jugador]:
        resultado.set(f"¡Ganaste! {opciones[eleccion_jugador]} {eleccion_jugador} vence a {opciones[eleccion_pc]} {eleccion_pc}")
    else:
        resultado.set(f"Perdiste. {opciones[eleccion_pc]} {eleccion_pc} vence a {opciones[eleccion_jugador]} {eleccion_jugador}")

# parte de Interfaz grafica con tkinter
ventana = tk.Tk()
ventana.title("Piedra, Papel, Tijera, Lagarto, Spock")

resultado = tk.StringVar()
resultado.set("Elige una opción para jugar")

# Etiqueta de resultado que te dice quién gano
lbl = tk.Label(ventana, textvariable=resultado, font=("Arial", 12))
lbl.pack(pady=10)

# Esta es la parte cque tiene los botones para cada opción
for opcion, icono in opciones.items():
    b = tk.Button(ventana, text=f"{icono} {opcion}", width=20, command=lambda o=opcion: jugar(o))
    b.pack(pady=5)

ventana.mainloop()
