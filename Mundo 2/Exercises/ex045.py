print('=== Desafio 45 ===')
from random import randint
print('''Suas opções
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura
''')
n = int(input('Qual é sua jogada? '))
o = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0, 2)

if n == pc:
    print('Vocês dois escolheram {}. Empate!'.format(o[pc]))
elif n == 0 and pc == 1:
    print('O computador escolhe {}. Você perde!'.format(o[pc]))
elif n == 1 and pc == 2:
    print('O computador escolhe {}. Você perde!'.format(o[pc]))
elif n == 2 and pc == 0:
    print('O computador escolhe {}. Você perde!'.format(o[pc]))

elif pc == 0 and n == 1:
    print('O computador escolhe {}. Você ganha!'.format(o[pc]))
elif pc == 1 and n == 2:
    print('O computador escolhe {}. Você ganha!'.format(o[pc]))
elif pc == 2 and n == 0:
    print('O computador escolhe {}. Você ganha!'.format(o[pc]))
else:
    print('Inválido')

# man easy but there must be a less code version