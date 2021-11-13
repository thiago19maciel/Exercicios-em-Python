#Crie um programa que leia duas notas de um aluno e calcule sua média
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1+nota2)/2

#mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
if media < 5:
    print(f'Média {media:.1f} \nAluno REPROVADO ')
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
elif media < 7:
    print(f'Média {media:.1f} \nAluno EM RECUPERAÇÃO')
#– Média 7.0 ou superior: APROVADO
else:
    print(f'Média {media:.1f} \nAluno APROVADO')