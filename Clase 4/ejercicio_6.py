'''
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa 
corporal calculado redondeado con dos decimales.
IMC = peso [kg]/ estatura [m2]).
'''
peso = input('Ingrese su peso (en kg): ')
estatura = input('Ingrese su estatura (en metros): ')
def calcular_IMC(peso,estatura):
    peso=float(peso)
    estatura=float(estatura)**2
    imc = peso/estatura
    return round(imc,2)
imc = calcular_IMC(peso,estatura)
print(f'Tu índice de masa corporal es {imc}')



