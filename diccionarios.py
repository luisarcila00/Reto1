alumno = {
    'nombre': 'Luis',
    'apellido': 'Arcila',
    'nacionalidad': 'Colombiano',
    'edad': 33
}

print(alumno)
alumno['profesor'] = {'nombre': 'Cesar'}
print(f"{alumno['apellido']}")
print(f'{alumno["profesor"]["nombre"]}')
