

def facturacion(estrato, consumo):
    # Validacion
    if estrato < 1 or estrato > 6:
        return 'Error: Estrato fuera de rango'
    if consumo < 0:
        return 'Error: El consumo debe ser un valor positivo'
    # Algoritmo
    if estrato == 1:
        cargo_fijo = 2500
        metros_consumo = 2200 * consumo
        basuras_alcantarillado = 5500
    elif estrato == 2:
        cargo_fijo = 2800
        metros_consumo = 2350 * consumo
        basuras_alcantarillado = 6200
    elif estrato == 3:        
        cargo_fijo = 3000
        metros_consumo = 2600 * consumo
        basuras_alcantarillado = 7400
    elif estrato == 4:
        cargo_fijo = 3300
        metros_consumo = 3400 * consumo
        basuras_alcantarillado = 8600
    elif estrato == 5:
        cargo_fijo = 3700
        metros_consumo = 3900 * consumo
        basuras_alcantarillado = 9700
    elif estrato == 6:
        cargo_fijo = 4400
        metros_consumo = 4800 * consumo
        basuras_alcantarillado = 11000

    return cargo_fijo + metros_consumo + basuras_alcantarillado

print(facturacion(4,3))
     