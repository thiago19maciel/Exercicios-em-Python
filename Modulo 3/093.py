# 1° modo de exibir
dadosJogador = {
    'Nome' : str(input('Digite o nome do jogador: '))
}
partidas = int(input(f'Quantas partidas {dadosJogador["Nome"]} jogou: '))
gols = list()
for i in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}: ')))
dadosJogador['Gols'] = gols[:]
dadosJogador['Total'] = sum(gols)
del gols
print('-'*20)
print(dadosJogador)
print('-'*20)
# 2° modo de exibir
for k,v in dadosJogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*20)
# 3° modo de exibição
print(f'O jogador {dadosJogador["Nome"]} jogou {partidas} partidas')
for j in range(partidas):
    print(f' => Na partida {j+1}, fez {dadosJogador["Gols"][j]}')
print(f'No total de {sum(dadosJogador["Gols"])}')