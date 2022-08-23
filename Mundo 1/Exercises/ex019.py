print('=== Desafio 19 ===')
# sortear um nome entre 4
from random import choice
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Terceiro aluno: ')
# array/lista com os nomes
l = [a, b, c, d]
print('O escolhido é {}'.format(choice(l)))