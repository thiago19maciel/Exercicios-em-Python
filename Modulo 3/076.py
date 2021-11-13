produtos = ('manga',2.75,
'banana',5.50,'suco', 13.49,'couve',2.50, 
'morango',9.78,)
print(f'{"Vila das Frutas":^40}')
for i in range (0,len(produtos)):#for i in produtos
    if i % 2 == 0:#if type(i) is str
        print(f'{produtos[i]:.<30}',end='')
    else:
        print(f'R${produtos[i]:>7.2f}')