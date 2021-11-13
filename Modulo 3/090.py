dados_aluno = {'Nome': str(input('Nome do aluno: ')), 'Media': float(input('Média: '))}
if dados_aluno['Media'] > 7:
    dados_aluno['situação'] = 'Aprovado'
else:
    dados_aluno['situação'] = 'Reprovado'
print(f'Situação é igual a {dados_aluno["situação"]} ')