continua = True
soma = cont = 0
while continua:
    numero = int(input('Digite um numero [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'A soma de todos os {cont} numeros digitados é: {soma}')