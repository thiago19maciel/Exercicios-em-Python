somaPares = 0
for i in range(0,6):
    num = int(input('Digite qualquer numero: '))
    if num % 2 == 0:
        somaPares += num
print(f'A soma dos numeros pares digitados foi de: {somaPares}')