while True:
    tabuada = int(input('Qual tabuada voce deseja: '))
    cont = 0
    if tabuada < 0:
        break
    for cont in range(0 ,11):
        print(f'{tabuada} X {cont} = {tabuada*cont}')
        cont += 1
    print('-'*30)
print('FIM')