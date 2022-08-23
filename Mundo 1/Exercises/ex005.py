print('=== Desafio 5 ===')
# descobrir o sucessor e o antecessor de um input numerico
n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print('Tendo o número {}, seu antecessor é {} e seu sucessor é {}'.format(n, a, s))
# do professor:
print('Tendo o número {}, seu antecessor é {} e seu sucessor é {}'.format(n, (n - 1), (n + 1)))
# se você for precisar das variaveis do antecessor e sucessor na frente, é inevitável cria-las aqui
