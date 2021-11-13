def escreva(msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f"  {msg}")
    print('-'*tam)


mensagem = input('Digite uma mensagem qualquer: ')
escreva(mensagem)