number1 = int(input('Inserta el número 1: '))

number2 = int(input('Inserta el número 2: '))

def sum(number1, number2):
    result= number1 + number2
    print(f'El resultado es: {result}')
    
def sub(number1, number2):
    result= number1 - number2
    print(f'El resultado es: {result}')   
    
def mult(number1, number2):
    result = number1 * number2
    print(f'El resultado es: {result}')  

def div(number1, number2):
    if(number2 !=0):
       result = number1 / number2
       print(f'El resultado es: {result}') 
    else:
       print(f'El resultado es: {result}')
       
sum(number1,number2)
sub(number1,number2)  
mult(number1,number2) 
div(number1,number2)          
           