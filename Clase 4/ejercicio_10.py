'''
Crea un programa que dado un número entero que designa un periodo de tiempo expresado en segundos, 
imprima el equivalente en días, horas, minutos y segundos.
Por ejemplo:

300000 segundos serán 3 días, 11 horas, 20 minutos y 0 segundos.
7400 segundos serán 0 días, 2 horas, 3 minutos y 20 segundos.
'''
dia_en_segundos = 84400
hora_en_segundos = 3600
minutos_en_segundos = 60
def calc(segundos):
    dias = segundos % dia_en_segundos
    horas = ""
    minutos =  ""
    return f'{segundos} segundos serán {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.'

print(calc(84401))