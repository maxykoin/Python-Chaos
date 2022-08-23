print('=== Desafio 20 ===')
# sortear um nome entre 4
from random import shuffle
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Terceiro aluno: ')
# array/lista com os nomes
l = [a, b, c, d]
# não funciona dentro dos colchetes/no format
shuffle(l)
print('A ordem é {}'.format(l))