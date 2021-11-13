from os import system
system("cls")
listaNumeros = []
for c in range(1,3):
    numero = int(input(f'Digite o {c}° numero: '))
    listaNumeros.append(numero)

continuar = False
while not continuar:
    print('[1] -> somar \n[2] -> multiplicar \n[3] -> Ver qual o maior número \n[4] -> Digitar novos numeros \n[5] -> sair')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print('A soma entre',listaNumeros[0], 'e',listaNumeros[1], 'é: ',listaNumeros[0]+listaNumeros[1])
    if opcao == 2:
        print(f'A multiplicação entre {listaNumeros[0]} e {listaNumeros[1]} é: {listaNumeros[0] * listaNumeros[1]}')
    if opcao == 3:
        if listaNumeros[0] > listaNumeros[1]:
            print(f'Entre {listaNumeros[0]} e {listaNumeros[1]}, {listaNumeros[0]} é maior')
        else:
            print(f'Entre {listaNumeros[0]} e {listaNumeros[1]}, {listaNumeros[1]} é maior')
    if opcao == 4:
        for i in range(1,3):
            listaNumeros[i] = int(input(f'Digite o {i} numero: '))
    if opcao == 5:
        continuar = True
    input('Aperte enter para continuar')
    system("cls")