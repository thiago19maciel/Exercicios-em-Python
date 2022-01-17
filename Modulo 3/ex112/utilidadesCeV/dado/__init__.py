def leia_dinheiro():
    while True:
        texto = input("Digite um valor monetário: R$").replace(' , ', ' . ').strip()
        if texto.isalpha() or texto == '' or not texto.isnumeric():
            print(f"\033[0;31mErro! \"{texto}\" é um preco invalalido!\033[m")
        else:
            return float(texto)
