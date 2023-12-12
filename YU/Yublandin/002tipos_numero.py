
edad= 30
peso = 80.34

print(edad + 2)

print(peso - 5)

# utilizando constructor convertir de texto a numero y viceversa
edad2 = int(40)
peso2 = float(90.55) # float es para decimales
print(edad2 + 2)
print(peso2 - 5)

edad3 ="70"
peso3 ="100.21" # es un texto por las comillas

print(edad3 +2)
print(peso2 -5)

TypeError: can only concatenate str (not "int") to str

#print(edad3 +2) no puede sumar algo que es texto por estar en comillas
#print(peso2 -5)

edad3_num = int(edad3) ##convierte el texto "70" a numero 70
print(edad3_num + 2)

peso3_num = float(peso3)
print(peso3_num - 5)

#convertir un numero a texto
codigo_postal = str(28003) #convertir de int a str
