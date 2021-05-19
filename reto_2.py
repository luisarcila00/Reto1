cliente0 = {
    'nombre': 'César Díaz',
    'nacional': True,
    'agujas': 0.0,
    'escolares': 0.0,
    'hogar': 0.0    
}
cliente1 = {
    'nombre': 'César Díaz',
    'nacional': False,
    'agujas': 25000,
    'escolares': 10000.0,
    'hogar': 15000.0    
}
cliente2 = {
    'nombre': 'César Díaz',
    'nacional': True,
    'agujas': 150000000.0,
    'escolares': 30000000.0,
    'hogar': 20000000.0    
}
cliente3 = {
    'nombre': 'César Díaz',
    'nacional': True,
    'agujas': 100000001.0,
    'escolares': 32000000.0,
    'hogar': 41325120.0    
}
cliente4 = {
    'nombre': 'César Díaz',
    'nacional': True,
    'agujas': 70000100.0,
    'escolares': 20000000.0,
    'hogar': 40000001.0    
}
cliente5 = {
    'nombre': 'César Díaz',
    'nacional': True,
    'agujas': 70000000.0,
    'escolares': 30000000.0,
    'hogar': 40000000.0    
}

def calculo_descuentos(cliente):
    descuento_agujas = 0.0
    descuento_escolares = 0.0
    descuento_hogar = 0.0
    compras_acumuladas = cliente['agujas'] + cliente['escolares'] + cliente['hogar']
    if cliente['nacional']:
        if cliente['agujas'] > 70000000:
            descuento_agujas = 5.0            
        if cliente['escolares'] > 30000000:            
            descuento_escolares = 5.0            
        if cliente['hogar'] > 40000000:                        
            descuento_hogar = 5.0          
        if compras_acumuladas >= 200000000:
            descuento_agujas = 10.0
            descuento_escolares = 10.0
            descuento_hogar = 10.0
        elif cliente['agujas'] > 70000000 and cliente['escolares'] > 30000000 and cliente['hogar'] > 40000000:
            descuento_agujas = 7.0
            descuento_escolares = 7.0
            descuento_hogar = 7.0 
    else:
        if cliente['agujas'] > 25000:
            descuento_agujas = 3.0            
        if cliente['escolares'] > 10000:            
            descuento_escolares = 3.0            
        if cliente['hogar'] > 15000:                        
            descuento_hogar = 3.0          
        if compras_acumuladas >= 100000:
            descuento_agujas = 8.0
            descuento_escolares = 8.0
            descuento_hogar = 8.0
        elif cliente['agujas'] > 25000 and cliente['escolares'] > 10000 and cliente['hogar'] > 15000:
            descuento_agujas = 5.0
            descuento_escolares = 5.0
            descuento_hogar = 5.0 
    return {'nombre':cliente['nombre'],'agujas':descuento_agujas,'escolares':descuento_escolares,'hogar':descuento_hogar}

print(calculo_descuentos(cliente1))
print(calculo_descuentos(cliente2))
print(calculo_descuentos(cliente3))
print(calculo_descuentos(cliente4))
print(calculo_descuentos(cliente5))