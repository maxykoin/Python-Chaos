print('=== Desafio 50 ===')

# n1 = int(input('Primeiro número: '))
# n2 = int(input('Segundo número: '))
# n3 = int(input('Terceiro número: '))
# n4 = int(input('Quarto número: '))
# n5 = int(input('Quinto número: '))
# n6 = int(input('Sexto número: ')) 

# is there a way to get different values from a single input? .split()?3
# yes dumbass

s = 0
i = 0

for c in range(1,7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        s = s + n
        i = i + 1
print('A soma de todos os {} números pedidos é de {}'.format(i, s))