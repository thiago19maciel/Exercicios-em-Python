#separador de unidades
numero = float(input('Numero: '))
unidade = numero % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Unidade',unidade ,'\nDezena',dezena ,'\nCentena',centena ,'\nMilhar',milhar)
'''
numero = '0000'
numero += input('Digite um numero de 0 a 9999: ')
print(f'Unidade : {numero[-1]}')
print(f'Dezena : {numero[-2]}')
print(f'Centena : {numero[-3]}')
print(f'Milhar : {numero[-4]}')


num = int(input('Numero: '))
num2 = str(int(10000 + num))
print('M',num2[1])
print('C',num2[2])
print('D',num2[3])
print('U',num2[4])'''