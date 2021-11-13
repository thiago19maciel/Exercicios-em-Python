#Crie um programa que leia um número Real qualquer pelo teclado 
num = float(input('Digite qualquer numero: '))
#Mostre na tela a sua porção Inteira.
print(f'A parte inteira do numero {num} é {int(num)}')

import math
print(f'A parte inteira do numero {num} é {math.trunc(num)}') #trunca o valor
print(f'A parte inteira do numero {num} é {math.floor(num)}') #arredonda para baixo