"""
Archivo con funciones de utilidad para leer datos por consola
utilizando input, while, try except
"""

def read_int(prompt):
    while True:
        try:
            numero = int(input(prompt)) # devuelve el valor leído por consola
            return numero
        except Exception:
            print('No se ha podido leer el número int')
        
        
def read_float(prompt):
    while True:
        try:
            numero = float(input(prompt)) # devuelve el valor leído por consola
            return numero
        except Exception:
            print('No se ha podido leer el número float')
          
          
def read_bool(prompt):
    # respuesta = input(prompt)
    # boolleano = respuesta : lower() ['si', 'yes', 'sí', 'oui', 'ja']
    # devuelve booleano
    
    respuesta = input(prompt)
    booleano = respuesta.lower() in ['si', 'yes', 'sí', 'oui', 'ja'] # devuelve el valor leído por consola
    return booleano # True o False

