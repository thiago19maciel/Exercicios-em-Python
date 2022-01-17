def aumentar(preco, taxa, formatar = False):
    '''

    :param preco: valor a ser formatado
    :param taxa: porcentagem a ser aumentada
    :param formatar: caso seja True, formata para moeda R$1,00
    :return: retorna o valor formatado ou nao, dependendo do param formatar
    '''
    res = preco + (preco * taxa/100)
    if formatar == True:
        return moeda(res)
    else:
        return res


def diminuir(preco, taxa, formatar = False):
    '''

    :param preco: valor a ser formatado
    :param taxa: porcentagem a ser reduzida
    :param formatar: caso seja True, formata para moeda R$1,00
    :return: retorna o valor formatado ou nao, dependendo do param formatar
    '''
    res = preco - (preco * taxa/100)
    if formatar == True:
        return moeda(res)
    else:
        return res


def dobro(preco, formatar = False):
    '''

    :param preco: valor a ser formatado
    :param formatar: caso seja True, formata para moeda R$1,00
    :return: retorna o valor formatado ou nao
    '''
    res = preco * 2
    if formatar == True:
        return moeda(res)
    else:
        return res


def metade(preco, formatar = False):
    '''

    :param preco: valor a ser formatado
    :param formatar: formata de 1.0 para R$1,00
    :return: retorna o valor formatado ou nao
    '''
    res = preco / 2
    if formatar == True:
        return moeda(res)
    else:
        return res


def moeda(preco, unidade="R$"):
    return f"{unidade}{preco:.2f}".replace(".", ',')


def resumo(preco = 0, taxa_aumento=0, taxa_reducao=0):
    #valor = preco
    #aumento = taxa_aumento
    #reducao = taxa_reducao
    print('-'*30)
    print(f"Resumo do valor".center(30))
    print('-' * 30)
    print(f"Preco analisado: \t{moeda(preco)}")
    print(f"Dobro do preco: \t\t{dobro(preco,True)}")
    print(f"Metade do preco: \t{metade(preco,True)}")
    print(f"Aumentando {taxa_aumento}%: \t{aumentar(preco, taxa_aumento,True)}")
    print(f"Reduzindo {taxa_reducao}%: \t{diminuir(preco,taxa_reducao,True)}")
    print("-"*30)
