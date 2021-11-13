count = total = maisQue1000 = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    valor = float(input('Qual o valor do produto R$'))
    total += valor
    count += 1
    if count == 1 or valor < menorValor:
        maisBarato = nome
        menorValor = valor
    if valor > 1000:
        maisQue1000 += 1
    continuar = ' '
    while not continuar in 'SN':
        continuar = str(input('Continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O valor total da compra é: R${total:.2f}')
print(f'{maisQue1000} produtos custam mais que R$1000')
print(f'O produto mais barato é {maisBarato} e custa R${menorValor}')
