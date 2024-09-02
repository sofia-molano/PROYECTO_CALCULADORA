import VIEW_vista as vista
import MODEL_firebase_python as firebase_python
import math
from tkinter import messagebox
import MV_v_grafica_funcionamiento as vgf


def actualizar_historial_pantalla(entrada2, nuevo_texto):
    global historial_pantalla
    if isinstance(nuevo_texto, list):
        nuevo_texto = "\n".join(nuevo_texto)  # Convertir la lista en una cadena con saltos de línea
    historial_pantalla += nuevo_texto + "\n"  # Agregar nuevo texto al historial local
    entrada2.set(historial_pantalla)

def ingresar(tecla, entrada1):
    # Obtiene el texto actual del Entry
    current_text = entrada1.get()

    # Lista de operaciones
    op1 = ['+', '-', '*', '/', '^', '(', ')', '.', '!','<','>']
    op2 = ['sin', 'cos', 'tan', 'selev-1', 'conoelev-1', 'taelev-1', 'log']
    op3 = ['√', 'x²', 'x√n', '||', 'x/y', '±', 'f(x)=', 'x°', 'P rad']

    if tecla.isdigit() or tecla in 'xyzπe' or tecla in op1:
        entrada1.set(current_text + tecla)
    elif tecla in op2:
        entrada1.set(tecla + '(' + current_text + ')')
    elif tecla in op3:
        if tecla == '√':
            entrada1.set(tecla + current_text)
        elif tecla == 'x√n':
            entrada1.set(current_text + '√')
        elif tecla == 'x²':
            entrada1.set('(' + current_text + ')^2')
        elif tecla == '||':
            entrada1.set('abs(' + current_text + ')')
        elif tecla == '±':
            entrada1.set(tecla + current_text)
        elif tecla == 'f(x)=':
            entrada1.set(tecla + current_text)
        #-------------------------------
        #Radianes a grados
        elif tecla == 'x°':
            entrada1.set('math.degrees(' + entrada1.get() + ')')
        #Grados a radianes
        elif tecla == 'P rad':
            entrada1.set('math.radians(' + entrada1.get() + ')')

    elif tecla == '=' or tecla=='Return':
        expresion = current_text
        expresion = expresion.replace('^', '**')
        expresion = expresion.replace('π', 'math.pi')
        expresion = expresion.replace('sin', 'math.sin')
        expresion = expresion.replace('cos', 'math.cos')
        expresion = expresion.replace('tan', 'math.tan')
        
        expresion = expresion.replace('selev-1', 'math.asin')
        expresion = expresion.replace('conoelev-1', 'math.acos')
        expresion = expresion.replace('taelev-1', "math.atan")



        expresion = expresion.replace('log', 'math.log')
        expresion = expresion.replace('!', 'math.factorial')
        expresion = expresion.replace('√', 'math.sqrt')

        nueva_expresion = vgf.insertar_multiplicacion(expresion)
        
        try:
            resultado = eval(nueva_expresion)
            entrada1.set(str(resultado))
            firebase_python.RealtimeSet(expresion, str(resultado))
            

            nuevo_texto = f"{nueva_expresion} = {resultado}"
            actualizar_historial_pantalla(vista.entrada2, nuevo_texto)
        except SyntaxError:
            entrada1.set("Error")
            messagebox.showerror("Error de Sintaxis", "Usted ingresó una operación o un carácter que no se puede resolver. Por favor, revise la expresión y vuelva a intentarlo.")
        except ZeroDivisionError:
            entrada1.set("Error")
            messagebox.showerror("Error Matemático", "No se puede dividir por cero. Por favor, corrija la operación.")
        except Exception as e:
            entrada1.set("Error")
            messagebox.showerror("Error", f"Se produjo un error inesperado: {str(e)}. Vuelva a ingresar la operación correctamente.")


    else:
        firebase_python.RealtimeSet(current_text, '')
        firebase_python.RealtimeUpdate(current_text, '', vista.entrada2)


def borrar(entrada1):
    i=0
    f=len(entrada1.get())
    entrada1.set(entrada1.get()[i:f-1])

def borrar_todo(entrada1):
    entrada1.set("")

historial_pantalla = ""

def borrar_historial_pantalla(entrada2):
    global historial_pantalla
    entrada2.set("")  # Limpiar la pantalla
    historial_pantalla = ""  # Reiniciar el historial local

