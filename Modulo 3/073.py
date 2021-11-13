times = ('America-MG','Athletico-PR','Atletico-GO',
'Atletico-MG','Bahia','Bragantino','Ceara',
'Chapecoense','Corinthians','Cuiaba',
'Flamengo','Fluminense','Fortaleza',
'Gremio','Internacional','Juventude',
'Palmeiras','Santos','Sao Paulo','Sport')

print(f'Os 5 primeiros colocados são:')
for i in range(0,5):
     print(f'{i + 1}° {times[i]}')

print(f'Os ultimos 4 times da tabela são')
for c in range(16,20):
    print(f'{c+1}° {times[c]}',end= ' ')

sorted(times)
print(f'\nPor ordem alfabética')
for i in range(0,20):
     print(f'{i + 1}° {times[i]}')

timePesquisado = str(input('Qual time quer saber a posição: ')).title()     
if timePesquisado in times:
    print(f'O time {timePesquisado} está na {times.index(timePesquisado)+1}° posição')
else:
    print('Time digitado não existe')