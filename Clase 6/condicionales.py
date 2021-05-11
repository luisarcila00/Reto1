def imprimir_nota(nota):   
    if nota > 5 or nota < 0:        
        return 'Error: Nota fuera de rango'
    felicitaciones = ''
    if nota < 3:        
        felicitaciones = 'ud es muy burro'
    if nota >= 3:
        return f'Su nota es {nota}'
    

nota = float(input('Ingrese una nota: '))

print(imprimir_nota(nota))

def imprimir_nota(nota):   
    if nota > 5 or nota < 0:        
        return 'Error: Nota fuera de rango'
    if nota > 3:        
        return f'Gano el curso'
    else:
        return 'Perdió el curso'
    

nota = float(input('Ingrese una nota: '))

print(imprimir_nota(nota))


nombre = input('ingrese su nombre: ')
edad  = int(input('ingrese su edad: '))

def mayor_o_menor(nombre, edad):
    if edad < 0:
        return f'{nombre} aún no ha nacido!'
    if edad < 18:
        return f'{nombre} es menor de edad'
    else:
        return f'{nombre} es mayor de edad'

print(mayor_o_menor(nombre,edad))


