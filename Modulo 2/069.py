maior18 = mulheresMenor20 = homens = 0
from os import system
while True:
    system('cls')
    sexo = ' '
    while not sexo in 'MF':
        sexo = str(input('digite seu sexo M for Male/ F for female: ')).strip().upper()[0]
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenor20 += 1
    continua = ' '
    while not continua in 'SN':
        continua = str(input('Deseja continuar Sim(s) Não(n): ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'São {maior18} pessoas com mais de 18 anos')
print(f'São {homens} homens')
print(f'São {mulheresMenor20} mulheres com mais de 20 anos')