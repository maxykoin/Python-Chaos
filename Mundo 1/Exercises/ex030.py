print('=== Desafio 30 ===')
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Insira um número: '))

# impar é que não divide por dois, então o resto da divisão nunca vai ser zero
if n % 2 == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))
# matemática /neg
