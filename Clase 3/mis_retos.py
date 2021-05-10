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

def simular_recaudo_producto(precio_base, cantidad, porcentaje_actual=0):
    porcentaje_actual = porcentaje_actual  + 100
    precio_base_mas_iva = (precio_base * porcentaje_actual) / 100
    precio_total_mas_iva = precio_base_mas_iva * cantidad
    iva = 1.19
    precio_mas_iva = (precio_base * iva) 
    precio_total_iva_19 = (precio_mas_iva * cantidad) 
    valor_recaudado = precio_total_iva_19 - precio_total_mas_iva
    return round(valor_recaudado,2)