#Reto 2
# Encontramos que el telefono se encuentra dentro de la categoria del Tipo General con el iva gravado del 21%
iva_general = 21
# Me surge la duda si el precio del telefono en el escaparate esta gravado con el IVA de 21% o si es solo el precio neto. Por ende realizare el ejercicio de las 2 maneras
#En este asumire que el costo del telefono incluye el IVA
print('Asumiendo que el costo del telefono es con iva incluido')
costo_telefono = 420
#Procedo a obtener el iva gravado en el telefono
iva_gravado = costo_telefono * (iva_general/100)
print('Valor del iva',iva_gravado,'€')
#obtengo el valor neto del telefono sin iva
costo_telefono_sin_iva = costo_telefono - iva_gravado
print('Costo telefono sin iva', costo_telefono_sin_iva,'€')
# al dia siguiente el telefono sufrira un incremento del 20%
incremento = 20
costo_incremento = costo_telefono_sin_iva * (incremento/100)
print('Valor incremento',costo_incremento,'€')
#Sumamos el incremento al costo del telefono
costo_telefono_incremento = costo_telefono_sin_iva + costo_incremento
print('Costo del telefono con incremento',costo_telefono_incremento,'€')
#buscamos cuanto seria el iva del nuevo valor del telefono
nuevo_iva = costo_telefono_incremento * (iva_general/100)
print('Nuevo valor del iva con incremento',nuevo_iva,'€')
#sumamos el nuevo iva con el nuevo costo del telefono
costo_total_con_iva = costo_telefono_incremento + nuevo_iva
print('Nuevo precio mas iva',costo_total_con_iva,'€')

#Asumiendo que el costo del telefono es sin iva incluido
#Obteniendo el 20% de incremento
print('Asumiendo que el costo del telefono es sin iva incluido')
incremento2 = costo_telefono * (incremento/100)
print('Incremento',incremento2)
costo_con_incremento = costo_telefono + incremento2
print('Costo con incremento',costo_con_incremento)
iva = costo_con_incremento * (iva_general/100)
print('Iva',iva)
costo_con_iva = costo_con_incremento + iva
print('Costo con total',costo_con_iva)