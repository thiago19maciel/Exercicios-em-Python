from time import sleep

def contador(inicio,fim,passo):
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}")
    cont = inicio
    if passo < 0:
        passo *= -1
    if passo == 0:
        print("Voce digitou passo 0. Para poder contar iremos alterar para passo 1")
        passo = 1
    if inicio > fim:
        while cont >= fim:
            print(f'{cont}',end=' -> ', flush=True)
            sleep(0.5)
            cont -= passo

    elif inicio < fim:
        while cont <= fim:
            print(f'{cont}',end=' -> ',flush=True)
            sleep(0.5)
            cont += passo

    print('Fim da contagem')
    print('-='*20)

print("Programa contador")
contador(1,10,1)
contador(10,0,2)
print("Agora é a sua vez de personalizar a contagem :)")
inicio = int(input("Digite o inicio da contagem: "))
fim = int(input('Digite o fim da contagem: '))
passo = int(input("""\nPasso do contador.
Exemplo: se voce digitar 2, a contagem irá avançar de 2 em 2. 0 -> 2 -> 4...
Digite o passo do contador: """))

contador(inicio,fim,passo)