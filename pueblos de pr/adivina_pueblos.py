import pandas as pd
import tkinter as tk
from tkinter import messagebox

# TODO: Función para cargar los pueblos desde el archivo CSV
def cargar_pueblos():

# TODO: Función para guardar los pueblos adivinados en un archivo CSV
def guardar_pueblos_acertados():
    

# Función para verificar la respuesta del usuario
def verificar_respuesta():
    global tiempo_restante, temporizador_id
    respuesta = entry.get().strip().lower()
    entry.delete(0, tk.END)
    
    if respuesta == "salir":
        guardar_pueblos_acertados()
        root.quit()
    elif respuesta in pueblos and respuesta not in pueblos_acertados:
        pueblos_acertados.add(respuesta)
        label_feedback.config(text=f"¡Correcto! Pueblos acertados: {len(pueblos_acertados)} / {len(pueblos)}")
        # Reiniciar el temporizador
        root.after_cancel(temporizador_id)
        actualizar_tiempo()
    else:
        label_feedback.config(text="Pueblo incorrecto")
        game_over("GAME OVER, pueblo incorrecto o ya adivinado :)")
    
    if len(pueblos_acertados) == len(pueblos):
        messagebox.showinfo("¡Felicidades!", "¡Has adivinado todos los pueblos de Puerto Rico!")
        guardar_pueblos_acertados()
        root.quit()

# Función para actualizar el temporizador
def actualizar_tiempo():
    global tiempo_restante, temporizador_id
    tiempo_restante = 15
    label_tiempo.config(text=f"Tiempo restante: {tiempo_restante} segundos")
    temporizador_id = root.after(1000, temporizador)

# Función para gestionar el temporizador
def temporizador():
    global tiempo_restante, temporizador_id
    if tiempo_restante > 0:
        tiempo_restante -= 1
        label_tiempo.config(text=f"Tiempo restante: {tiempo_restante} segundos")
        temporizador_id = root.after(1000, temporizador)
    else:
        game_over("Se ha agotado el tiempo para esta respuesta.")

# Función para manejar el fin del juego
def game_over(mensaje):
    messagebox.showinfo("Game Over", mensaje)
    guardar_pueblos_acertados()
    root.quit()

# Inicializar variables
pueblos = cargar_pueblos()
pueblos_acertados = set()
tiempo_restante = 15
temporizador_id = None

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Adivina los Pueblos de Puerto Rico")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_instrucciones = tk.Label(frame, text="Ingresa el nombre de un pueblo de Puerto Rico:")
label_instrucciones.pack()

entry = tk.Entry(frame)
entry.pack(pady=5)

button_verificar = tk.Button(frame, text="Verificar", command=verificar_respuesta)
button_verificar.pack(pady=5)

label_feedback = tk.Label(frame, text="")
label_feedback.pack()

label_tiempo = tk.Label(frame, text=f"Tiempo restante: {tiempo_restante} segundos")
label_tiempo.pack()

# Iniciar el temporizador
actualizar_tiempo()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()