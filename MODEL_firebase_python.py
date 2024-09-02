from firebase_admin import db
import numpy as np
import tkinter as tk
from tkinter import messagebox
import re

user_uid = None
correo = None

def sanitize_path(path):
    return re.sub(r'[\/\#\$\[\]\.@]', '_', path)

def configurar_usuario(uid, email):
    global user_uid
    global correo
    user_uid = uid
    correo = email
    sanitized_email = sanitize_path(correo)

    # Obtener la referencia al nodo específico del usuario
    ref = db.reference(f'usuarios/{sanitized_email}')


def RealtimeSet(entrada1, resultado):
    if not user_uid or not correo:
        raise ValueError("Debe iniciar sesión primero.")
    
    sanitized_email = sanitize_path(correo)
    ref = db.reference(f'usuarios/{sanitized_email}')
    nueva_entrada = ref.push()
    nueva_entrada.set({
        'expresion': entrada1,
        'resultado': resultado
    })

def RealtimeGet():
    if not user_uid:
        raise ValueError("Debe iniciar sesión primero.")
    
    sanitized_email = sanitize_path(correo)
    ref = db.reference(f'usuarios/{sanitized_email}')
    historial = ref.get()
    historial_lista = []

    if historial:
        for key, x in reversed(list(historial.items())):
            if isinstance(x, dict):
                expresion = x.get('expresion', 'Desconocida')
                resultado = x.get('resultado', 'Datos de gráfica')
            else:
                expresion = x
                resultado = 'Los datos de la gráfica no se muestran en pantalla'
            historial_lista.append(f"{expresion} = {resultado}")

    return historial_lista

def RealtimeDelete():
    try:
        sanitized_email = sanitize_path(correo)
        ref = db.reference(f'usuarios/{sanitized_email}')
        ref.delete()
        messagebox.showinfo("Información","Los datos del historial han sido eliminados correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")
#--------------------------------------------------------------------------------------------------------------------------------
def RealtimeGet_Claves():
    # Funciones CRUD: LEER
    sanitized_email = sanitize_path(correo)
    ref = db.reference(f'usuarios/{sanitized_email}')
    historial = ref.get()
    historial_lista = []  # Crear una lista para almacenar las operaciones y resultados con sus claves

    if historial:
        for key, x in reversed(list(historial.items())):  # Invertir el orden de los elementos
            if isinstance(x, dict):  # Verifica si x es un diccionario
                expresion = x.get('expresion', 'Desconocida')
                resultado = x.get('resultado', 'Datos de grafica')
            else:  # Si x no es un diccionario, es una cadena de texto
                expresion = x
                resultado = 'Los datos de la gráfica no se muestran en pantalla'
            valor = f"{expresion} = {resultado}"  # Agregar la operación como una sola cadena
            historial_lista.append((key, valor))  # Agregar la clave y el valor como una tupla a la lista

    return historial_lista  # Devolver la lista de tuplas (clave, valor)


def RealtimeDelete_elemento(listbox, item_claves):
    seleccion = listbox.curselection()  # Obtener el índice del elemento seleccionado
    if seleccion:
        index = seleccion[0]
        item_value = listbox.get(index)  # Obtener el valor del elemento seleccionado
        item_key = item_claves.get(item_value)  # Obtener la clave asociada en Firebase
        
        if item_key:
            respuesta = messagebox.askyesno("Confirmación", f"¿Seguro que desea borrar el elemento '{item_value}'?")
            
            if respuesta:
                try:
                    sanitized_email = sanitize_path(correo)
                    ref = db.reference(f'usuarios/{sanitized_email}')
                    ref.child(item_key).delete()  # Elimina solo el elemento con la clave especificada
                    listbox.delete(index)  # Eliminar del Listbox
                    messagebox.showinfo("Confirmación", "El elemento ha sido borrado.")
                except Exception as e:
                    messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")
        else:
            messagebox.showerror("Error", "No se encontró la clave para el elemento seleccionado.")




def RealtimeSetGraficas(expresion, x_val_fb, y_val_fb):
    if not user_uid or not correo:
        raise ValueError("Debe iniciar sesión primero.")
    
    # Sanitiza el correo electrónico antes de usarlo en el path
    sanitized_email = sanitize_path(correo)
    
    # Usa el UID y el correo electrónico sanitizado para crear una clave única en Firebase
    ref = db.reference(f'usuarios/{sanitized_email}')
    nueva_entrada = ref.push()  # Crea una nueva entrada con una clave única

    # Convertir x_val_fb y y_val_fb a listas si son arrays de NumPy
    x_val_list = x_val_fb.tolist() if isinstance(x_val_fb, np.ndarray) else x_val_fb
    y_val_list = y_val_fb.tolist() if isinstance(y_val_fb, np.ndarray) else y_val_fb
    
    # Crear una lista de pares x:y como cadenas
    datos_graficas = [f" {x} : {y} " for x, y in zip(x_val_list, y_val_list)]
    
    nueva_entrada.set({
        'expresion': expresion,
        'valores x : f(x)': datos_graficas
    })
    
    print("Datos ingresados correctamente en el historial")
