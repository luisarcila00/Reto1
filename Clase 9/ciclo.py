for numero in range(11):
    print(2 *(numero * -1))

datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}

clave = datos_basicos.keys()
valor = datos_basicos.values()

cantidad_datos = datos_basicos.items()

for clave, valor in cantidad_datos:
    print(clave + ": " + valor)
    
