#Para organizar una fiesta de graduación del instituto se compran 9 cajas de refrescos, 
# donde cada caja contiene 24 latas de refrescos. Invitamos a 56 personas y queremos que todas 
# y cada una de ellas consuman la misma cantidad de refrescos ¿Cuántas latas de refresco sobrarán?
compradas = 9
contenido = 24
invitados = 56
cantidad_total_de_refrescos = compradas * contenido
print('Obtenemos la cantidad total de refrescos', cantidad_total_de_refrescos)
refrescos_consumidos = cantidad_total_de_refrescos % invitados
print('Obtenemos la cantidad de refrescos que sobran',refrescos_consumidos)
