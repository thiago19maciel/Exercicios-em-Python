# Data reading
condicao = True
somaIdades = 0
listaPessoas = []
while condicao:
    dados = {
        "Nome" : str(input('Nome: ')),
        "Idade" : int(input('Idade: '))
    }
    somaIdades += dados["Idade"]
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print('Erro! Digite apenas M ou F')
    listaPessoas.append(dados.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if continua in 'SN':
            if continua == 'N':
                condicao = False
                break
            if continua == 'S':
                break
        else:
            print('Erro! Digite apenas S ou N')
mediaIdades = somaIdades / len(listaPessoas)

# Showing results
print(f'A) Ao todo temos {len(listaPessoas)} pessoas cadastradas')
print(f'B) A média de idade é de {mediaIdades:.2f} anos')
print(f'C) As mulheres cadastradas foram: ',end='')
for i in range(0,len(listaPessoas)):
    if listaPessoas[i]["sexo"] == 'F':
        print(listaPessoas[i]["Nome"],end=' ')
print(f'\nD) As pessoas com idade acima da média: ')
for c in listaPessoas:
    if c['Idade'] > mediaIdades:
        for k,v in c.items(): # Variavel de controle C serve como cada termo da lista
            print(f'  => {k} = {v}',end='')
        print()
print('<< ENCERRADO >>')