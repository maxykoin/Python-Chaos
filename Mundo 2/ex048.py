print('=== Desafio 48 ===')

s = 0
i = 0 

for n in range(1, 501, 2):
    if n % 3 == 0:
        s = s + 1
        i = i + s
print('A soma de todos os {} números pedidos é de {}'.format(s, i))

# wah