#Declarar variables#

nombre = input ('¿Cual es tu nombre? ')
#edad = int(input('¿Cual es tu edad? '))
#print(f'Hola {nombre} tienes {edad} años')#se pone f en el print para evitar que haya conflictos con las variables, si no tenemos variables dentro y es texto plano no sería necesaria la f#

#Función saludar#

def saludar(nombre):
  print('Hola,' + nombre + 'Bienvenida al workshop de Python')


saludar('barbara') 

#Otra forma de hacerlo#
def saludar(nombre):
  print(f'Hola, {nombre} Bienvenida al workshop de Python')


saludar(nombre) 