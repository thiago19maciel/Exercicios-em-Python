valores = [[],[]]
for i in range(0,7):
    valor = int(input(f'Digite o {i+1}° valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f'Os valores pares foram {sorted(valores[0])}')
print(f'Os valores impares foram {sorted(valores[1])}')
