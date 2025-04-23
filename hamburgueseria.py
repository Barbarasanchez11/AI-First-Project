inventario = int 100
#print(f'El inventario contiene {inventario} hamburguesas')

#se utiliza cuando no sabemos cuando va a terminar el bucle#
while inventario > 0:
    if inventario <= 10:
        print('Advertencia: El inventario está casi vacio.')
    numHamburguesas = int(input('Cuantas hamburguesas quiere el cliente? '))
    
    if numHamburguesas > inventario:
        print(f'No hay suficientes hamburguesas en stock. Solo hay {inventario}')
    else:
        inventario -= numHamburguesas 
        print(f'El cliente ha pedido {numHamburguesas} hamburguesas el inventario ahora tiene {inventario} hamburguesas')   
        
     