import tkinter as tk
from tkinter import messagebox
import random


def verificar_ganador(tablero):
    combinaciones = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a,b,c in combinaciones:
        if tablero[a] == tablero[b] == tablero[c] and tablero[a] != "":
            return tablero[a]
    if "" not in tablero:
        return "Empate"
    return None

def minimax(tablero, es_maximizador, maquina, humano):
    ganador = verificar_ganador(tablero)
    if ganador == maquina:
        return 1
    elif ganador == humano:
        return -1
    elif ganador == "Empate":
        return 0

    if es_maximizador:
        mejor_puntaje = -100
        for i in range(9):
            if tablero[i] == "":
                tablero[i] = maquina
                puntaje = minimax(tablero, False, maquina, humano)
                tablero[i] = ""
                mejor_puntaje = max(puntaje, mejor_puntaje)
        return mejor_puntaje
    else:
        mejor_puntaje = 100
        for i in range(9):
            if tablero[i] == "":
                tablero[i] = humano
                puntaje = minimax(tablero, True, maquina, humano)
                tablero[i] = ""
                mejor_puntaje = min(puntaje, mejor_puntaje)
        return mejor_puntaje

def mejor_jugada(tablero, maquina, humano):
    mejor_puntaje = -100
    movimiento = None
    for i in range(9):
        if tablero[i] == "":
            tablero[i] = maquina
            puntaje = minimax(tablero, False, maquina, humano)
            tablero[i] = ""
            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                movimiento = i
    return movimiento

# TKINTERRRRRRRRRRR

class TresEnRaya:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Tres en Raya HQ3")
        self.tablero = ["" for _ in range(9)]
        self.botones = []
        self.humano = "X"
        self.maquina = "O"
        self.turno = "humano"
        self.dificultad = "Difícil"
        self.pantalla_inicio()

    def pantalla_inicio(self):
        self.limpiar()
        tk.Label(self.raiz, text="¡Bienvenido al Tres en Raya!", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.raiz, text="Elige tu símbolo:", font=("Arial", 14)).pack(pady=5)
        tk.Button(self.raiz, text="Jugar con X", font=("Arial", 18), width=12,
                  command=lambda: self.seleccionar_dificultad("X")).pack(pady=5)
        tk.Button(self.raiz, text="Jugar con O", font=("Arial", 18), width=12,
                  command=lambda: self.seleccionar_dificultad("O")).pack(pady=5)

    def seleccionar_dificultad(self, simbolo):
        self.humano = simbolo
        self.maquina = "O" if simbolo == "X" else "X"
        self.limpiar()
        tk.Label(self.raiz, text="Selecciona la dificultad:", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(self.raiz, text="Fácil", font=("Arial", 16), width=12,
                  command=lambda: self.iniciar_juego("Fácil")).pack(pady=5)
        tk.Button(self.raiz, text="Medio", font=("Arial", 16), width=12,
                  command=lambda: self.iniciar_juego("Medio")).pack(pady=5)
        tk.Button(self.raiz, text="Difícil", font=("Arial", 16), width=12,
                  command=lambda: self.iniciar_juego("Difícil")).pack(pady=5)

    def iniciar_juego(self, dificultad):
        self.dificultad = dificultad
        self.limpiar()
        self.crear_tablero()
        self.turno = "humano" if self.humano == "X" else "maquina"
        if self.turno == "maquina":
            self.turno_maquina()

    def crear_tablero(self):
        marco = tk.Frame(self.raiz)
        marco.pack()
        for i in range(9):
            boton = tk.Button(marco, text="", font=("Arial", 26), width=4, height=2,
                              command=lambda i=i: self.turno_humano(i))
            boton.grid(row=i//3, column=i%3)
            self.botones.append(boton)

    def turno_humano(self, i):
        if self.tablero[i] == "" and self.turno == "humano":
            self.tablero[i] = self.humano
            self.botones[i].config(text=self.humano, state="disabled")
            self.turno = "maquina"
            self.verificar_juego()
            if self.turno == "maquina":
                self.raiz.after(500, self.turno_maquina)

    def turno_maquina(self):
        movimiento = None
        if self.dificultad == "Fácil":
            disponibles = [i for i in range(9) if self.tablero[i] == ""]
            movimiento = random.choice(disponibles)
        elif self.dificultad == "Medio":
            if random.random() < 0.5:
                movimiento = mejor_jugada(self.tablero, self.maquina, self.humano)
            else:
                disponibles = [i for i in range(9) if self.tablero[i] == ""]
                movimiento = random.choice(disponibles)
        else:
            movimiento = mejor_jugada(self.tablero, self.maquina, self.humano)

        if movimiento is not None:
            self.tablero[movimiento] = self.maquina
            self.botones[movimiento].config(text=self.maquina, state="disabled")

        self.turno = "humano"
        self.verificar_juego()

    def verificar_juego(self):
        ganador = verificar_ganador(self.tablero)
        if ganador:
            if ganador == "Empate":
                mensaje = "¡Empate!"
            elif ganador == self.humano:
                mensaje = "¡Ganaste! "
            else:
                mensaje = "La máquina ha ganado "
            messagebox.showinfo("Resultado", mensaje)
            self.reiniciar()

    def reiniciar(self):
        for boton in self.botones:
            boton.destroy()
        self.botones.clear()
        self.tablero = ["" for _ in range(9)]
        self.pantalla_inicio()

    def limpiar(self):
        for widget in self.raiz.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    raiz = tk.Tk()
    app = TresEnRaya(raiz)
    raiz.mainloop()
