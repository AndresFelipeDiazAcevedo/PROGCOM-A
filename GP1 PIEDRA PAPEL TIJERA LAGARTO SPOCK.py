import tkinter as tk
import random

# Opciones del juego
opciones = ["Piedra", "Papel", "Tijera", "Lagarto", "Spock"]

# Reglas: cada opción a qué le gana
reglas = {
    "Piedra": ["Tijera", "Lagarto"],
    "Papel": ["Piedra", "Spock"],
    "Tijera": ["Papel", "Lagarto"],
    "Lagarto": ["Papel", "Spock"],
    "Spock": ["Tijera", "Piedra"]
}

def jugar(eleccion_jugador):
    eleccion_pc = random.choice(opciones)
    if eleccion_jugador == eleccion_pc:
        resultado.set(f"Empate: ambos eligieron {eleccion_jugador}")
    elif eleccion_pc in reglas[eleccion_jugador]:
        resultado.set(f"¡Ganaste! {eleccion_jugador} vence a {eleccion_pc}")
    else:
        resultado.set(f"Perdiste. {eleccion_pc} vence a {eleccion_jugador}")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Piedra, Papel, Tijera, Lagarto, Spock")

resultado = tk.StringVar()
resultado.set("Elige una opción para jugar")

# Etiqueta de resultado
lbl = tk.Label(ventana, textvariable=resultado, font=("Arial", 12))
lbl.pack(pady=10)

# Botones para cada opción
for opcion in opciones:
    b = tk.Button(ventana, text=opcion, width=15, command=lambda o=opcion: jugar(o))
    b.pack(pady=5)

ventana.mainloop()
