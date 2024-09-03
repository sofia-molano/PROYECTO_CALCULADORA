import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import math
from tkinter import messagebox, simpledialog, colorchooser

import MV_v_grafica_funcionamiento as v_grafica_funcionamiento
import MODEL_firebase_python as firebase_python

def abrir_ventana(entrada1):
    # Obtener la expresión de la entrada
    expresion = entrada1.get()
    expresion = expresion.replace('^', '**')
    expresion = expresion.replace('f(x)=', '')

    funciones_permitidas = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'selev-1': math.asin,
        'conoelev-1': math.acos,
        'taelev-1': math.atan,
        'log': math.log,
        'sqrt': math.sqrt,
        'pi': math.pi,
        'e': math.e
    }
    expresion = v_grafica_funcionamiento.insertar_multiplicacion(expresion)

    rangos = simpledialog.askstring(
        "Rango de Ejes", 
        "Ingrese el rango para los ejes x en el formato 'x_min, x_max':",
        initialvalue="-20, 20"
    )

    if rangos:
        try:
            x_min, x_max = map(float, rangos.split(','))
        except ValueError:
            messagebox.showerror("Error", "El formato ingresado es incorrecto. Por favor ingrese valores válidos.")
            return
    else:
        return  

    # Generar valores de x y y
    x_vals = np.linspace(x_min, x_max, 2000)
    y_vals = []

    for x in x_vals:
        y = v_grafica_funcionamiento.evaluar_funcion(x, expresion, funciones_permitidas)
        if y is None:
            return  
        y_vals.append(y)
    # Crear la figura y el eje
    fig, ax = plt.subplots()

    # Graficar los datos
    linea, = ax.plot(x_vals, y_vals, color='blue', label=str(expresion))
    ax.set_xlabel('Eje x')
    ax.set_ylabel('Eje f(x)')
    ax.set_title('Gráfica de ' + str(expresion))
    ax.grid(True)
    ax.legend()
    ax.set_ylim(-5, 5)  
    ax.axhline(0, color='blue', linestyle='--')  
    ax.axvline(0, color='blue', linestyle='--')  

    # Función para cambiar el color de la gráfica
    def cambiar_color(event):
        nuevo_color = colorchooser.askcolor(title="Seleccione el Nuevo Color de la Línea")[1]
        if nuevo_color:
            linea.set_color(nuevo_color)
            fig.canvas.draw()

    ax_color = plt.axes([0.8, 0.01, 0.1, 0.05])  # Posición del botón en la figura
    boton_color = Button(ax_color, 'Color')
    boton_color.on_clicked(cambiar_color)
    
    mostrar_3d = messagebox.askyesno('Graficar 3D', '¿Desea mostrar la gráfica en 3D?')

    if mostrar_3d:  # Esto es lo mismo que decir `if mostrar_3d == True:`
        v_grafica_funcionamiento.grafica_3D(expresion, x_min, x_max, color='blue',resolution=100)

    # Mostrar la gráfica
    plt.show()
    
    # Guardar la información de la función en Firebase
    x_val_fb = np.linspace(-15, 15, 25)
    y_val_fb = []

    for x in x_val_fb:
        y = v_grafica_funcionamiento.evaluar_funcion(x, expresion, funciones_permitidas)
        if y is None:
            return  # Si hay un error, salir de la función
        y_val_fb.append(y)

    firebase_python.RealtimeSetGraficas(expresion, x_val_fb, y_val_fb)
    print("x_vals shape:", x_vals.shape)
    print("y_vals shape:", np.array(y_vals).shape)
