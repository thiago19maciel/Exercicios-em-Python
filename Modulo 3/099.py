# imports
from os import system
from time import sleep


# funcoes
def maior(*comparacao):
    print(f"O maior valor é {max(comparacao)} e o menor é {min(comparacao)}")

def cls():
    system("cls")


# programa principal 
listas_valores = list()
valores = list()
while True:
    valor = int(input("Informe um valor: "))
    valores.append(valor)
        
    # pergunta ao usuario se quer adicionar um valor
    while True:
        continuar = str(input("Deseja informar mais um valor? [Sim/Nao]: ")).upper()[0]
        if continuar in "SN":
            break
        else:
            print("Erro! Digite apenas S ou N")
    cls()
    if continuar == "N":
        # pergunta se quer fazer nova comparacao
        while True:
            resposta = str(input("Deseja adicionar uma nova comparação? [Sim/Nao]: ")).upper()[0]
            if resposta in "SN":
                listas_valores.append(valores[:])
                valores.clear()
                break
            else:
                print("Erro! Digite apenas S para sim ou N para nao")
        if resposta == "N":
            break
    cls()
# imprime os valores informados
for lista in listas_valores:
    print('-=-' * 15)
    if len(lista) == 1:
        print(f"Foi informado {len(lista)} valor \nO valor foi: {lista[0]}", flush=True)
    if len(lista) > 1:
        print(f"Foram informados {len(lista)} valores\nOs valores foram: ",end='')
        for v in lista:
            sleep(1)
            print(v,end=' | ', flush=True)
    sleep(1)
    maior(*lista)
print("-=-" * 15, "\nFim do programa")
