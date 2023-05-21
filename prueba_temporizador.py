# Juego_Matriz_Aritmetico
import time
import os

def temporizador(i):

    while i > 0:
        print("Su tiempo restante es de: ", i ," segundos")
        i = i - 1
        time.sleep(1)
        os.system("cls")
    
temporizador(15)
