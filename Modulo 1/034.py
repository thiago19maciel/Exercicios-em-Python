#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
salario = float(input('Digite o salario: '))
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
if salario > 1250:
    print(f'O novo salário com um aumento de 10% é R${salario*1.10:.2f}')
# Para os inferiores ou iguais, o aumento é de 15%.
else:
    print(f'Seu novo salário com aumento de 15% é R${salario*1.15:.2f}')