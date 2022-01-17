from ex115.lib.interface import *

def arquivo_existe(nome):
    try:
        arquivo = open(nome, "rt")
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        print("Arquivo encontrado")
        return True

def criar_arq(nome):
    try:
        arquivo = open(nome, "wt+")
        arquivo.close()
    except:
        print("Erro na criacao do arquivo")
    else:
        print("Arquivo criado com sucesso")


def ler_arq(nome):
    arq = open(nome, "rt")
    for linha in arq:
        dado = linha.split(';')
        print(f"{dado[0]:<30}{dado[1]:>3} anos")

def escrever_arq(nome):
    arq = open(nome, "a")
    while True:
        nomeDaPessoa = input("Digite o nome: ").strip()
        if not nomeDaPessoa.replace(" ",'').isalpha():
            print("Erro! Digite apenas letras...")
        else:
            break
    idade = leia_int("Digite a idade: ")
    print(f"Novo registro de {nomeDaPessoa} adicionado!")
    arq.writelines(f"{nomeDaPessoa};{idade}")
    arq.write('\n')
