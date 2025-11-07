import tkinter as tk
from tkinter import messagebox
import numpy as np

class SistemaEcuacionesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resolver Sistema de Ecuaciones")
        self.root.geometry("400x400")

        # Título
        tk.Label(root, text="Sistema de Ecuaciones Lineales", font=("Arial", 14, "bold")).pack(pady=10)

        # Entradas para tamaño de matriz
        tk.Label(root, text="Número de incógnitas (n):").pack()
        self.entry_n = tk.Entry(root, width=5)
        self.entry_n.pack(pady=5)

        tk.Button(root, text="Crear matriz", command=self.crear_matriz).pack(pady=10)

        self.frame_matriz = tk.Frame(root)
        self.frame_matriz.pack()

        self.btn_resolver = tk.Button(root, text="Resolver", command=self.resolver_sistema)
        self.btn_resolver.pack(pady=10)

        self.resultado_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.resultado_label.pack(pady=10)

    def crear_matriz(self):
        # Limpiar frame anterior
        for widget in self.frame_matriz.winfo_children():
            widget.destroy()
        try:
            self.n = int(self.entry_n.get())
            self.entries_A = []
            self.entries_B = []

            tk.Label(self.frame_matriz, text="Matriz de coeficientes A:").grid(row=0, column=0, columnspan=self.n)
            for i in range(self.n):
                fila_entries = []
                for j in range(self.n):
                    e = tk.Entry(self.frame_matriz, width=5)
                    e.grid(row=i+1, column=j, padx=2, pady=2)
                    fila_entries.append(e)
                self.entries_A.append(fila_entries)

            tk.Label(self.frame_matriz, text="Vector resultados B:").grid(row=self.n+1, column=0, columnspan=self.n)
            for i in range(self.n):
                e = tk.Entry(self.frame_matriz, width=5)
                e.grid(row=self.n+2+i, column=0, padx=2, pady=2)
                self.entries_B.append(e)

        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido de incógnitas.")

    def resolver_sistema(self):
        try:
            # Leer matriz A
            A = np.array([[float(self.entries_A[i][j].get()) for j in range(self.n)] for i in range(self.n)])
            # Leer vector B
            B = np.array([float(self.entries_B[i].get()) for i in range(self.n)])

            # Resolver sistema
            x = np.linalg.solve(A, B)

            # Mostrar resultados
            resultado_texto = "Solución:\n" + "\n".join([f"x{i+1} = {v:.2f}" for i, v in enumerate(x)])
            self.resultado_label.config(text=resultado_texto)

        except np.linalg.LinAlgError:
            messagebox.showerror("Error", "El sistema no tiene solución o la matriz es singular.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, llena todas las entradas con números válidos.")

root = tk.Tk()
app = SistemaEcuacionesApp(root)
root.mainloop()
