#Declarar variables#

#nombre = input ('¿Cual es tu nombre? ')
edad = int(input('¿Cual es tu edad? '))
#print(f'Hola {nombre} tienes {edad} años')#se pone f en el print para evitar que haya conflictos con las variables, si no tenemos variables dentro y es texto plano no sería necesaria la f#

#Función saludar#

##def saludar(nombre):
  #print('Hola,' + nombre + 'Bienvenida al workshop de Python')


#saludar('barbara') 

#Otra forma de hacerlo, para esto debemos tener declarada una variable#
#def saludar(nombre):
  #print(f'Hola, {nombre} Bienvenida al workshop de Python')


#saludar(nombre) 


#bucle for#

#for recorrer in range(1,10):
  # print(recorrer)
  
def esMayorDeEdad(edad):
    if edad >= 18:
       return 'Eres mayor de edad'
    else:
        return 'Eres menor de edad'
   
print(esMayorDeEdad(edad))
#bucle while#
