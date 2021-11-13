tupla = ('carro','bicicleta','pneu','arara')
for i in range(0,len(tupla)):
    palavra = tupla[i]
    print(f'\nA palavra {palavra.upper()} tem as vogais: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
