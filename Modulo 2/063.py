qtdNumeros = int(input('Quantos termos de Fibonacci voce deseja mostrar: '))
anterior = 0
atual = 1
print(f'{anterior} -> {atual} -> ', end='')
cont = 3
while qtdNumeros != 0:
    while cont <= qtdNumeros:
        cont+=1
        prox = anterior + atual
        print(f'{prox} -> ', end='')
        anterior = atual
        atual = prox
    print('pausa')
    qtdNumeros = int(input('\nDeseja ver quantos termos a mais: '))
    cont = 1
print(' FIM')