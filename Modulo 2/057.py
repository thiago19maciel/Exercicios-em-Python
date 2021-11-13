sexo = str(input('Digite seu sexo: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F': #while sexo not in 'MmFm':
    sexo = str(input('Opção inválida, digite seu sexo novamente: ')).upper().strip()[0]
print('Sexo \033[1;33m',sexo,'\033[m registrado com sucesso')