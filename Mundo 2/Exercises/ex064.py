print('=== Desafio 64 ===')

n = c = s = 0
n = int(input('Digite um número (999 para parar): '))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um número (999 para parar): '))
print('A soma dos {} números digitados é {}'.format(c, s))