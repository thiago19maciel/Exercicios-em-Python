matriz = [[0,0,0], [0,0,0], [0,0,0]]
somaPares = soma3Coluna = maior2Coluna = 0
for string in range(0,3):
    for column in range(0,3):
        number = int(input(f'Digite um valor para [{column},{string}]: '))
        matriz[string][column] = number
        if number % 2 == 0:
            somaPares += number
        if column == 2:#pode fazer for i in range(0,3): matriz [l]para percorrer linhas [2]coluna fixa
            soma3Coluna += number
        if column == 1 and number > maior2Coluna:
            maior2Coluna = number
for string in range(0,3):
    for column in range(0,3):
        print(f'[{matriz[string][column]:^5}]', end='')
    print()
print(f'A soma dos pares é {somaPares}')
print(f'A soma dos valores da 3° coluna é {soma3Coluna}')
print(f'O maior valor da segunda coluna é {maior2Coluna}')