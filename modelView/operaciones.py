import math

def suma(entrada1, numero):
    return float(entrada1 + numero)

def resta(entrada1,numero):
    return float (entrada1 - numero)

def multiplicar(entrada1,numero):
    return float(entrada1 * numero)

def dividir(entrada1,numero):
    return float(entrada1 / numero)

def potencia_dos(numero):
    return float(numero) ** 2

def potencia_x(entrada1, numero):
    return float(entrada1**numero)

def raiz_cuadrada(numero):
    return math.sqrt(float(numero))

def raiz(entrada1,indice_raiz):
    numero = float(entrada1.get())
    resultado = numero ** (1 / indice_raiz)
    entrada1.set(f"{numero}√{indice_raiz}")
    entrada1.set(str(resultado))

def logaritmo(numero):
    return math.log10(float(numero))

def pi():                   
    return math.pi

def epsilon():
    return math.e

def valor_absoluto(numero):
    if numero < 0:
        numero = float(numero)
        return (numero*(-1))
    else:
        numero = float(numero)
        return numero

def factorial(numero):
    return math.factorial(int(numero))

def seno(numero):
    return math.sin(math.radians(float(numero)))

def coseno(numero):
    return math.cos(math.radians(float(numero)))

def tangente(numero):
    return math.tan(math.radians(float(numero)))

def arcsin(numero):
    return math.degrees(math.asin(float(numero)))

def arccos(numero):
    return math.degrees(math.acos(float(numero)))

def arctan(numero):
    return math.degrees(math.atan(float(numero)))

