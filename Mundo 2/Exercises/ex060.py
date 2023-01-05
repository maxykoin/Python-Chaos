print('=== Desafio 60 ===')
from math import factorial

n = int(input('Digite um número: '))
c = n
print('Calculando o fatorial de {}! = '.format(n), end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(factorial(n))