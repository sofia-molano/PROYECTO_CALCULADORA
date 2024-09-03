import MODEL_firebase_python as firebase_python
import MV_entradas
import VIEW_ventana_grafica as ventana_grafica
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk

#VENTANA CALCULADORA
root=Tk()
root.title("Calculadora")
root.geometry("+200+80")
root.resizable(False,False)
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

estilos=ttk.Style()
estilos.theme_use('clam')

mainframe=ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0,sticky=(W,E,N,S))

for i in range(7): 
    mainframe.columnconfigure(i, weight=1) 
for i in range(9): 
    mainframe.rowconfigure(i, weight=1) 
 
# Crear un Frame para el Label y el Botón 
frame = ttk.Frame(root, style="mainframe.TFrame")
frame.grid(column=10, row=0, sticky=(W, E, N, S))

# Configurar columnas y filas del frame
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
#LABEL1
estilos_label1=ttk.Style()

entrada1=StringVar()
Label_entrada1=ttk.Label(mainframe,textvariable=entrada1,style='Label1.TLabel') 
Label_entrada1.grid(column=0, row=0,columnspan=4,sticky=(W,E,N,S))

#LABEL 2
estilos_label2=ttk.Style()

entrada2 = StringVar()
Label_entrada2 = ttk.Label(frame, textvariable=entrada2, style='Label2.TLabel', font="arial 20")
Label_entrada2.grid(column=0, row=0, sticky=(N, S, W, E), padx=25, pady=0)

#ESTILOS
estilos_botones_numeros=ttk.Style()
estilos_botones_borrar=ttk.Style()
estilos_botones_restantes=ttk.Style()
estilos_botones_especiales=ttk.Style()
estilos_botones_trigonometricas=ttk.Style()
estilos_boton_graficar=ttk.Style()

#TEMA CLARO 

def claro():
    estilos.configure('mainframe.TFrame', background="#e8f6f3", font="arial 22")
    estilos_label1.configure('Label1.TLabel', font="arial 25", anchor="e", background="#e8f6f3")
    estilos_label2.configure('Label2.TLabel', font="arial 15", anchor="e", background="#e8f6f3", foreground='#0b5345')

    estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width="5", background="#d0ece7", relief="flat",foreground="#000000")
    estilos_botones_numeros.map('Botones_numeros.TButton', foreground=[('active','#17202a')],background=[("active","#a2d9ce")])

    estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 20", width="5", background="#45b39d", relief="flat",foreground="#000000")
    estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active','#FFFFFF')],background=[("active","#45B39D")])

    estilos_boton_graficar.configure('Boton_graficar.TButton', font="arial 15", width="5", background="#45b39d", relief="flat",foreground="#000000")
    estilos_boton_graficar.map('Boton_graficar.TButton', foreground=[('active','#FFFFFF')],background=[("active","#45B39D")])

    estilos_botones_restantes.configure('Botones_restantes.TButton', font="arial 22", width="5", background="#a2d9ce", relief="flat",foreground="#000000")
    estilos_botones_restantes.map('Botones_restantes.TButton', foreground=[('active','#FFFFFF')],background=[("active","#138d75")])

    estilos_botones_trigonometricas.configure('Botones_trigonometricas.TButton', font="arial 20", width="5", background="#73c6b6", relief="flat",foreground="#000000")
    estilos_botones_trigonometricas.map('Botones_trigonometricas.TButton', foreground=[('active','#2C3E50')],background=[("active","#EAF2F8")])

#TEMA OSCURO

def oscuro():
    estilos.configure('mainframe.TFrame', background="#212f3c", font="arial 22")
    estilos_label1.configure('Label1.TLabel', font="arial 25", anchor="e", background="#d6dbdf")
    estilos_label2.configure('Label2.TLabel', font="arial 15", anchor="e", background="#212f3c", foreground="#d6dbdf")

    estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width="5", background="#34495e", relief="flat",foreground="#FFFFFF")
    estilos_botones_numeros.map('Botones_numeros.TButton', foreground=[('active','#17202a')],background=[("active","#aeb6bf")])

    estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 20", width="5", background="#5d6d7e", relief="flat",foreground="#FFFFFF")
    estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active','#000000')],background=[("active","#566573")])

    estilos_boton_graficar.configure('Boton_graficar.TButton', font="arial 15", width="5", background="#5d6d7e", relief="flat",foreground="#FFFFFF")
    estilos_boton_graficar.map('Boton_graficar.TButton', foreground=[('active','#000000')],background=[("active","#566573")])

    estilos_botones_restantes.configure('Botones_restantes.TButton', font="arial 22", width="5", background="#283747", relief="flat",foreground="#FFFFFF")
    estilos_botones_restantes.map('Botones_restantes.TButton', foreground=[('active','#FFFFFF')],background=[("active","#85929e")])

    estilos_botones_trigonometricas.configure('Botones_trigonometricas.TButton', font="arial 20", width="5", background="#1b2631", relief="flat",foreground="#FFFFFF")
    estilos_botones_trigonometricas.map('Botones_trigonometricas.TButton', foreground=[('active','#2C3E50')],background=[("active","#d6dbdf")])

