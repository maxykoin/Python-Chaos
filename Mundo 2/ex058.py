print('=== Desafio 58 ===')
from random import randint

n = int(input('Em que número estou pensando? (0-5): '))
r = randint(0, 5)

p = 0
while n != r:
    n = int(input('Errou!. Em que número estou pensando agora? (0-5): '))
    p += 1
    if n == r:
        print('Parábens, você acertou! Estava pensando no número {}! Você teve {} palpites'.format(r, p))
        break 