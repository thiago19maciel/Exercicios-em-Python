# A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria,
nascimento = int(input('Ano de nascimento: '))
from datetime import datetime
anoAtual = datetime.today().year
idade = anoAtual - nascimento
# de acordo com a idade:
# – Até 9 anos: MIRIM
if idade < 9:
    print(f'{idade} anos. Categoria MIRIM')
# – Até 14 anos: INFANTIL
elif idade < 14:
    print(f'{idade} anos. Categoria INFANTIL')
# – Até 19 anos: JÚNIOR
elif idade < 19:
    print(f'{idade} anos. Categoria JÚNIOR')
# – Até 25 anos: SÊNIOR
elif idade < 25:
    print(f'{idade} anos. Categorai SÊNIOR')
# – Acima de 25 anos: MASTER
else:
    print(f'{idade} anos. Categoria MASTER')
