import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate("E:/PROYECTO_CALCULADORA/model/clave_firebase.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://calculadora-grafica-468ee-default-rtdb.firebaseio.com/'
})

def RealtimeSet(entrada1,resultado):
    # Funciones CRUD: ESCRIBIR
    ref = db.reference('historial')
    nueva_entrada = ref.push()  
    nueva_entrada.set({
        'expresion': entrada1,
        'resultado': resultado
    })
    print("Datos ingresados correctamente en el historial")

def RealtimeGet():
    # Funciones CRUD: LEER
    ref = db.reference('historial')
    historial = ref.get()
    historial_texto = ""
    if historial:
        for key, x in historial.items():
            historial_texto += f"{x['expresion']} = {x['resultado']}\n"
    return historial_texto

def RealtimeUpdate(expresion, resultado, entrada2):
    # Funciones CRUD: ACTUALIZAR
    historial_texto = RealtimeGet()
    nuevo_historial = f"{expresion} = {resultado}\n"
    historial_lineas = historial_texto.split('\n')
    historial_lineas.insert(0, nuevo_historial.strip())  
    if len(historial_lineas) > 10:
        historial_lineas = historial_lineas[:10]
    
    historial_texto = "\n".join(historial_lineas) 
    entrada2.set(historial_texto)
    ref = db.reference('historial')
    ref.set({str(i): {'expresion': linea.split(' = ')[0], 'resultado': linea.split(' = ')[1]} for i, linea in enumerate(historial_lineas) if linea})
    print("Historial actualizado correctamente")

def RealtimeDelete():
    # Funciones CRUD: BORRAR
    ref = db.reference('historial')
    ref.child('5').delete()
    print("Datos eliminados correctamente")
