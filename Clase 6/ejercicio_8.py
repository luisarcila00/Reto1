def tarifas(estrato):  
    if estrato == 1:
        return {
        'cargo_fijo': 2500,
        'metros_consumo': 2200,
        'basuras_alcantarillado': 5500
        }  
    elif estrato == 2:
        return {
        'cargo_fijo': 2800,
        'metros_consumo': 2350,
        'basuras_alcantarillado': 6200
        }
    elif estrato == 3:
        return {
        'cargo_fijo': 3000,
        'metros_consumo': 2600,
        'basuras_alcantarillado': 7400
        }  
    elif estrato == 4:
        return {
        'cargo_fijo': 2800,
        'metros_consumo': 2350,
        'basuras_alcantarillado': 6200
        }  
    elif estrato == 5:
        return {
        'cargo_fijo': 2800,
        'metros_consumo': 2350 ,
        'basuras_alcantarillado': 6200
        }  
    elif estrato == 6:
        return {
        'cargo_fijo': 2800,
        'metros_consumo': 2350,
        'basuras_alcantarillado': 6200
        }  

def facturacion(estrato, consumo):
    # Validacion
    if estrato < 1 or estrato > 6:
        return 'Error: Estrato fuera de rango'
    if consumo < 0:
        return 'Error: El consumo debe ser un valor positivo'
    # Algoritmo
    tarifa = tarifas(estrato)    
    return tarifa['cargo_fijo'] + tarifa['metros_consumo'] * consumo + tarifa['basuras_alcantarillado'] 
    

print(facturacion(4,3))
     