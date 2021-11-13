dados = list()
galera = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    galera.append(dados[:])
    if len(galera) == 1:
        maior = menor = dados[1]
    
    #verificar classes de peso
    if len(galera) == 1:
        maior = menor = dados[1]
    else:
        #maior peso
        if dados[1] > maior:
            maior = dados[1]
        #menor peso
        if dados[1] < menor:
            menor = dados[1]
    dados.clear()
    resp = str(input('continuar [S/N]: '))
    if resp in 'Nn':
        break

maisPesados = list()
maisLeves = list()
#verificar as pessoas mais pesadas
for p in galera: #percorrer todos os elementos trabalhando direto com cada posição
    if p[1] == maior:
        maisPesados.append(p[0])
    if p[1] == menor:
        maisLeves.append(p[0])
        print('-=-'*20)
print(f'Foram cadastradas {len(galera)}')
print(f'O maior peso foi Kg {maior:.2f} com {maisPesados}')
print(f'O menor peso foi Kg {menor:.2f} com {maisLeves}')