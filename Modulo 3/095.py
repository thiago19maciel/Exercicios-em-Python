# um dia eu tive muita dificuldade com esse codigo
lista = []
dadosJogador = dict()
# Coletando dados
while True:
    dadosJogador.clear()
    dadosJogador = {
        'Nome' : str(input('Digite o nome do jogador: '))
    }
    partidas = int(input(f'Quantas partidas {dadosJogador["Nome"]} jogou: '))
    gols = list()
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {i+1}: ')))
    dadosJogador['Gols'] = gols[:]
    dadosJogador['Total'] = sum(gols)
    gols.clear()

    # Salvando dados do jogador em uma lista
    lista.append(dadosJogador.copy())

    while True:
        resposta = input('Quer continuar [S/N]? \n').upper()[0]
        if resposta in 'SN':
            break
        else:
            print(f'ERRO! Você digitou {resposta}')
    if resposta == 'N':
        break

print('cod ',end='')
for i in dadosJogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k,v in enumerate(lista):
    print(f'{k:>3} ',end='') # varivel k representa o index da lista
    for dado in v.values():
        print(f'{str(dado):<15}',end='')
        #dado formatado para string pois pode ser um n°
    print()
print('-'*40)

while True:
    codigo = int(input('Digite o codigo para ver o jogador (999 para parar): '))
    if codigo == 999:
        break
    elif codigo >= len(lista):
        print(f'Erro! Não existe jogador com o código {codigo}')
    else:
        print(f'Levantamento do jogador {lista[codigo]["Nome"]}')
        for i, g in enumerate(lista[codigo]["Gols"]): # i representa o index
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*40)
print('Volte sempre :)')