soma = cont = 0
continuar = 'S'
listaNumeros = []
while continuar == 'S':
    numero = int(input('Digite um numero: '))
    soma += numero
    cont += 1
    listaNumeros.append(numero)
    continuar = str(input('Quer continuar? [S/N}')).upper()
print(f'A média entre os {cont} numeros digitados foi: {soma/cont:.2f}')
print(f'O menor numero foi {min(listaNumeros)} e o maior foi {max(listaNumeros)}')