"""Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador
mesmo que algum dado não tenha sido informado corretamente.
"""

def ficha(jogador = "<Desconhecido>", gol = 0):
    print(f"O jogador {jogador} marcou {gol} gols")
    

nome = str(input("Digite o nome do jogador: "))
gols = str(input(f"Quantos gols {nome} fez: "))
if gols.isnumeric(): # se gols for igual a um numero
    gols = int(gols)
else: # se gols nao for um numero
    gols = 0

if nome.strip() == '': # se nome for igual a vazio
    ficha(gol=gols) # apenas o parametro gol
else:
    ficha(nome,gols) # se nome nao estiver vazio, passa paramentro nome, e apos validar gols, passar gols

