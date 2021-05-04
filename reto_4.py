#Para organizar una fiesta de graduación del instituto se compran 9 cajas de refrescos, 
# donde cada caja contiene 24 latas de refrescos. Invitamos a 56 personas y queremos que todas 
# y cada una de ellas consuman la misma cantidad de refrescos ¿Cuántas latas de refresco sobrarán?
compradas = 9
contenido = 24
invitados = 56
cantidad_total_de_refrescos = compradas * contenido
refrescos_sobrantes = cantidad_total_de_refrescos % invitados
print('Cantidad de refrescos que sobran:',refrescos_sobrantes)