claro()

# Variable para rastrear el estado del tema
tema_actual = StringVar(value="claro")

# Función para alternar entre temas
def alternar_tema():
    if tema_actual.get() == "claro":
        oscuro()
        tema_actual.set("oscuro")
        boton_tema.config(text="Claro")
    else:
        claro()
        tema_actual.set("claro")
        boton_tema.config(text="Oscuro")

# Botón para alternar entre temas
boton_tema = ttk.Button(mainframe, text="Oscuro", style='Boton_graficar.TButton', command=alternar_tema)
boton_tema.grid(column=6, row=0, sticky=(W, E, N, S))


#BOTÓN BORRAR HISTORIAL
img = Image.open('e:/basura.png')
img = img.resize((35, 30), Image.LANCZOS)  # Redimensionar (Ancho, Alto)
img = ImageTk.PhotoImage(img)

# Crear el botón y agregarlo al grid
botonNuevo1 = ttk.Button(frame, image=img,style='Botones_borrar.TButton', command=lambda: MV_entradas.borrar_historial_pantalla(entrada2))
botonNuevo1.grid(column=0, row=7, sticky=W)
frame.rowconfigure(1, weight=1)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#x,y,z,pi,e
button_pi = ttk.Button(mainframe, text="π", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('π', entrada1))
button_epsilon = ttk.Button(mainframe, text="e", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('e', entrada1))
button_x = ttk.Button(mainframe, text="x", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('x', entrada1))
button_y = ttk.Button(mainframe, text="y", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('y', entrada1))
button_z = ttk.Button(mainframe, text="z", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('z', entrada1))

#potencias, raíces, logaritmo
button_potencia_dos = ttk.Button(mainframe, text="x²", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('x²', entrada1))
button_potencia_y = ttk.Button(mainframe, text="x^y", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('^', entrada1))
button_raiz_cuadrada = ttk.Button(mainframe, text="√", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('√', entrada1))
button_raiz = ttk.Button(mainframe, text="x√n", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('x√n', entrada1))
button_logaritmo = ttk.Button(mainframe, text="log", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('log', entrada1))

#simbolos
button_menor = ttk.Button(mainframe, text="<", style='Botones_restantes.TButton',command=lambda:MV_entradas.ingresar('<',entrada1))
button_mayor = ttk.Button(mainframe, text=">", style='Botones_restantes.TButton',command=lambda:MV_entradas.ingresar('>',entrada1))
button_parentesis1=ttk.Button(mainframe,text="(",style='Botones_restantes.TButton',command=lambda:MV_entradas.ingresar('(',entrada1))
button_parentesis2=ttk.Button(mainframe,text=")",style='Botones_restantes.TButton',command=lambda:MV_entradas.ingresar(')',entrada1))
button_valor_absoluto =ttk.Button(mainframe, text="||", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('||', entrada1))

#extras
button_fraccion = ttk.Button(mainframe, text="x/y", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('x/y', entrada1))
button_factorial = ttk.Button(mainframe, text="!", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('!', entrada1))


#botones de los números
button0= ttk.Button(mainframe,text="0",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('0',entrada1))
button1= ttk.Button(mainframe,text="1",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('1',entrada1))
button2= ttk.Button(mainframe,text="2",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('2',entrada1))
button3= ttk.Button(mainframe,text="3",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('3',entrada1))
button4= ttk.Button(mainframe,text="4",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('4',entrada1))
button5= ttk.Button(mainframe,text="5",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('5',entrada1))
button6= ttk.Button(mainframe,text="6",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('6',entrada1))
button7= ttk.Button(mainframe,text="7",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('7',entrada1))
button8= ttk.Button(mainframe,text="8",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('8',entrada1))
button9= ttk.Button(mainframe,text="9",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('9',entrada1))

