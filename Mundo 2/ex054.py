print('=== Desafio 54 ===')

tM = 0
tm = 0

for c in range(1, 8):
    n = int(input('Qual é a idade da {}º pessoa?: '.format(c)))
    if 2022 - n <= 18:
        tm += 1
    else:
        tM += 1

print('Existem {} pessoas menores de idade no grupo'.format(tm))
print('Existem {} pessoas maiores de idade no grupo'.format(tM))