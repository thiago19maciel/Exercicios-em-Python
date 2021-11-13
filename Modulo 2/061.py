#PA
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da pa: '))
termo = 1
while termo <= 10:
  print(f'{primeiro}', end='') if termo == 1 else print(f' -> {primeiro + (razao * termo)}', end='')
  termo += 1
print(' Acabou')