#cadastrar nome, ano nascimento como idade
from datetime import datetime
dadosTrabalhador = {
    'nome' : str(input('Nome: ')),
    'idade' : datetime.today().year - int(input('Ano nascimento: ')),
    'ctps' : int(input('CTPS: '))
}

# se houver carteira de trabalho, ler numero, data contrato e dizer idade aposentadoria
if dadosTrabalhador['ctps'] != 0:
    dadosTrabalhador['Ano Contrato'] = int(input('Ano de contratação: '))
    dadosTrabalhador['Idade aposentadoria'] = (dadosTrabalhador['Ano Contrato'] + dadosTrabalhador['idade'] + 35) - datetime.today().year
    
print(dadosTrabalhador)