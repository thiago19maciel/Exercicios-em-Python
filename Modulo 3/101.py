"""Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""
# importacoes
from datetime import datetime


# funcoes
def voto(anoNascimento=0,anoAtual=0):
    anoNascimento = int(input("Digite seu ano de nascimento: "))
    global idade
    anoAtual = datetime.today().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        return "NEGADO"
    elif idade < 18 or idade > 59:
        return "OPCIONAL"
    else:
        return "OBRIGATÓRIO"


# programa principal
idade = 0

resultado = voto()
print(f"Com {idade} anos: VOTO {resultado}")

"""Outra forma de fazer

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = ano - atual
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA"
    elif idade < 18 or idade > 59:
        return f"Com {idade} anos: VOTO OBRIGATORIO
    else:
        return f"Com {idade} anos: VOTO OPCIONAL

nascimento = int(input("Em que ano voce nasceu: "))
print(voto(nascimento))

"""