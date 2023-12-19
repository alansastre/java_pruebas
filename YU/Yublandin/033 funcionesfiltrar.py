# lista de precios
#filtrar precios por rango

"""CREAR UNA FUNCION QUE RECIBE UNA LISTA DE PRECIOS, UN PRECIO MIN, UN PRECIO MAX
LA FUNCION DEBE COMPROBAR UNO A UNO LOS PRECIOS Y COMPROBAR SI ESTAN 
COMPRENDIDOS ENTRE PRECIO MIN Y PRECIO MAX, SI LO ESTAN ENTINCES SE GUARDAN 
EN UNA LISTA DE RESULTADOS Y FINALMENTE SE DEVUELVE LA LISTA DE RESULTADOS 

"""
def filtrar_precios(precios, precio_min, precio_max):
    resultados = [] #lista par almacenar los resultados, precios filtrados
    for precio in precios:
        if precio_min <= precio <= precio_max:
           resultados.append(precio) # con el resultado appen guarda el precio en resultado
    return resultados        
            

precios = [20.99, 42.33, 55.50, 90.77, 36.77, 47.89]
# paramentro: lista precios, precio minimo, precio maximo
# precio_filtrados es una lista de resultados, de precios filtrados

precios_filtrados = filtrar_precios(precios, 30, 50)
