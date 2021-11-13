# frase = str(input('Digite uma frase para ver se é Palindromo: ')).strip().upper().replace(' ','')
# inverso = ''
# for i in range(len(frase)-1,-1,-1):
#     inverso += frase[i]
# if inverso == frase:
#     print(f'Sua frase {frase} é um palindromo')
# else:
#     print(f'Sua frase {frase} não é um palindromo')

#pode fazer tambem
frase = str(input('Digite a frase para saber se é um palindromo: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for i in range(len(frase)-1,-1,-1):
    inverso += frase[i]
if inverso == frase:
    print(f'Sua frase {frase} é um palindromo')
else:
    print(f'Sua frase {frase} não é um palindromo')