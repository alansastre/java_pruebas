# Operadores de identidad

email = None
email_user = input('introduce tu email')
if email_user.endswith('gmail.com'):
    email = email_user

# is

if email is None: # habitual para comprar si existe un valos
    print('no se ha podido completar el registro.')
# el numero 1 es true

print(1 == true) # true compara valores, significado de 1 en python
print(0 == true) # false
print(1 is true) # false compara la identidad , es decir que 1 es numero y true un booleado

# is not

if email is None:
    print('el email es correcto, registro completado.')

# is else

if email is None:
    print('no se ha podido completar el registro.')
else:
    print('el email es correcto, registro completado.')
    
    if email is not None: #combrueba que le email no es nulo o vacio
         print('el email es correcto, registro completado.')
    else:
        print('email icorrecto.')
# in
