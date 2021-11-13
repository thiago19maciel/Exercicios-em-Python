expressao = str(input('Digite sua expressão: '))
soma = 0
for c in range(0,len(expressao)):
    if expressao[c] == '(':
        soma += 1
    elif expressao[c] == ')':
        soma -= 1
    if soma < 0:
        break
if soma == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')