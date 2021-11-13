#Desenvolva um programa que pergunte a distância de uma viagem em Km.
km = float(input('Distancia da viagem: '))

#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
if km <= 200:
    print(f'Sua viagem de {km}Km custa R${km*1.75 :.2f}')
#E R$0,45 parta viagens mais longas.
else:
    print(f'Sua viagem de {km}Km custará R${km*1.5 :.2f}')