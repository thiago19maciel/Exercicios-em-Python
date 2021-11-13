#Um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele
#lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import randint
lista = [input('Digite o nome do 1° aluno: '), 
         input('Digite o nome do 2° aluno: '),
         input('Digite o nome do 3° aluno: '),
         input('Digite o nome do 4° aluno: ')]
print(f'O aluno sorteado para apagar o quadro foi {lista[randint(0,4)]}')