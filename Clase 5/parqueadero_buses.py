def parqueadero_buses(total_parqueadero, numero_bus):
    # valiadar las entradas
    if total_parqueadero % 3 != 0:
        return 'Error: El número de parqueadero no es multiplo de 3'

    if numero_bus > total_parqueadero:
        return 'Error: El numero de bus excede el total de parqueaderos'

    TOTAL_LOTES = 3
    parqueaderos_lote = total_parqueadero / TOTAL_LOTES
    if numero_bus <= parqueaderos_lote:
        return 1
    if numero_bus <= 2 * parqueaderos_lote:
        return 2
    if numero_bus <= 3 * parqueaderos_lote:
        return 3    
print(parqueadero_buses(100,91))
    