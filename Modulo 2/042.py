# Refaça o DESAFIO 35 dos triângulos
# , acrescentando o recurso de mostrar que tipo de triângulo será formado:
a = float(input('LADO A: '))
b = float(input('LADO B: '))
c = float(input('LADO C: '))
# – EQUILÁTERO: todos os lados iguais
if a == b == c:
    print('3 LADOS IGUAIS. VOCE TEM UM EQUILÁTERO')
# – ISÓSCELES: dois lados iguais, um diferente
if (a == b != c) or (a == c != b) or (b == c != a):
    print('2 LADOS IGUAIS E UM DIFERENTE. VOCE TEM UM ISÓSCELES')
# – ESCALENO: todos os lados diferentes
if a != b != c != a:
    print('TODOS OS LADOS DIFERENTES. VOCE TEM UM ESCALENO')