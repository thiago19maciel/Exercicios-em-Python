menores = maiores = 0
from datetime import datetime
anoAtual = datetime.today().year
for i in range(0,6):
    anoNascimento = int(input('Digite seu ano de nascimento: '))
    saldo = anoAtual - anoNascimento
    if saldo >= 18:
        maiores+=1
    else:
        menores+=1
print(f'Foram cadastradas {maiores} pessoas maiores de idade \nE {menores} pessoas menores de idade')