"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(num=0,show=False):
    """
    -> Calcula o fatorial de um numero
    :num: fatorial a ser calculado
    :show: se False, nao imprime calculo, se True, imprime calculo
    :return: retorna o fatorial calculado
    """
    fat = 1
    for i in range(num,0,-1):
        if show:
            print(i,end='')
            if i > 1 :
                print(" X ",end='',)
            else:
                print(f' = ',end='')
        fat *= i
    return fat
print(fatorial(4,show=True))
help(fatorial)