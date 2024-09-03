import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox, Button, colorchooser
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button
from tkinter import colorchooser

def insertar_multiplicacion(expresion):
    nueva_expresion = ""
    longitud = len(expresion)
    funciones = {"sin", "cos", "tan", "log", "sqrt", "selev-1", "conoelev-1", "taelev-1"}
    i = 0
    while i < longitud:
        for funcion in funciones:
            if expresion[i:i+len(funcion)] == funcion:
                nueva_expresion += funcion
                i += len(funcion)
                if i < longitud and expresion[i] == '(':
                    nueva_expresion += expresion[i]
                    i += 1
                break
        else:
            if i > 0 and (
                (expresion[i].isdigit() and (expresion[i-1].isalpha() or expresion[i-1] == ')')) or
                (expresion[i].isalpha() and (expresion[i-1].isdigit() or expresion[i-1] == ')')) or
                (expresion[i] == '(' and (expresion[i-1].isdigit() or expresion[i-1].isalpha()))
            ):
                nueva_expresion += '*'
            nueva_expresion += expresion[i]
            i += 1

    return nueva_expresion

def evaluar_funcion(x, expresion, funciones_permitidas):
    try:
        resultado = eval(expresion, {"__builtins__": None}, {**funciones_permitidas, 'x': x, 'y': x, 'z': x})
        return resultado
    except SyntaxError:
        messagebox.showerror("Error de Sintaxis", "Usted ingresó una operación que no se puede resolver, falta o sobra un caracter. Por favor, revise la expresión y vuelva a intentarlo.")
    except ZeroDivisionError:
        messagebox.showerror("Error Matemático", "No se puede dividir por cero. Por favor, corrija la operación.")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error inesperado: {str(e)}. Vuelva a ingresar la operación correctamente.")

def cambiar_color(event, ax, x_vals, y_vals, z_vals, fig):
    nuevo_color = colorchooser.askcolor(title="Seleccione el Nuevo Color de la Línea")[1]
    if nuevo_color:
        ax.clear()  # Limpiar el eje actual
        ax.plot_surface(x_vals, y_vals, z_vals, color=nuevo_color)
        ax.set_xlabel('Eje x')
        ax.set_ylabel('Eje y')
        ax.set_zlabel('Eje z')
        ax.set_title('Gráfica 3D')
        ax.set_zlim(-5, 5)
        fig.canvas.draw_idle()


def grafica_3D(expresion, x_min, x_max, color,resolution=200):
    x_vals = np.linspace(x_min, x_max, resolution)
    y_vals = np.linspace(x_min, x_max, resolution)
    x_vals, y_vals = np.meshgrid(x_vals, y_vals)

    # Evaluar la función para z, manejando las discontinuidades
    z_vals = np.array([
        evaluar_funcion(x, expresion, funciones_permitidas={'sin': np.sin, 'cos': np.cos, 'tan': np.tan, 'log': np.log, 'sqrt': np.sqrt, 'pi': np.pi, 'e': np.e})
        for x, y in zip(np.ravel(x_vals), np.ravel(y_vals))
    ]).reshape(x_vals.shape)

    z_vals = np.where(np.abs(z_vals) > 5, np.nan, z_vals)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x_vals, y_vals, z_vals, color=color)
    ax.set_xlabel('Eje x')
    ax.set_ylabel('Eje y')
    ax.set_zlabel('Eje z')
    ax.set_title('Gráfica 3D de ' + str(expresion))
    ax.set_zlim(-5, 5)

    # Crear un botón para cambiar el color usando matplotlib.widgets.Button
    ax_color = plt.axes([0.8, 0.01, 0.1, 0.05])
    boton_color = Button(ax_color, 'Color')
    boton_color.on_clicked(lambda event: cambiar_color(event, ax, x_vals, y_vals, z_vals, fig))

    plt.show()


