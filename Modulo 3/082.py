listaPares = []
listaImpares = []
listaCompleta = []
while True:
    num = int(input('Digite o numero: '))
    listaCompleta.append(num)
    if num % 2 == 0:
        listaPares.append(num)
    else:
        listaImpares.append(num)
    still = str(input('Continuar[sim/não]: ')).strip().lower()[0]
    if still == 'n':
        break

print(f'A Lista completa é {listaCompleta}')
print(f'A lista de pares é {listaPares} \nE a lista de ímpares é {listaImpares}')