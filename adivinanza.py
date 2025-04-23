import random

def juegoAdivinanza():
    numeroSecreto = random.randint(1,100)
    intentos = 0
    adivinado = False
    
    print('Bienvenid@ al juego de adivinanza de números!')
    print('Estoy pensando en un número entre 1 y 100')
    
    
    while not adivinado:
        experimento = int(input('Adivina el número: '))
        intentos += 1
        
        if experimento < numeroSecreto:
            print('El número es mayor')
        elif experimento > numeroSecreto:
            print('El número es menor')   
        else:
            adivinado = True
            print(f'Felicidades!Adivinaste el número de {intentos} intentos')    

juegoAdivinanza()            