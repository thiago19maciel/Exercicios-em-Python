'''from random import randint
from time import sleep
numero = randint(1,10)
chute = int(input('Advinhe o numero que estou pensando de 1 a 10: '))
print('Hmmmm')
sleep(1)
cont = 1
while chute != numero:
    if chute > numero:
        print('MENOS')
    if chute < numero:
        print('MAIS')
    chute = int(input('Tente novamente: '))
    cont += 1
print('Acertou com \033[4;35m',cont,'\033[m tentativas')
'''

from random import randint
computador = randint(1,10)
print('Pensei num numero de 1 a 10 \nSerá que voce consegue advinhar qual?')
acertou = False
cont = 0
while not acertou:
    chute = int(input('Qual seu palpite: '))
    if chute == computador:
        acertou = True
    if chute > computador:
        print('MENOS')
    if chute < computador:
        print('MAIS')
    cont += 1
print('Acertou com \033[4;35m',cont,'\033[m tentativas')
