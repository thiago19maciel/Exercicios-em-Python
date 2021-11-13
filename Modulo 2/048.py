#soma entre todos os números que 
#são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('Soma dos n° multiplos de tres entre 1 e 500')
cont = 0
soma = 0
for i in range(1,501):
    if i % 3 == 0 and not i%2 == 0:
        soma += i
        cont += 1
print(f'A Soma dos {cont} numeros deu {soma}')
