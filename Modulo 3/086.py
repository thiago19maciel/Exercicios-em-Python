matrix = [[], [], []]
column = element = 0
for column in range(0,3):
    for rope in range(0,3):
        matrix[column].append(int(input(f'Digite um valor para [{column},{rope}]: ')))
#mostrar matriz
print('-=-'*20)
for column in range(0,3):
    for rope in range(0,3):
        print(f'[{matrix[column][rope]:^5}]', end=' ')
    print()
print('FIM DO PROGRAMA')

#other solution
'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for linha:
    for coluna:
        matriz[linha][coluna] = int(input(valor))
'''