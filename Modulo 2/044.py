# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
valor = float(input('Valor: '))
condicao = int(input('''
[1] -> à vista em dinheiro ou check com 10% off 
[2] -> à vista no cartão com 5%off
[3] -> em até 2x no cartão
[4] -> 3x ou mais no cartão com 20% de juros
Qual sua opção: '''))
# – à vista dinheiro/cheque: 10% de desconto
if condicao == 1:
    print(f'Valor total do produto R${valor:.2f}. Mas com 10% off fica R${valor*0.9:.2f}')
# – à vista no cartão: 5% de desconto
elif condicao == 2:
    print(f'O valor cheio é R${valor:.2f}. Mas à vista no cartao fica por R${valor*0.95:.2f}')
# – em até 2x no cartão: preço formal 
elif condicao == 3:
    print(f'Valor total R${valor:.2f}. Parcelado em 2 vezes de R${valor/2:.2f}')
# – 3x ou mais no cartão: 20% de juros
elif condicao == 4:
    parcelas = int(input('EM quantas parcelas: '))
    valorComJuros = valor*1.20
    valorParcela = valorComJuros/parcelas
    print(f'Valor sem juros R${valor:.2f}. Porem parcelado fica R${valorComJuros:.2f}. \nCom {parcelas} parcelas de R${valorParcela:.2f}')
    