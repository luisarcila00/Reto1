def refrescos_sobrantes(compradas,contenido,invitados):    
    cantidad_total_de_refrescos = compradas * contenido
    refrescos_sobrantes = cantidad_total_de_refrescos % invitados
    return refrescos_sobrantes

def precio_por_kilo(peso_empacado,precio_empacado,peso_kilo = 1000):            
    peso_empacado = float(peso_empacado)
    precio_empacado = float(precio_empacado)
    precio_gramo = precio_empacado / peso_empacado
    precio_kilo = precio_gramo * PESO_KILO
    return round(precio_kilo,2)
