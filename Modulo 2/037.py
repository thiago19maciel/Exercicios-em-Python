#Escreva um programa em Python que leia um número inteiro qualquer e
numero = int(input('Digite um numero: '))
# peça para o usuário escolher qual será a base de conversão: 
print('[1] para binário \n[2] para octal \n[3] para hexadecimal')
opcao = int(input('Qual conversão deseja fazer? '))
if opcao == 1:
    print(f'{numero} convertido para binário é igual a: {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para octal é igual a: {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para hexadecimal é igual a: {hex(numero)[2:]}')
else:
    print('OPÇÃO INVALIDA! TENTE NOVAMENTE')
# 1 para binário, 2 para octal e 3 para hexadecimal.