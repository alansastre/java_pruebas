
print(type('hola')) #str
print(type(40))  #int
print(type(99.99))  #float
print(type(True)) #bool
print(type(False))#bool

texto = "hola curso de java"
#len() calcular la longitud de un texto y de una estructura
print(len(texto))

#upper() convierte a mayusculas

print(texto.upper()) #el numbre de la variable, punto + nombre del texto

#lower() convierte a minuscula 

print(texto.lower())

#capitalize() convierte solo la primera letra de todo a mayuscula

print(texto.capitalize())


#split() divide el texto en funcion de un seperador, devuelve una lista

palabras = texto.split() # si no ponemos nada dentro del splity, entonces separa por espacios
print(palabras) # ['hola, 'curso, 'java]
print(palabras[0]) # hola
print(palabras[1]) # curso
print(palabras[2]) # java
# print(palabras[3]) # index Error list index out of range

print(palabras[0].capitalize())
print(palabras[0].capitalize())
print(palabras[0].capitalize())

texto_capitalized= palabras[0].capitalize() +" "+ palabras[1].capitalize() +" "


#format {} {}  con dos huecos
mensaje = "hola curso{} la nota minima es de {} puntos."
print(mensaje.format("java", 5)) 
print(mensaje.format("python", 5)) 
print(mensaje.format("spring", 7)) 

#format {} {} {}con tres huecos
pantilla ="{} {} {}" #
texto_capitalized = plantilla.format(
palabras[0].capitalize(),    #string con 3 huecos separados por espacios
palabras[1].capitalize(), 
palabras[2].capitalize()  
)
print(texto_capitalized)

# f strings: cadena con formato , permite incrustar expresiones dentro de cadenas literales

producto = "laptop Asus"
precio= 499.99
print(f"el producto seleccionado es {producto} con precio{precio}euros")

#remplace