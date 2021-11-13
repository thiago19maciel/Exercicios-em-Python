lista = []
from os import system
while True:
    numero = int(input('Digite um numero: '))
    system("cls")
    if numero in lista:
        print(f'Valor {numero} duplicado. Não vou adicionar')
    else:
        lista.append(numero)
        print(f'Valor {numero} adicionado')
    continuar = str(input('Deseja continuar [Sim/Não]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\nValores digitados {sorted(lista)}')
