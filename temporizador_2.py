# Juego_Matriz_Aritmetico
import tkinter as tk
from tkinter import messagebox

class Temporizador:
    def __init__(self, tiempo_limite):
        self.tiempo_limite = tiempo_limite
        self.tiempo_restante = tiempo_limite
        self.timer_running = False

        self.root = tk.Tk()
        self.root.title("Temporizador")

        self.label = tk.Label(self.root, text="")
        self.label.pack(padx=50, pady=20)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        self.btn_ingresar = tk.Button(self.root, text="Ingresar", command=self.ingresar)
        self.btn_ingresar.pack(pady=10)

        self.btn_reiniciar = tk.Button(self.root, text="Reiniciar", command=self.reiniciar)
        self.btn_reiniciar.pack(pady=10)
        self.btn_reiniciar.config(state="disabled")

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.countdown()

    def countdown(self):
        minutos = self.tiempo_restante // 60
        segundos = self.tiempo_restante % 60

        tiempo_restante = f"{minutos:02d}:{segundos:02d}"
        self.label.config(text=tiempo_restante)

        if self.timer_running and self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.root.after(1000, self.countdown)
        elif self.tiempo_restante == 0:
            messagebox.showinfo("Temporizador", "¡Tiempo terminado!")
            self.timer_running = False
            self.btn_reiniciar.config(state="normal")

    def ingresar(self):
        if self.timer_running:
            dato = self.entry.get()
            self.timer_running = False
            self.label.config(text="Temporizador detenido")
            messagebox.showinfo("Código ingresado", f"Código: {dato}")
            self.btn_reiniciar.config(state="normal")

    def reiniciar(self):
        self.tiempo_restante = self.tiempo_limite
        self.timer_running = False
        self.btn_reiniciar.config(state="disabled")
        self.label.config(text="")
        self.start_timer()

    def start(self):
        self.start_timer()
        self.root.mainloop()

# Crear un temporizador de 10 segundos
temporizador = Temporizador(10)
temporizador.start()
