def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f"\033[0;31mErro! Digite um numero inteiro valido.\033[m")
            continue
            #Volta para loop while
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuario!")
            return 0
        else:
            return n

def linha(tam=42):
    print('-'*tam)

def cabecalho(texto):
    linha()
    print(texto.center(42))
    linha()

def menu(lista_opcoes):
    cabecalho("Menu principal")
    c = 1
    for item in lista_opcoes:
        print(f"{c} - {item} ")
        c += 1
    linha()
    opc = leia_int("Digite um numero inteiro: ")
    return opc



