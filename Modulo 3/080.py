lista = []
for i in range(0,5):
    numero = int(input('Digite um numero: '))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print(lista)
'''
count = 0
lista = []
while count < 5:
    numeroDoUsuario = int(input('Insira o valor: '))
    lista.append(numeroDoUsuario)
    count += 1

lista.sort()
lista.reverse()

print('\n\n ')
for i in range(len(lista)):
    valorDaLinha = i+1
    print(f'O valor na linha {i+1} é: {lista[i]}')
'''