#Faça um programa que leia três números
num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
num3 = int(input('Number 3: '))
#e mostre qual é o biggest e qual é o menor.

#biggest
if num1 > num2 and num1 > num3:
    biggest = num1
if num2 > num1 and num2 > num3:
    biggest = num2
if num3 > num2 and num3 > num1:
    biggest = num3
    
#menor
if num1 < num2 and num1 < num3:
    smallest = num1
if num2 < num1 and num2 < num3:
    smallest = num2
if num3 < num1 and num3 < num3:
    smallest = num3

print('\nNumeros Digitados\n')
print('number one: ',num1)
print('number two: ',num2)
print('number three: ',num3)

print('The smallest number was ',smallest)
print('The biggest number was ',biggest)