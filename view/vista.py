import sys
sys.path.insert(1,'E:/PROYECTO_CALCULADORA/modelView')
sys.path.insert(1,'E:/PROYECTO_CALCULADORA/view')
import entradas
import ventana_grafica
from tkinter import *
from tkinter import ttk

#VENTANA CALCULADORA
root=Tk()
root.title("Calculadora")
root.geometry("+300+80")
root.resizable(False,False)
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

estilos=ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#EBF5FB")

mainframe=ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0,sticky=(W,E,N,S))
mainframe.columnconfigure(0,weight=1)
mainframe.columnconfigure(1,weight=1)
mainframe.columnconfigure(2,weight=1)
mainframe.columnconfigure(3,weight=1)
mainframe.columnconfigure(4,weight=1)
mainframe.columnconfigure(5,weight=1)
mainframe.columnconfigure(6,weight=1)
mainframe.columnconfigure(10,weight=1)

mainframe.rowconfigure(0,weight=1)
mainframe.rowconfigure(1,weight=1)
mainframe.rowconfigure(2,weight=1)
mainframe.rowconfigure(3,weight=1)
mainframe.rowconfigure(4,weight=1)
mainframe.rowconfigure(5,weight=1)
mainframe.rowconfigure(6,weight=1)
mainframe.rowconfigure(7,weight=1)
mainframe.rowconfigure(8,weight=1)

#LABEL1
estilos_label1=ttk.Style()
estilos_label1.configure('Label1.TLabel', font="arial 25", anchor="e", background="#EBF5FB")

entrada1=StringVar()
Label_entrada1=ttk.Label(mainframe,textvariable=entrada1,style='Label1.TLabel')
Label_entrada1.grid(column=0, row=0,columnspan=4,sticky=(W,E,N,S))

#LABEL 2
estilos_label2=ttk.Style()
estilos_label2.configure('Label2.TLabel', font="arial 15", anchor="e", background="#EBF5FB")

entrada2 = StringVar()
Label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style='Label2.TLabel')
Label_entrada2.grid(column=10, row=0, rowspan=9, padx=10, pady=10, sticky=(N, S, W, E))

#BOTONES
estilos_botones_numeros=ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width="5", background="#FFFFFF", relief="flat")
estilos_botones_numeros.map('Botones_numeros.TButton', foreground=[('active','#2C3E50')],background=[("active","#D6DBDF")])

estilos_botones_borrar=ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 22", width="5", background="#D6EAF8", relief="flat")
estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active','#FFFFFF')],background=[("active","#2980B9")])

estilos_botones_restantes=ttk.Style()
estilos_botones_restantes.configure('Botones_restantes.TButton', font="arial 22", width="5", background="#AED6F1", relief="flat")
estilos_botones_restantes.map('Botones_restantes.TButton', foreground=[('active','#2C3E50')],background=[("active","#85C1E9")])

estilos_botones_especiales=ttk.Style()
estilos_botones_especiales.configure('Botones_especiales.TButton', font="arial 22", width="5", background="#A9CCE3", relief="flat")
estilos_botones_especiales.map('Botones_especiales.TButton', foreground=[('active','#2C3E50')],background=[("active","#7FB3D5")])

estilos_botones_trigonometricas=ttk.Style()
estilos_botones_trigonometricas.configure('Botones_trigonometricas.TButton', font="arial 22", width="5", background="#85C1E9", relief="flat")
estilos_botones_trigonometricas.map('Botones_trigonometricas.TButton', foreground=[('active','#2C3E50')],background=[("active","#EAF2F8")])

estilos_boton_graficar=ttk.Style()
estilos_boton_graficar.configure('Boton_graficar.TButton', font="arial 18", width="5", background="#D6EAF8", relief="flat")
estilos_boton_graficar.map('Boton_graficar.TButton', foreground=[('active','#FFFFFF')],background=[("active","#2980B9")])

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#x,y,z,pi,e
button_pi = ttk.Button(mainframe, text="π", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('π', entrada1))
button_epsilon = ttk.Button(mainframe, text="e", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('e', entrada1))
button_x = ttk.Button(mainframe, text="x", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('x', entrada1))
button_y = ttk.Button(mainframe, text="y", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('y', entrada1))
button_z = ttk.Button(mainframe, text="z", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('z', entrada1))

#potencias, raíces, logaritmo
button_potencia_dos = ttk.Button(mainframe, text="x²", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('x²', entrada1))
button_potencia_y = ttk.Button(mainframe, text="x^y", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('^', entrada1))
button_raiz_cuadrada = ttk.Button(mainframe, text="√", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('√', entrada1))
button_raiz = ttk.Button(mainframe, text="x√n", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('x√n', entrada1))
button_logaritmo = ttk.Button(mainframe, text="log", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('log', entrada1))

#simbolos
button_menor = ttk.Button(mainframe, text="<", style='Botones_especiales.TButton',command=lambda:entradas.ingresar('<',entrada1))
button_mayor = ttk.Button(mainframe, text=">", style='Botones_especiales.TButton',command=lambda:entradas.ingresar('>',entrada1))
button_parentesis1=ttk.Button(mainframe,text="(",style='Botones_especiales.TButton',command=lambda:entradas.ingresar('(',entrada1))
button_parentesis2=ttk.Button(mainframe,text=")",style='Botones_especiales.TButton',command=lambda:entradas.ingresar(')',entrada1))
button_valor_absoluto =ttk.Button(mainframe, text="||", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('||', entrada1))

