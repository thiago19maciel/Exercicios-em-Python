termo = int(input('Digite o primeiro termo da pa: '))
razao = int(input('Digite a razão da sua pa: '))
qtdTermos = 10
termosMostrados = 0
while qtdTermos != 0:
    termosMostrados += qtdTermos 
    cont = 1
    while cont <= qtdTermos:
        print(f'{termo} -> ', end='')
        termo += razao
        cont +=1
    print(' Pausa')
    qtdTermos = int(input('Quantos termos voce quer mostrar a mais: '))
print(f'Foram {termosMostrados} termos mostrados.')