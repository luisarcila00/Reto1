<<<<<<< HEAD
#import mis_retos
#from mis_retos import refrescos_sobrantes
#import carpeta.misteros
import mis_retos as mr

compradas = int(input('Ingrese el numero de cajas compradas: '))
contenido =  int(input('Ingrese el contenido de cada caja: '))
invitados =  int(input('Ingrese el numero de invitados: '))    
print('Cantidad de refrescos que sobran:',refrescos_sobrantes(compradas,contenido,invitados))

peso_empacado = input('Ingrese el peso en gramos empacado: ')
precio_empacado = input('Ingrese el precio empacado: ')
print('El precio por kilo es:',precio_por_kilo(peso_empacado,precio_empacado))
=======
import mis_retos as f
print(f.simular_recaudo_producto(100,1000000,0)) 
print(f.simular_recaudo_producto(1000,1000000,5)) 
print(f.simular_recaudo_producto(158.53,2354837,5))
>>>>>>> d76492aee010ad8bb1c2be30db30aded45c0f414