#botones de operaciones básicas
button_suma= ttk.Button(mainframe,text="+",style='Botones_restantes.TButton',command=lambda:MV_entradas.ingresar('+',entrada1))
button_resta= ttk.Button(mainframe,text="-",style='Botones_restantes.TButton',command=lambda:MV_entradas.ingresar('-',entrada1))
button_multiplicación= ttk.Button(mainframe,text="*",style='Botones_restantes.TButton',command=lambda:MV_entradas.ingresar('*',entrada1))
button_división= ttk.Button(mainframe,text=chr(247),style='Botones_restantes.TButton',command=lambda:MV_entradas.ingresar('/',entrada1))
button_igual= ttk.Button(mainframe,text="=",style='Botones_restantes.TButton',command=lambda:MV_entradas.ingresar('=' or 'Return',entrada1))

#Funciones trigonométricas
button_seno = ttk.Button(mainframe, text="sin", style='Botones_trigonometricas.TButton', command=lambda:MV_entradas.ingresar('sin',entrada1))
button_coseno = ttk.Button(mainframe, text="cos", style='Botones_trigonometricas.TButton', command=lambda: MV_entradas.ingresar('cos',entrada1))
button_tangente = ttk.Button(mainframe, text="tan", style='Botones_trigonometricas.TButton', command=lambda: MV_entradas.ingresar('tan',entrada1))        

#Funciones trigonométricas INVERSAS
button_arcsin=ttk.Button(mainframe, text="sen^-1", style='Botones_trigonometricas.TButton', command=lambda:MV_entradas.ingresar('selev-1',entrada1))
button_arccos= ttk.Button(mainframe, text="cos^-1", style='Botones_trigonometricas.TButton',command=lambda:MV_entradas.ingresar('conoelev-1',entrada1))
button_arctan= ttk.Button(mainframe, text="tan^-1", style='Botones_trigonometricas.TButton',command=lambda:MV_entradas.ingresar('taelev-1',entrada1))


#botones de borrar, paréntesis y punto
button_borrar = ttk.Button(mainframe, text=chr(9003), style='Botones_borrar.TButton', command=lambda: MV_entradas.borrar(entrada1))
button_borrar_todo = ttk.Button(mainframe, text="C", style='Botones_borrar.TButton', command=lambda: MV_entradas.borrar_todo(entrada1))
button_punto=ttk.Button(mainframe,text=".",style='Botones_numeros.TButton',command=lambda:MV_entradas.ingresar('.',entrada1))
button_fx=ttk.Button(mainframe,text="f(x)",style='Botones_borrar.TButton', command=lambda:MV_entradas.ingresar('f(x)=',entrada1))
button_graficar=ttk.Button(mainframe,text="graficar",style='Boton_graficar.TButton', command=lambda:ventana_grafica.abrir_ventana(entrada1))

#Boton radianes a grados
button_radian_g = ttk.Button (mainframe, text="x°", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('x°', entrada1) )

#Boton grados a radianes
button_grados_r = ttk.Button (mainframe, text="π rad", style='Botones_restantes.TButton', command=lambda: MV_entradas.ingresar('P rad', entrada1) )


#---------------------------------------------------------------------------------------------------------------------------------------------------------
#Colocar botones en pantalla

button_x.grid(column=0,row=2,sticky=(W,E,N,S))
button_y.grid(column=1,row=2,sticky=(W,E,N,S))
button_z.grid(column=2,row=2,sticky=(W,E,N,S))
button_pi.grid(column=3, row=2,sticky=(W,E,N,S))

button_potencia_dos.grid(column=0, row=3,sticky=(W,E,N,S))
button_raiz_cuadrada.grid(column=1, row=3,sticky=(W,E,N,S))
button_raiz.grid(column=2, row=3,sticky=(W,E,N,S))
button_epsilon.grid(column=3, row=3,sticky=(W,E,N,S))

button_menor.grid(column=0, row=4,sticky=(W,E,N,S))
button_mayor.grid(column=1, row=4,sticky=(W,E,N,S))
button_potencia_y.grid(column=2, row=4,sticky=(W,E,N,S))
button_valor_absoluto.grid(column=3, row=4,sticky=(W,E,N,S))

button_parentesis1.grid(column=0,row=5,sticky=(W,E,N,S))
button_parentesis2.grid(column=1,row=5,sticky=(W,E,N,S))
button_logaritmo.grid(column=2, row=5,sticky=(W,E,N,S))
button_fraccion.grid(column=3, row=5,sticky=(W,E,N,S))

button_seno.grid(column=3, row=6,sticky=(W,E,N,S))
button_coseno.grid(column=4, row=6,sticky=(W,E,N,S))
button_tangente.grid(column=5, row=6,sticky=(W,E,N,S))

