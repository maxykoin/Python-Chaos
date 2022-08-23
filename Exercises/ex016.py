print('=== Desafio 16 ===')
from math import trunc
n = float(input('Insira um valor: '))
print('O valor inserido é {} e sua porção inteira é {}'.format(n, trunc(n)))
# outra possibilidade
print('O valor inserido é {} e sua porção inteira é {}'.format(n, int(n)))