def read_bool(prompt):
    
            respuesta = input(prompt)
            booleano = respuesta.lower() in ['si, 'yes', 'sí','oui','ja']
            return booleano
        except Exception:
            print('no se ha podido leer el numero float')
    
    
edad = read_int('introduce tu edad : ')   
   
peso = read_int('introduce tu peso : ')

altura = read_int('introduce tu altura: ')

altura = read_float('introduce tu salario: ')

altura = read_bool('si trabaja o no (si/no): ')