button7.grid(column=4, row=2,sticky=(W,E,N,S))
button8.grid(column=5, row=2,sticky=(W,E,N,S))
button9.grid(column=6, row=2,sticky=(W,E,N,S))
button_multiplicación.grid(column=7, row=2,sticky=(W,E,N,S))
button_división.grid(column=8, row=2,sticky=(W,E,N,S))

button4.grid(column=4, row=3,sticky=(W,E,N,S))
button5.grid(column=5, row=3,sticky=(W,E,N,S))
button6.grid(column=6, row=3,sticky=(W,E,N,S))
button_suma.grid(column=7, row=3,sticky=(W,E,N,S))
button_resta.grid(column=8, row=3,sticky=(W,E,N,S))

button1.grid(column=4, row=4,sticky=(W,E,N,S))
button2.grid(column=5, row=4,sticky=(W,E,N,S))
button3.grid(column=6, row=4,sticky=(W,E,N,S))
button_igual.grid(column=7, row=4,columnspan=3,sticky=(W,E,N,S))

button0.grid(column=4, row=5,columnspan=2,sticky=(W,E,N,S))
button_punto.grid(column=6, row=5,sticky=(W,E,N,S))
button_borrar.grid(column=7, row=5,sticky=(W,E,N,S))
button_borrar_todo.grid(column=8,row=5,sticky=(W,E,N,S))
button_fx.grid(column=7,row=0,sticky=(W,E,N,S))
button_graficar.grid(column=8,row=0,sticky=(W,E,N,S))

button_arcsin.grid(column=6, row=6,sticky=(W,E,N,S))
button_arccos.grid(column=7, row=6,sticky=(W,E,N,S))
button_arctan.grid(column=8, row=6,sticky=(W,E,N,S))

button_factorial.grid(column=0, row=6,sticky=(W,E,N,S))
#Radianes a grados
button_radian_g.grid (column=1, row=6, sticky = (W,E,N,S))
#grados a radianes
button_grados_r.grid (column=2, row=6, sticky = (W,E,N,S))

entry = Entry(mainframe, textvariable=entrada1, font=("Arial", 25))
entry.grid(column=0, row=0, columnspan=4, sticky=(W, E, N, S))
entry.focus_set()

Label_entrada1.focus()

def manejar_tecla(event):
    tecla = event.keysym
    if tecla == 'Return':  
        MV_entradas.ingresar(tecla, entrada1) 
    elif tecla == 'BackSpace': 
        MV_entradas.borrar(entrada1)  
    elif len(tecla) == 1:  
        return
    else:
        return

root.bind('<KeyPress>', manejar_tecla)

#-----------------------------------------------------------------------------------------

# Asignar la función de mostrar el Listbox al menú

def mostrar_historial():
    nuevo_texto=firebase_python.RealtimeGet()
    MV_entradas.actualizar_historial_pantalla(entrada2, nuevo_texto)
    messagebox.showinfo("Confirmación", "Se ha mostrado el historial de la base de datos")

def borrar_hitorial():
    respuesta = messagebox.askokcancel("Confirmación", "¿Seguro que desea borrar el historial?")
    if respuesta:
        firebase_python.RealtimeDelete()

def salir():
    respuesta = messagebox.askokcancel("Confirmación", "¿Seguro que quiere salir?")
    if respuesta:
        root.quit() 

def acerca_de():
    messagebox.showinfo('Acerca de',"Esta es una calculadora creada por el grupo 8 de la clase de Progamación de Computadores de la Universidad Nacional.")

menu_bar = tk.Menu(root)

# Crear el menú "Historial"
historial_menu = tk.Menu(menu_bar, tearoff=0)
historial_menu.add_command(label="Mostrar historial de base de datos", command=mostrar_historial)
historial_menu.add_command(label="Eliminar todo el historial de base de datos", command=borrar_hitorial)

menu_bar.add_cascade(label="Historial", menu=historial_menu)

# Crear el menú "Ayuda"
ayuda_menu = tk.Menu(menu_bar, tearoff=0)
ayuda_menu.add_command(label="Acerca de", command=acerca_de)
ayuda_menu.add_separator()  # Separador
ayuda_menu.add_command(label="Salir", command=salir)

# Añadir "Ayuda" a la barra de menús
menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

# Configurar la barra de menús en la ventana
root.config(menu=menu_bar)
root.protocol("WM_DELETE_WINDOW", salir)

#---------------------------------------------------------------------------------------------------------------------------

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)
