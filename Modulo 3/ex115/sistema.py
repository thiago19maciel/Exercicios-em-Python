from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'Cadastro.txt'
if not arquivo_existe('Cadastro.txt'):
    criar_arq('Cadastro.txt')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('EXIBINDO PESSOAS CADASTRADAS')
        ler_arq(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        escrever_arq(arq)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Ate logo!')
        break
    else:
        print("Erro! Digite uma opcao valida!")

