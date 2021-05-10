compradas = int(input('Ingrese el numero de cajas compradas: '))
contenido =  int(input('Ingrese el contenido de cada caja: '))
invitados =  int(input('Ingrese el numero de invitados: '))

cantidad_total_de_refrescos = compradas * contenido
refrescos_sobrantes = cantidad_total_de_refrescos % invitados
print('Cantidad de refrescos que sobran:',refrescos_sobrantes)