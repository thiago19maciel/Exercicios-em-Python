"""
Crie um programa que tenha a função leiaInt(), 
que vai funcionar de forma semelhante ‘a função input() do Python
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
"""

# guardar valor dentro de uma vriavel, dica: ler como string
def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            print("Digitou um numero\n")
            break
        else:
            print("Nao digitou um numero!\n\n")
    return n


numero = leiaInt('Digite um n: ')
print(f"Voce acabou de digitar o numero {numero}")

    # analisar se é um valor numerico
    # enquanto nao for, pedir ao usuario para digirar um valor numerico
