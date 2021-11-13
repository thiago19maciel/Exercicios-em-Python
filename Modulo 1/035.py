#leia 3 medidas e diga se forma um triangulo
lado1 = float(input('Lado a: '))
lado2 = float(input('Lado b: '))
lado3 = float(input('Lado c: '))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    print('Congratulations You HAVE a triangle')
else:
    print('Sorry You can''t make a triangle')