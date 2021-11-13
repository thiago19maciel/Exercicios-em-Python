#fatorial
numero = int(input('Digite um numero para ver seu fatorial: '))
i = numero
resultado = 1
for i in range(numero,0,-1):
    print(f'{i}', end = '')
    print(' X ' if i > 1 else ' = ', end='')
    resultado *= i
print(resultado)

i = 1
resultado = 1
while not i > numero:
    resultado = resultado * i
    i += 1
print(resultado)