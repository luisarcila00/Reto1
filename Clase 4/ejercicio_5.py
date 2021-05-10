#Escribir un programa que lea un entero positivo n, introducido por el usuario y después muestre en 
# pantalla la suma de todos los enteros desde 1 hasta n. La suma de los primeros enteros positivos 
# puede ser calculada de la siguiente forma: suma = n(n+1)/2

def entero(n):
    n = int(n)
    suma = (n * (n+1))/2
    return suma
numero = input('Ingresa un número entero: ')
impresion = entero(numero)
print(impresion)
