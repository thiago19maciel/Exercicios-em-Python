jogo = list()
jogos = list()
print('-='*15)
print('JOGAR MEGA SENA')
print('-='*15)
total = int(input('Quantos jogos voce deseja fazer: '))
from random import randint
from time import sleep
from os import system
for tempo in range(2):
    frase = 'Sorteando Jogos.'
    for c in range(0,3):
        system("cls")
        print(frase)
        sleep(1)
        frase += '.'

for i in range(0,total):
    for j in range(0,6):
        while True:
            numero = randint(1, 60)        
            if not numero in jogo:
                break
        jogo.append(numero)
    jogos.append(jogo[:])
    jogo.clear()
print('RESULTADOS\n','-=-'*10)
for j in range(0,total):
    print(f'Jogo {j+1}: {sorted(jogos[j])}')
print('-=-'*10)
print('Obrigado por Jogar na Mega Sena e BOA SORTE !!!')