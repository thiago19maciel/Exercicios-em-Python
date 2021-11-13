""" 
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""

# variaveis
valor = soma = 0
flag = 999

# main
while (valor!=flag):
    valor = int(input("Digite um numero: "))
    if valor != 999:
        soma+=valor

print(f"Soma igual a: {soma}")