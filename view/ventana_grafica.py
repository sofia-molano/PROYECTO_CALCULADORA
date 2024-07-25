import numpy as np
import sympy as sp
import matplotlib as plt
from matplotlib import pyplot
import vista

def abrir_ventana():
    expresion = vista.entrada1.get()
    x = sp.Symbol('x')

    try:
        funcion = sp.sympify(expresion.replace('^', '**'))
        f_lambdified = sp.lambdify(x, funcion, modules=['numpy'])
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lambdified(x_vals)
        plt.plot(x_vals, y_vals)
        plt.xlabel('x')
        plt.ylabel(str(expresion))
        plt.title('Gráfica de ' + str(expresion))
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error al graficar la función: {e}")
