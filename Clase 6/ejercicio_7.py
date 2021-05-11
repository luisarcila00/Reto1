
def imprimir_caracter(caracter):
    if caracter == 'a' or caracter == 'A':
        return 'Android'
    elif  caracter == 'i' or caracter == 'I':
        return 'IOS'
    else:
        return 'Opción inválida'


print(imprimir_caracter('a'))
print(imprimir_caracter('A'))
print(imprimir_caracter('i'))
print(imprimir_caracter('I'))
print(imprimir_caracter('g'))
print(imprimir_caracter('V'))
print(imprimir_caracter(' '))