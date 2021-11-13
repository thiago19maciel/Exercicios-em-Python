"""
cores = (
    "\033[m", #  0- limpa
    "\033[0;30;42m", # 1 - fundo verde
    "\033[0;30;41m", # 2 - fundo vermelho
    "\033[0;37;47m", # 3 - inverter cores de fundo e texto
    "\033[1;33;47m", # 4 - amarelow
    "\033[0;30;47m" # 5 - preto e brancow
    )


def ajuda(comando):
    titulo(f"Acessando manual do comando \'{comando}\' ",4) # \' \' escape para que seja possivel digitar aspas como texto
    print(cores[5],end='')
    help(comando)
    print(cores[0],end='')


def titulo(msg,cor=0):
    tam = len(msg) + 4
    print(cores[cor],end='')
    print("~" *tam)
    print(f"  {msg}")
    print("~" *tam)
    print(cores[0],end='')


while True:
    titulo("Sistema de ajuda pyHelp",1)
    comando = str(input("Digite o comando ou biblioteca: "))
    if comando == 'fim':
        break
    else:
        ajuda(comando)
    
titulo("Até logo",2)

"""

from termcolor import *
from colorama import *

tupla = 'red', 'blue', 'green', 'yellow', 'magenta', 'cyan'
for cor in tupla:
    print(colored('TESTE DE TEXTO', cor))