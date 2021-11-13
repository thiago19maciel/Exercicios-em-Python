num = int(input('Digite um numero para ver se é primo: '))
cont = 0
for i in range(1,num+1):
    if num % i == 0:
        cont += 1
if cont == 2:
    print(f'O numero {num} é primo')
else:
    print(f'O numero {num} não é primo') 