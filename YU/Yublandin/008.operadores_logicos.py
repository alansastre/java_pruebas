# and (AND) Y
# RESTRICTIVO PORQUE SE TIENE QUE CUMPLIR TODAS
# LAS CONDICIONES PARA QUE SEA TRUE

email_correcto = 'admin@gmail.com'
password_correcta = '1234'

email = input('introducen tu email: ')
password = input ('introduce password: ')

if email == email_correcto and password == password_correcta:
   print('credenciales correctas') 
else:
    print('credenciales incorrectas') 
    
    
# OR 0
# FLEXIBLE PORQUE ES TRUE SI AL MENOS SE CUMPLE c
# UNA CONDICION
 es_estudiante = input('¿es estudiante? si o no') == 'si' #true o false
 precio = float(input('inntroduce el precio de la compra'))
 if es_estudiante or precio >= 100:
     print(f"Descuento del 20%, precio final: {precio * 0.80}")
 else:
     print(f"precio final: {precio}")
     
# not: invierte una condicion o bool existente
# en java es !
     
 edad = int(input('introduce tu edad'))
 if not edad >= 18:
 print('no tiene acceso.')
 
 # ejemplo not: todo las campos son obligatorios
 
 email = input('Introduce email: ')
 password = input('introduce contraseña: ')
 
 if not email or not password:
     print('todos los campos son obligatorios.')
 else:
     print('registro completo.')
     
 
 
         