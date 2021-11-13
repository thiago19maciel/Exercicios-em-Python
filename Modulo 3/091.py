from operator import itemgetter
from random import randint

jogadores = {
    'P1' : randint(1,6),
    'P2' : randint(1,6),
    'P3' : randint(1,6),
    'P4' : randint(1,6)}

for k,v in jogadores.keys():
    print(f'O {k} tirou {v} no dado')

ranking = list()
ranking = sorted(jogadores.items(),key=itemgetter(1), reverse=True)

for i,j in enumerate(ranking): # variavel i é cada elemento da lista aninhada
    print(f'{i+1}° lugar: {j[0]} com {j[1]}') # variavel j é o elemento de cada listinha dentro da lista

#cria dicionario com os dados jogados
# import time,random
# data = {}
# for c in range (0,4):
#     player_id = "player "+str(c+1)
#     data[player_id] = random.randint(1,6)
#     time.sleep(.5)
#     print(f'The {player_id} has {data[player_id]}')
    
# n = 1
# for c in range(0,7):
#     for p,v in data.items(): #verifica se o value é o maior numero, se nao, passa
#         if v == (6 - c):
#             print(f"The {n}º position is the {p} with {v}")
#             n += 1