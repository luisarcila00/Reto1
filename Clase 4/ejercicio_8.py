# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento 
# del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le 
# hace por no ser fresca y el coste final total.
precio_barra_pan = 3.49
def coste_final(barras_vendidas, descuento = 60):
    descuento = descuento / 100
    precio_habitual = barras_vendidas * precio_barra_pan
    descuento_por_no_ser_fresco = precio_habitual * descuento
    precio_con_descuento = precio_habitual - descuento_por_no_ser_fresco
    return f"El precio habitual es {precio_habitual}\nDescuento por no ser fresco es {descuento_por_no_ser_fresco}\nEl coste final con descuento es {round(precio_con_descuento,2)}"

print(coste_final(100))
    