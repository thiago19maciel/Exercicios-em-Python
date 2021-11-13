# Faça um programa que leia o ano de nascimento de um jovem e
from datetime import datetime
nascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = datetime.today().year
idade = anoAtual - nascimento
# informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
if idade < 18:
    print(f'Faltam {18-idade} anos para voce se alistar')
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
elif idade == 18:
    print('Voce deve se alistar esse ano!')
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
else:
    print(f'Voce devia ter se alistado há {idade - 18} anos. Em {anoAtual - (idade - 18)}')