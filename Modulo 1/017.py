cat_op = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digite o cateto adjascente: '))

'''
hipotenusa = ((cat_op ** 2) + (cat_adj ** 2)) ** 0.5
print(f'Hipotenusa = {hipotenusa:.2f}')
'''
#using modules
'''
from math import hypot
print(f'Hipotenusa = {hypot(cat_op, cat_adj):.2f}')
'''

from math import sqrt as raizQuadrada
hipotenusa = raizQuadrada((cat_op*cat_op) + (cat_adj*cat_adj))
print(f'Hipotenusa = {hipotenusa:.2f}')