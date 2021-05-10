import math as f
def area_circulo(radio):
    radio = float(radio)
    area = f.pi * (radio**2)
    return area
def volumen_cilindro(radio,altura):
    radio = float(radio)
    altura= float(altura)
    area = area_circulo(radio)
    volumen = area * altura
    return volumen
area = input('Ingrese el radio del circulo: ')
print(f'El area del circulo es {area_circulo(area)}')
altura = input('Ingrese la altura del cilindro: ')
print(f'El volumen del cilindro es {volumen_cilindro(area,altura)}')