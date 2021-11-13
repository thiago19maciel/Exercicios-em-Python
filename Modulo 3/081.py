lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    more = str(input('Continuar [sim/não]: ')).strip().upper()[0]
    if more == 'N':
        break
print(f'\nVocê digitou {len(lista)} valores')
print(f'Os valores em forma decrescente são: {sorted(lista,reverse=True)}')
print(f'O valor 5 faz parte desta lista') if 5 in lista else print('O valor 5 não faz parte da lista')