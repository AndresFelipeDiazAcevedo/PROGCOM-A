import itertools
import random
import tkinter as tk
from tkinter import ttk, messagebox




def generar_numero():
    """Genera un número de 4 dígitos sin repetidos."""
    digitos = random.sample("0123456789", 4)
    while digitos[0] == "0":
        digitos = random.sample("0123456789", 4)
    return "".join(digitos)


def generar_todas():
    """Genera todas las combinaciones posibles."""
    numeros = []
    for comb in itertools.permutations("0123456789", 4):
        if comb[0] != "0":
            numeros.append("".join(comb))
    return numeros


def evaluar(n1, n2):
    """Devuelve picas y fijas entre dos números."""
    fijas = sum(a == b for a, b in zip(n1, n2))
    picas = sum(min(n1.count(d), n2.count(d)) for d in set(n1)) - fijas
    return picas, fijas



class PicasFijasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Picas y Fijas — Juego Completo ")
        self.root.geometry("520x620")
        self.root.resizable(False, False)

        # Canvas de fondo
        self.canvas = tk.Canvas(root, width=520, height=620, highlightthickness=0)
        self.canvas.pack()
        self._draw_gradient("#ffde9f", "#f29f5c")

        # frame contenedor
        self.main_frame = tk.Frame(root, bg="white")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=550)

        self.menu_principal()



    def menu_principal(self):
        self.limpiar_frame()

        tk.Label(self.main_frame, text=" Picas y Fijas",
                 font=("Arial Rounded MT Bold", 28), bg="white").pack(pady=20)

        ttk.Button(self.main_frame, text="1️  Yo adivino",
                   command=self.modo_jugador, width=25).pack(pady=20)

        ttk.Button(self.main_frame, text="2️  La máquina adivina",
                   command=self.modo_maquina, width=25).pack(pady=20)



    def modo_jugador(self):
        self.limpiar_frame()

        self.secreto = generar_numero()

        tk.Label(self.main_frame, text=" Adivina el número",
                 font=("Arial Rounded MT Bold", 20), bg="white").pack(pady=10)

        self.entry = ttk.Entry(self.main_frame, font=("Consolas", 20), justify="center")
        self.entry.pack(pady=10)

        ttk.Button(self.main_frame, text="Probar", command=self.probar_jugador)\
            .pack(pady=10)

        self.hist_jugador = tk.Text(self.main_frame, height=17, width=40,
                                    font=("Consolas", 12))
        self.hist_jugador.pack()

        ttk.Button(self.main_frame, text=" Volver", command=self.menu_principal)\
            .pack(pady=10)

    def probar_jugador(self):
        intento = self.entry.get()

        if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
            messagebox.showerror("Error", "Debe ser un número válido de 4 dígitos sin repetidos.")
            return

        p, f = evaluar(intento, self.secreto)
        self.hist_jugador.insert(tk.END, f"{intento} → {p} P | {f} F\n")

        if f == 4:
            messagebox.showinfo(" Ganaste", f"El número era {self.secreto}")
            self.menu_principal()



    def modo_maquina(self):
        self.limpiar_frame()

        tk.Label(self.main_frame, text=" La máquina adivina",
                 font=("Arial Rounded MT Bold", 20), bg="white").pack(pady=10)

        self.posibles = generar_todas()
        self.intento_actual = None

        self.label_intento = tk.Label(self.main_frame, text="(Haz clic en Intento)",
                                      font=("Consolas", 22), bg="white")
        self.label_intento.pack(pady=20)

        ttk.Button(self.main_frame, text="Hacer intento",
                   command=self.hacer_intento).pack(pady=10)

        frame = tk.Frame(self.main_frame, bg="white")
        frame.pack(pady=10)

        tk.Label(frame, text="Picas:", bg="white").grid(row=0, column=0)
        tk.Label(frame, text="Fijas:", bg="white").grid(row=1, column=0)

        self.entry_p = ttk.Entry(frame, width=5)
        self.entry_f = ttk.Entry(frame, width=5)

        self.entry_p.grid(row=0, column=1)
        self.entry_f.grid(row=1, column=1)

        ttk.Button(self.main_frame, text="Verificar",
                   command=self.verificar_maquina).pack(pady=10)

        self.hist_maquina = tk.Text(self.main_frame, height=13, width=42,
                                    font=("Consolas", 12))
        self.hist_maquina.pack()

        ttk.Button(self.main_frame, text=" Volver",
                   command=self.menu_principal).pack(pady=10)

    def hacer_intento(self):
        """La máquina elige un número NO repetido y válido."""
        if not self.posibles:
            messagebox.showerror("Error", "No quedan posibilidades. Revisar tus respuestas.")
            return

        import random
        self.intento_actual = random.choice(self.posibles)
        self.label_intento.config(text=self.intento_actual)

    def verificar_maquina(self):
        """El usuario da picas/fijas y la máquina filtra posibilidades."""
        if self.intento_actual is None:
            messagebox.showerror("Error", "Primero presiona 'Hacer intento'.")
            return

        # leer entradas del usuario
        try:
            p = int(self.entry_p.get())
            f = int(self.entry_f.get())
        except:
            messagebox.showerror("Error", "Ingresa números válidos.")
            return

        # mostrar en historial
        self.hist_maquina.insert(tk.END, f"{self.intento_actual} → {p} P | {f} F\n")

        if f == 4:
            messagebox.showinfo(" La máquina ganó",
                                f"Tu número era {self.intento_actual}")
            self.menu_principal()
            return

        # eliminar intento actual (para que no se repita)
        if self.intento_actual in self.posibles:
            self.posibles.remove(self.intento_actual)

        nuevas = []
        for num in self.posibles:
            p2, f2 = evaluar(self.intento_actual, num)
            if p == p2 and f == f2:
                nuevas.append(num)

        self.posibles = nuevas


        self.entry_p.delete(0, tk.END)
        self.entry_f.delete(0, tk.END)

        self.intento_actual = None
        self.label_intento.config(text="(Haz clic en Intento)")



    def _draw_gradient(self, c1, c2):
        r1, g1, b1 = self.root.winfo_rgb(c1)
        r2, g2, b2 = self.root.winfo_rgb(c2)

        for i in range(620):
            r = int(r1 + (r2 - r1) * i / 620)
            g = int(g1 + (g2 - g1) * i / 620)
            b = int(b1 + (b2 - b1) * i / 620)
            hex_color = f"#{r//256:02x}{g//256:02x}{b//256:02x}"
            self.canvas.create_line(0, i, 520, i, fill=hex_color)


    def limpiar_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()



root = tk.Tk()
PicasFijasApp(root)
root.mainloop()
