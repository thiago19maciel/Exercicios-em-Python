extenso = (
    'zero','um','dois','tres',
    'quatro','cinco','seis',
    'sete','oito','nove',
    'dez','onze','doze','treze',
    'catorze','quinze','desesseis','dezessete','dezoito','dezenove','vinte')

while True:
    numero = int(input('Digite um numero: '))
    if not 0 <= numero <= 20:
        print('Valor inválido')
    else:
        if numero < 0:
            print(f'Voce digitou o numero menos {extenso[numero * -1]}')
        else:
            print(f'Você digitou o numero {extenso[numero]}')
    continuar = str(input('Você deseja continuar [Sim/Não]: ')).strip()[0]
    if continuar in 'Nn':
        break
print('FIM DO PROGRAMA')