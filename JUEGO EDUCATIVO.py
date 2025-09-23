import tkinter as tk
import random

class MathQuest:
    def __init__(self, root):
        self.root = root
        self.root.title("MathQuest 🎯")
        self.nivel = 1
        self.puntos = 0
        self.pregunta = ""
        self.respuesta = 0

        # Etiquetas
        self.label_nivel = tk.Label(root, text=f"Nivel: {self.nivel}", font=("Arial", 14))
        self.label_nivel.pack(pady=5)

        self.label_puntos = tk.Label(root, text=f"Puntos: {self.puntos}", font=("Arial", 14))
        self.label_puntos.pack(pady=5)

        self.label_pregunta = tk.Label(root, text="Haz clic en 'Nueva Pregunta'", font=("Arial", 16))
        self.label_pregunta.pack(pady=10)

        # Entrada del usuario
        self.entry_respuesta = tk.Entry(root, font=("Arial", 14))
        self.entry_respuesta.pack(pady=5)

        # Botones
        self.btn_pregunta = tk.Button(root, text="Nueva Pregunta", command=self.generar_pregunta, font=("Arial", 12))
        self.btn_pregunta.pack(pady=5)

        self.btn_verificar = tk.Button(root, text="Verificar", command=self.verificar_respuesta, font=("Arial", 12))
        self.btn_verificar.pack(pady=5)

        self.label_resultado = tk.Label(root, text="", font=("Arial", 14))
        self.label_resultado.pack(pady=10)

    def generar_pregunta(self):
        operaciones = ["+", "-", "*", "/"]
        op = random.choice(operaciones)

        if self.nivel == 1:
            a, b = random.randint(1, 10), random.randint(1, 10)
        elif self.nivel == 2:
            a, b = random.randint(5, 20), random.randint(5, 20)
        else:
            a, b = random.randint(10, 50), random.randint(1, 25)

        if op == "/":
            b = random.randint(1, 10)
            self.pregunta = f"{a*b} / {b}"
            self.respuesta = a
        else:
            self.pregunta = f"{a} {op} {b}"
            self.respuesta = eval(self.pregunta)

        self.label_pregunta.config(text=f"➡️ {self.pregunta} = ?")
        self.entry_respuesta.delete(0, tk.END)
        self.label_resultado.config(text="")

    def verificar_respuesta(self):
        try:
            user_resp = int(self.entry_respuesta.get())
            if user_resp == self.respuesta:
                self.label_resultado.config(text="✅ Correcto!", fg="green")
                self.puntos += 10
            else:
                self.label_resultado.config(text=f"❌ Incorrecto. Era {self.respuesta}", fg="red")

            self.label_puntos.config(text=f"Puntos: {self.puntos}")

            # Avanzar de nivel cada 30 puntos
            if self.puntos >= self.nivel * 30:
                self.nivel += 1
                self.label_nivel.config(text=f"Nivel: {self.nivel}")

        except:
            self.label_resultado.config(text="⚠️ Entrada inválida", fg="orange")


# Ejecutar juego
root = tk.Tk()
app = MathQuest(root)
root.mainloop()
