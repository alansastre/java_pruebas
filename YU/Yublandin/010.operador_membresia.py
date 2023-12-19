
# in

print("java" in "curso avanzado de java con spring") # true
print("java" in "curso avanzado de python con flask") # false

# in en listas
students = ['Jehiel', 'Judith', 'Noemi', 'Aleydis' ]
name = input ('introduce tu nombre: ')

if name in students:
    print('tienes acceso al curso de java')
else: 
    print('no eres VIP.')
    
    
# not in
if name not in students:
    print ('no tienes acceso al curso de java')
