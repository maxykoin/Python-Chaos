print('=== Desafio 59 ===')
# somar
# multiplicar
# maior 
# novos números
# sair do programa
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

while n1 != None and n2 != None:

    i = int(input('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    Qual é sua escolha? '''))

    if i == 1:
        s = n1 + n2
        print('{} + {} = {}'.format(n1, n2, s))
    elif i == 2:
        m = n1 * n2 
        print('{} x {} = {}'.format(n1, n2, m))
    elif i == 3:
        if n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('{} é maior que {}'.format(n1, n2))
    elif i == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif i == 5:
        print('Programa finalizado!')
        break
    else:
        print('Comando inválido')

# essas tão sendo muito fácil por mais que tenha mais código