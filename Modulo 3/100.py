from time import sleep
from random import randint


sorteados = []
def sorteia(*valores):
    print("Sorteando numeros...", flush=True)  
    while len(sorteados) < 5:
        n = randint(0,9)
        if not n in sorteados:
            sorteados.append(n)

def somaPar(numeros):
    s = 0
    print(f"\nSomando os pares: ",end='')
    for j in numeros:
        if j % 2 == 0:
            print(f"{j}",end=' ')
            s += j
    print(f"temos {s:.2f}")


# programa principal
sorteia(sorteados)
print("Os numeros sorteados foram:",end=' ')
for c in sorteados:
    print(c, end=' ', flush=True)
    sleep(0.5)

somaPar(sorteados)
