#nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
soma = 0
maiorIdade = 0
mulheresMais20 = 0
for i in range(0,4):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sex = str(input('Digite seu sexo: '))
    soma += idade
    if idade > maiorIdade and not sex in 'Ff':
        maisVelho = nome
    elif idade > 20 and sex not in 'Mm':
        mulheresMais20 += 1
media = soma / 4
print(f'A média de idade é {media:.2f} anos')
print(f'O homem mais velho cadastrado foi {maisVelho}')
print(f'Foram cadastradas {mulheresMais20} mulheres com mais de 20 anos')
#a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.