import sys
sys.path.insert(1,'E:/PROYECTO_CALCULADORA/model')
sys.path.insert(1,'E:/PROGRAMACION/PROYECTO_CALCULADORA/view')
import firebase_python
import vista
import math

def ingresar(tecla, entrada1):

    op1 = ['+', '-', '*', '/', '^', '(', ')', '.', '!']
    op2 = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log']
    op3 = ['√', 'x²', 'x√n', '||', 'x/y', '±', 'f(x)']
    
    if tecla.isdigit() or tecla in 'xyzπe' or tecla in op1:
        entrada1.set(entrada1.get() + tecla)
    elif tecla in op2:
        entrada1.set(tecla + '(' + entrada1.get() + ')')
    elif tecla in op3:
        if tecla == '√':
            entrada1.set(tecla + entrada1.get())
        elif tecla == 'x√n':
            entrada1.set(entrada1.get() + '√')
        elif tecla == 'x²':
            entrada1.set('(' + entrada1.get() + ')^2')
        elif tecla == '||':
            entrada1.set('abs(' + entrada1.get() + ')')
        elif tecla == '±':
            entrada1.set(tecla + entrada1.get())
    elif tecla == '=':
        expresion = entrada1.get()
        expresion = expresion.replace('^', '**')
        expresion = expresion.replace('π', 'math.pi')
        expresion = expresion.replace('sin', 'math.sin')
        expresion = expresion.replace('cos', 'math.cos')
        expresion = expresion.replace('tan', 'math.tan')
        expresion = expresion.replace('asin', 'math.asin')
        expresion = expresion.replace('acos', 'math.acos')
        expresion = expresion.replace('atan', 'math.atan')
        expresion = expresion.replace('log', 'math.log')
        expresion = expresion.replace('!', 'math.factorial')
        expresion = expresion.replace('√', 'math.sqrt')
        
        try:
            resultado = eval(expresion)
            entrada1.set(str(resultado))
            firebase_python.RealtimeSet(expresion, str(resultado))
            firebase_python.RealtimeUpdate(expresion, str(resultado), vista.entrada2)
        except Exception as e:
            entrada1.set("Error")
            firebase_python.RealtimeSet(expresion, "Error")
            firebase_python.RealtimeUpdate(expresion, "Error", vista.entrada2)
    else:
        firebase_python.RealtimeSet(entrada1.get(), '')
        firebase_python.RealtimeUpdate(entrada1.get(), '', vista.entrada2)

def borrar(entrada1):
    i=0
    f=len(entrada1.get())
    entrada1.set(entrada1.get()[i:f-1])

def borrar_todo(entrada1):
    entrada1.set("")