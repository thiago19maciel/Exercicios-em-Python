aluno = []
notas = []
sala = []
media = []
print('-=-=-= Boletim escolar =-=-=-')
while True:
    nome = str(input('Nome: '))
    aluno.append(nome)
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media.append((notas[0]+notas[1])/2)
    #pode usar tambem ficha = [[nome], [nota1,nota2], [media]]
    aluno.append(notas[:])
    aluno.append(media[:])
    sala.append(aluno[:])
    aluno.clear()
    notas.clear()
    media.clear()
    flag = str(input('Continuar[S/N]: '))
    if flag in 'Nn':
        break
print(f'{"N°":<4} {"Nome":<10} {"Média":>8}')
print('-=-'*10)
for i,a in enumerate(sala):
    print(f'{i+1}   {a[0]}    {a[2]}')
while True:
    print('-=-'*10)
    numeroAluno = int(input('Mostrar notas de qual aluno (999 para parar): '))
    if numeroAluno == 999:
        break
    else:
        numeroAluno -= 1
        if numeroAluno <= len(sala) -1:
            print(f'As notas de {sala[numeroAluno][0]} são: {sala[numeroAluno][1]}')
        else:
            print('Numero invalido')