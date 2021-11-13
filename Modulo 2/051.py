primeiro = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print(f'PA: ',end=' ')
for i in range(0,11):
    proximoTermo = primeiro + (razao*i)
    print(f'{proximoTermo}',end=' ')
