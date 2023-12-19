
from input_utils import read_int, read_float, read_bool

precios =[29.99, 44.32, 64.48]

print(''' 
Elige una opción:

1- ver todo los precios
2- ver un precio por posicion 
3- crear un nvo precio
4- Actualizar un precio existente
5- borrar un precio existente
6- borrar todos lo precios 
7- salir 

        ''')
while True:

   
    opcion = read_int('introduce la opcion (1 a 7): ')
    if opcion == 1:
        
        print('ha elegido ver todos los precios')
        print(precios)
    elif opcion == 2:
        print('ha elegido ver un precio')
        posicion = read_int( 'introduce la posicion del precio que desea consultar:  ')
        if 1 <= posicion <= len(precios):
            print(precios[posicion-1]) # -1 para adaptar al rango de 0 a len(precios)
        else: 
            print('posicion incorrecta')
    elif opcion == 3:
        print('ha elegido introducir un nvo precio')  
        nuevo_precio = read_float('introduce nuevo precio')   
        precios.append(nuevo_precio)          
    elif opcion == 4: 
        print('ha elegido actualizar un precio existente')  
        print ( precios)
        posicion = read_int( 'introduce la posicion del precio que desea consultar:  ')
        if 1 <= posicion <= len(precios):
            precio_modificado = read_float('introduce precio modificado: ')
            precios[posicion] = precio_modificado
        elif opcion == 5:
            print('ha elegido borrar un precio existente')
            posicion = read_int('introduce la posicion del precio que desea borrar: ')
            if 1 <= posicion  <= len(precios):
                precio_borrado = precios.pop(posicion -1) #saca el elemento por posicion
                print(f'precio borrado: {precio_borrado}')
            else:
                print('posición incorrecta')
        
                     