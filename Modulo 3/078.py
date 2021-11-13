lista = []
for i in range(0,5):
    lista.append(int(input(f'Digire o {i+1}° valor: ')))
print(f'Você digitou os valores {lista}')
menor = min(lista)
maior = max(lista)
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for posicao in range(0,len(lista)):
    if lista[posicao] == maior:
        print(posicao+1, end='... ')
print(f'\nO menor valor digitado foi {menor} nas posições',end=' ')
for pos in range(len(lista)):
    if lista[pos] == menor:
        print(pos+1, end=' ')