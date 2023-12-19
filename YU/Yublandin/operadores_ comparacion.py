# todos estos operadores devuelven un booleano

# = es par asignación de un valos a una variable

# igual==

password = input('introduce contraseña:')
password_correct = 'admin'
print(password == password_correct)

email = input('introduce tu email').lower()
email_correct = 'alan@gmail.com'
print(email == email_correct)

# Distinto que !=
# inversa de ==

password = input('introduce contraseña: ')
password_correct = 'admin'
if password != password_correct:
    print("credenciales incorrectas")
    
    respuesta_correcta = 'madrid'
    capital = input('introduce capital de Spain: ').lower().replace(" ","")
    
    if capital != respuesta_correcta:
        print('respuesta incorrecta.')

    else:
        print('has acertado toma un pin.')

    # > mayor que (Greater Than, GT)
    
    # >= mayor o igual que (Greater Than or equals, GTE)
    print(50> 20 ) #true
    print(50> 50 ) #false
    print(50>= 50 ) #true
    print(50> 100 ) #false
    
    # > menor que (less Than, LT)

   # >= menor o igual que (less Than or equals, LTE)
    print(50< 20 ) #false
    print(50< 50 ) #false
    print(50<= 50 ) #true
    print(50< 100 ) #true
    

    