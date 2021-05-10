#Entradas
PESO_KILO = 1000
peso_empacado = input('Ingrese el peso en gramos empacado: ')
precio_empacadao = input('Ingrese el precio empacado: ')
peso_empacado = float(peso_empacado)
precio_empacadao = float(precio_empacadao)
precio_gramo = precio_empacadao / peso_empacado
precio_kilo = precio_gramo * PESO_KILO
print('El precio por kilo es:',precio_kilo)




