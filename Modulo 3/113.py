"""
Reescreva a função leiaInt() que fizemos no desafio 104,
 incluindo agora a possibilidade da digitação de um número de tipo inválido.
  Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leia_tipo(tipo, informacao_pedida):
    while True:
        try:
            numero = tipo(input(f"Digite {informacao_pedida}: "))
            # nao receber palavras, espaços ou numero real
            return numero
        except ValueError:
            print(f"\033[0;31mErro! Digite {informacao_pedida} válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuario!")


inteiro = leia_tipo(int, "um numero inteiro")
real = leia_tipo(float, "um numero real")
print(f"\nO numero inteiro digitado foi: {inteiro} \n"
      f"E o numero real digitado foi: {real}")
