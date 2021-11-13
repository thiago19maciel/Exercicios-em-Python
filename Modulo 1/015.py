#Escreva um programa que pergunte a quantidade de distancia percorridos
distancia = int(input('Distancia percorrida em KM: '))
#quantidade de dias pelos quais ele foi alugado.
dias = int(input('Quantos dias? ')) 
#Calcule o preço a pagar
#Sabendo que o carro custa R$60 por dia e R$0,15 por distancia rodado.
preco = (60 * dias) + (0.15 * distancia)
print(f'Preço total a pagar R${preco:.2f}')