troco = float(input('Valor do troco: R$'))
cont50 = cont20 = cont10 = cont1 = 0
while True:
    if troco > 50:
        troco -= 50
        cont50 += 1
    elif troco > 20:
        troco -=20
        cont20 += 1
    elif troco > 10:
        troco -= 10
        cont10 += 1
    elif troco >= 1:
        troco -= 1
        cont1 += 1
    else:
        break
print(f'{cont50} notas de R$50 \n{cont20} notas de R$20 \n{cont10} notas de R$10 \n{cont1} notas de R$1')
