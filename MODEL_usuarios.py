import firebase_admin 
from firebase_admin import credentials, auth
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import MODEL_firebase_python as firebase_python

# Inicializar Firebase
cred = credentials.Certificate("clave.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://calculadora-grafica-468ee-default-rtdb.firebaseio.com/'
})

def iniciar_sesion(email, contraseña):
    try:
        user = auth.get_user_by_email(email)
        if user:
            messagebox.showinfo("Éxito", "Sesión iniciada correctamente.")
            ventana_sesion.destroy()
            uid = user.uid
            import VIEW_vista
            firebase_python.configurar_usuario(uid, email)
        else:
            messagebox.showerror("Error", "Usuario no encontrado.")
    except firebase_admin.auth.UserNotFoundError:
        messagebox.showerror("Error", "Usuario no encontrado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

def registrar_usuario(email, contraseña):
    if not email.strip() or not contraseña.strip():
        messagebox.showerror("Error", "Debe ingresar un correo electrónico y una contraseña.")
        return

    try:
        user = auth.create_user(email=email, password=contraseña)
        messagebox.showinfo("Éxito", f"Usuario registrado correctamente con UID: {user.uid}")
    except firebase_admin.auth.EmailAlreadyExistsError:
        messagebox.showerror("Error", "El correo electrónico ya está registrado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al registrar el usuario: {str(e)}")
        
# Interfaz Tkinter
ventana_sesion = tk.Tk()
ventana_sesion.title("Iniciar Sesión")
ventana_sesion.geometry("300x250")

tk.Label(ventana_sesion, text="Correo:").pack(pady=10)
email_entry = tk.Entry(ventana_sesion)
email_entry.pack(pady=5)

tk.Label(ventana_sesion, text="Contraseña:").pack(pady=10)
contraseña_entry = tk.Entry(ventana_sesion, show="*")
contraseña_entry.pack(pady=5)

tk.Button(ventana_sesion, text="Iniciar Sesión", command=lambda: iniciar_sesion(email_entry.get(), contraseña_entry.get())).pack(pady=10)
tk.Button(ventana_sesion, text="Registrar", command=lambda: registrar_usuario(email_entry.get(), contraseña_entry.get())).pack(pady=10)


ventana_sesion.mainloop()