# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
print('Welcome to the Fonterrada Bank :)')
#Pergunte o valor da casa, o salário do comprador 
valor = int(input('Valor da casa: '))
salario = int(input('Digite seu salário: '))
#e em quantos anos ele vai pagar. 
tempoEmAnos = int(input('Em quantos anos pretende pagar: ')) 
parcelas = tempoEmAnos*12
valorParcela = valor / parcelas
# A prestação mensal não pode exceder 30% do salário ou
print(f'A casa custa R${valor} e em {parcelas}X sai por R${valorParcela:.2f} mês')
if valorParcela < salario * 0.3:
    print('Great. Loan Aproved :)')
# então o empréstimo será negado.
else:
    print('Sorry, but You have no condition to pay the loan :(')
