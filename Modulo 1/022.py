nome = str(input('Nome: ')).strip()
#O nome com todas as letras maiúsculas e minúsculas.
print(f'{nome} em maiusculas fica {nome.upper()}')
print(f'{nome} em minusculas fica {nome.lower()}')
#– Quantas letras ao todo (sem considerar espaços).
'''tamanho = len(nome.replace(' ',''))
print(f'Seu nome tem {tamanho} letras')'''

#pode faer assim
print(f"Seu nome tem {len(nome) - nome.count(' ')}")
#– Quantas letras tem o primeiro nome.
nome_separado = nome.split()
print(f'Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])}')
