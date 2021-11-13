for i in range(0,4):
    peso = int(input(f'Digite o peso da {i+1}° pessoa: '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O menor peso registrado foi {menor} \nE o maior foi {maior}') 