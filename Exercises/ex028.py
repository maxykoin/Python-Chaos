print('=== Desafio 28 ===')

# puta biblioteca foda
# tentei fazer com o choice primeiro mas esse faz mais sentido
# leia a documentação da biblioteca crianças 
from random import randint

n = int(input('Em que número estou pensando? (0-5): '))
r = randint(4, 5)

if n == r:
    print('Parábens, você acertou! Estava pensando no número', r)
else:
    print('Você errou, estava pensando no número', r)