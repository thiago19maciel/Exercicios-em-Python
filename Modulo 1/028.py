from random import randint as aleatorio
from time import sleep as dormir
from os import system

system('cls')
print('-='*10)
print('Vou pensar em um numero entre 0 e 5. TENTE ADVINHAR')
print('-='*10)

numero_cpu = aleatorio(0,5)
chute = int(input('Em que numero eu pensei??? '))
print('Processando...')
dormir(1)
if chute != numero_cpu:
    print(f'Eu pensei no numero {numero_cpu} e não no {chute}')
else:
    print('Parabéns! Você conseguiu me vencer!!!')