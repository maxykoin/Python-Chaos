print('=== Desafio 65 ===')
v = 'n'
s = m = c = 0

while v != 's':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        M = me = n
    else:
        if n > M:
            M = n
        if n < me:
            me = n 
    v = input('Quer parar? (S/N): ').lower()
m = s / c
print('Você digitou {} números e a média deles é {:.2F}'.format(c, m))
print('O maior valor foi {} e o menor foi {}'.format(M, me))