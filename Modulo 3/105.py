"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas – A maior nota – A menor nota – A média da turma – A situação (opcional)"""

# funcoes
# essa funcao ira limpar a tela
def l():
    from os import system
    system("cls")

# essa funcao ira coletar as informacoes
def notas(*notasTurma,mostrarSituacao=False):
    """
    -> Coleta notas de alunos e informa:
    :param notasTurma: lista com as notas da turma
    :param mostrarSituacao: argumento opcional que indica como a situacao da turma
    :return dicionario: retorna um dicionario com as informacoes da turma
    """
       
    listaDeNotas = list()
    # receber quantidade indefinida de valores
    while True:
        l()
        nota = float(input("Digite a nota de um aluno: "))
        listaDeNotas.append(nota)
        while True:
            continuar = str(input("Quer digitar mais uma nota? [Sim/Nao]: "))[0].upper()
            if continuar in "SN":
                break
            else:
                l()
                print("Erro! Digite apenas S para sim, ou N para nao")
        if continuar == "N":
            break

    dicionario = {"Quantidade de notas": len(listaDeNotas),"Maior nota": max(listaDeNotas),
    "Menor nota": min(listaDeNotas),"Media da turma": (sum(listaDeNotas) / len(listaDeNotas))}

    if mostrarSituacao:
        if dicionario["Media da turma"] < 5:
            dicionario["Situacao"] = "Ruim"
        else:
            dicionario["Situacao"] = "Boa"
    return dicionario


# main
print(notas())
help(notas)