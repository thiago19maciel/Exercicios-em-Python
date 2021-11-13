tupla = (int(input('Digite um valor: ')),int(input('Digite outro valor: ')),
int(input('Digite outro valor: ')),int(input('Digite outro valor: ')))
print(f'Você digitou os numeros {tupla}')
print(f'O numero 9 aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro numero 3 aparece na {tupla.index(3)+1}° posição')
else:
    print('Você nao digitou o numero 3')
print('Os seguintes numeros digitados são pares:', end=' ')
for i in tupla:
    if i % 2 == 0:
        print(f'{i}',end='')