from random import randint
from time import sleep
from os import system
emojis = ['👊','✋','✌️']
resposta = str(input('TEM CORAGEM De jogar jokenpo comigo 😏 ? [Sim/Não]: '))[0]
if resposta in 'Ss':
    jogador = int(input('[0] -> Pedra \n[1] -> papel \n[2] -> tesoura. \nQual sua opção: '))
    cpu = randint(0,2)
    
    frase = 'Processando'
    for ponto in range(0,3):
        system('cls')
        frase += '.'
        print(frase)
        sleep(1)
    if (jogador == 0 and cpu == 2) or (jogador == 1 and cpu == 0) or (jogador == 2 and cpu == 1):
        print(f'Joguei {emojis[cpu]} e voce {emojis[jogador]}. \nVoce ganhou 😠')
    elif jogador == cpu:
        print(f'Nós dois jogamos {emojis[jogador]}. EMPATE 😑')
    else:
        print(f'Joguei {emojis[cpu]} e voce {emojis[jogador]}. Voce perdeu 😂')
        print('Mais sorte na proxima vez 😝')
else:
    print('Seu medroso 😒')