#extras
button_fraccion = ttk.Button(mainframe, text="x/y", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('x/y', entrada1))
button_factorial = ttk.Button(mainframe, text="!", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('!', entrada1))
button_maso = ttk.Button(mainframe, text="±", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('±', entrada1))
button_integral = ttk.Button(mainframe, text="∫", style='Botones_especiales.TButton', command=lambda: entradas.ingresar('∫', entrada1))


#botones de los números
button0= ttk.Button(mainframe,text="0",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('0',entrada1))
button1= ttk.Button(mainframe,text="1",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('1',entrada1))
button2= ttk.Button(mainframe,text="2",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('2',entrada1))
button3= ttk.Button(mainframe,text="3",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('3',entrada1))
button4= ttk.Button(mainframe,text="4",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('4',entrada1))
button5= ttk.Button(mainframe,text="5",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('5',entrada1))
button6= ttk.Button(mainframe,text="6",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('6',entrada1))
button7= ttk.Button(mainframe,text="7",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('7',entrada1))
button8= ttk.Button(mainframe,text="8",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('8',entrada1))
button9= ttk.Button(mainframe,text="9",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('9',entrada1))

#botones de operaciones básicas
button_suma= ttk.Button(mainframe,text="+",style='Botones_restantes.TButton',command=lambda:entradas.ingresar('+',entrada1))
button_resta= ttk.Button(mainframe,text="-",style='Botones_restantes.TButton',command=lambda:entradas.ingresar('-',entrada1))
button_multiplicación= ttk.Button(mainframe,text="x",style='Botones_restantes.TButton',command=lambda:entradas.ingresar('*',entrada1))
button_división= ttk.Button(mainframe,text=chr(247),style='Botones_restantes.TButton',command=lambda:entradas.ingresar('/',entrada1))
button_igual= ttk.Button(mainframe,text="=",style='Botones_restantes.TButton',command=lambda:entradas.ingresar('=',entrada1))

#Funciones trigonométricas
button_seno = ttk.Button(mainframe, text="sin", style='Botones_trigonometricas.TButton', command=lambda:entradas.ingresar('sin',entrada1))
button_coseno = ttk.Button(mainframe, text="cos", style='Botones_trigonometricas.TButton', command=lambda: entradas.ingresar('cos',entrada1))
button_tangente = ttk.Button(mainframe, text="tan", style='Botones_trigonometricas.TButton', command=lambda: entradas.ingresar('tan',entrada1))        

#Funciones trigonométricas INVERSAS
button_arcsin=ttk.Button(mainframe, text="sin^-1", style='Botones_trigonometricas.TButton', command=lambda:entradas.ingresar('sin^-1',entrada1))
button_arccos= ttk.Button(mainframe, text="cos^-1", style='Botones_trigonometricas.TButton',command=lambda:entradas.ingresar('cos^-1',entrada1))
button_arctan= ttk.Button(mainframe, text="tan^-1", style='Botones_trigonometricas.TButton',command=lambda:entradas.ingresar('tan^-1',entrada1))

#botones de borrar, paréntesis y punto
button_borrar = ttk.Button(mainframe, text=chr(9003), style='Botones_borrar.TButton', command=lambda: entradas.borrar(entrada1))
button_borrar_todo = ttk.Button(mainframe, text="C", style='Botones_borrar.TButton', command=lambda: entradas.borrar_todo(entrada1))
button_punto=ttk.Button(mainframe,text=".",style='Botones_numeros.TButton',command=lambda:entradas.ingresar('.',entrada1))
button_fx=ttk.Button(mainframe,text="f(x)",style='Boton_graficar.TButton', command=lambda:entradas.ingresar('f(x)',entrada1))
button_graficar=ttk.Button(mainframe,text="graficar",style='Boton_graficar.TButton', command=lambda:ventana_grafica.abrir_ventana())
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

button0.grid(column=4, row=5,columnspan=3,sticky=(W,E,N,S))
button_punto.grid(column=6, row=5,sticky=(W,E,N,S))
button_borrar.grid(column=7, row=5,sticky=(W,E,N,S))
button_borrar_todo.grid(column=8,row=5,sticky=(W,E,N,S))
button_fx.grid(column=7,row=0,sticky=(W,E,N,S))
button_graficar.grid(column=8,row=0,sticky=(W,E,N,S))

button_arcsin.grid(column=6, row=6,sticky=(W,E,N,S))
button_arccos.grid(column=7, row=6,sticky=(W,E,N,S))
button_arctan.grid(column=8, row=6,sticky=(W,E,N,S))

button_factorial.grid(column=0, row=6,sticky=(W,E,N,S))
button_maso.grid(column=1, row=6,sticky=(W,E,N,S))
button_integral.grid(column=2, row=6,sticky=(W,E,N,S))
#---------------------------------------------------------------------------------------------------------------------------

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

