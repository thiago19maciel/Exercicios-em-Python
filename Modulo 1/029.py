#Escreva um programa que leia a velocidade de um carro.
velocidade = float(input('Velocidade: '))
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
if velocidade > 80:
    print(f'Passou a {velocidade} numa pista de 80 !!! \nVai pagar R${((velocidade-80)*30):.2f} de multa')
#A multa vai custar R$7,00 por cada Km acima do limite.
else:
    print(f'{velocidade}Km. Voce estava dentro do limite de 80Km')