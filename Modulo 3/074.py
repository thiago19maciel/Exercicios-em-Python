from random import randint
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),)
print(f'Eu sorteei os numeros{numeros}')
print(f'O maior valor sorteado foi {sorted(numeros)[-1]}')
#pode usar max(numeros)
print(f'O menor valor sorteado foi {sorted(numeros)[0]}')
#pode usar min(numeros)