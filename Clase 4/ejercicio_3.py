def sumar_iva(total, iva=19):
    iva = iva  + 100
    total = (total * iva) / 100
    return round(total,2)

print(sumar_iva(50000,19))