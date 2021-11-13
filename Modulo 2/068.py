from random import randint
from time import sleep
print('Vamos jogar par ou impar')
cont = 0
while True:
    jogador = ' '
    while not jogador in 'PI':
        jogador = str(input('Par ou Impar [P/I]: ')).upper()[0]
    numeroJogador = int(input('Diga seu numero: '))
    numeroComputador = randint(0,10)
    soma = numeroJogador + numeroComputador
    sleep(1)
    print('DEU PAR ' if soma % 2 == 0 else 'DEU IMPAR')
    if jogador == 'P' and soma % 2 == 0:
        print(f'Voce escolheu Par e jogou {numeroJogador}, eu joguei {numeroComputador}, a soma deu {soma} \nParabéns você ganhou')
    elif jogador == 'I' and soma % 2 == 1:
        print(f'Voce escolheu Ímpar e jogou {numeroJogador}, eu joguei {numeroComputador}, a soma deu {soma} \nParabéns você ganhou')
    else:
        break
    cont += 1
    print('Vamos jogar denovo \n','-=-'*20)
print(f'Eu joguei {numeroComputador}, voce jogou {numeroJogador}, a soma deu {soma} \nTe peguei ^-^')
print(f'Voce ganhou {cont} vezes consecutivas!!!')