print('=== Desafio 28 ===')
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usúario venceu ou perdeu.

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