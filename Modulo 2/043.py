# Desenvolva uma lógica que leia o peso e a altura de uma pessoa
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
if imc < 18.5:
    print(f'{imc:.2f} de imc. Resultado: Abaixo do Peso')
elif imc < 25:
    print(f'{imc:.2f} de imc. Resultado: Peso ideal')
elif imc < 30:
    print(f'{imc:.2f} de imc. Resultado: Sobrepeso')
elif imc < 40:
    print(f'{imc:.2f} de imc. Resultado: Obesidade')
else:
    print(f'{imc:.2f} de imc. Resultado: Obesidade Morbida')

