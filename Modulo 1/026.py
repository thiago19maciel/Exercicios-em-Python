frase = str(input('Digite uma frase qualquer: ')).strip().upper()
#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
print(f'A letra "A" apareceu', frase.count('A'), 'vezes')
# em que posição ela aparece a primeira vez
print(f'A letra "A" apareceu na posição', frase.find('A')+1)
# e em que posição ela aparece a última vez.
print(f'A letra "A" apareceu pela ultima vez na posição', frase.rfind('A')+1)