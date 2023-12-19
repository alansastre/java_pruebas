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
    # booleano = respuesta.lower() in ['si', 'yes', 'sí', 'oui', 'ja'] # devuelve el valor leído por consola
    # return booleano # True o False
    while True:

        resultado = input(prompt).lower()
        if resultado == 'si':
            return True
        elif resultado == 'no':
            return False
        else:
            print('Valor incorrecto')
            # no te saca del bucle, repite otra iteración hasta que escriba si o no
    

              
# edad = read_int('Introduce tu edad: ')
# peso = read_int('Introduce tu peso: ')
# altura = read_int('Introduce tu altura: ')
# salario = read_float('Introduce salario: ')
# activo = read_bool('Introduce si es trabajador por cuenta ajena (si/no): ')
# print(f'activo {activo}')
