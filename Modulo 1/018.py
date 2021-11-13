#Faça um programa que leia um ângulo qualquer
from math import radians
angulo = int(input('Digite o angulo desejado para conversão: '))
x = radians(angulo)
#mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan
print(f'O cosseno de {angulo}° é {cos(x):.2f}')
print(f'O seno de {angulo}° é {sin(x):.2f}')
print(f'A tangente de {angulo} é {tan(x):.2f}')