print('=== Desafio 55 ===')

# tenho que pensar mais como eu pensava quando programava no arduino
M = 0
m = 0

for c in range(1, 6):
    n = float(input('Qual é o peso da {}ª pessoa? '.format(c)))
    if c == 1:
        m = n
        M = n
    else:
        if n > M:
            M = n
        if n < m:
            m = n 

print('O maior peso lido foi {} e o menor foi {}'.format(M, m))
    