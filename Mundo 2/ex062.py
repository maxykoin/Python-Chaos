print('=== Desafio 62 ===')

n1 = int(input('Primeiro Termo: '))
n2 = int(input('Razão: '))    
te = n1
c = 1
t = 0
m = 10

while m != 0:
    t = t + m
    while c <= t:
        print('{} -> '.format(te), end='')
        te += n2
        c += 1
    print('Pausa')
    m = int(input('Quantos termos a mais você quer mostrar? '))
    if m == 0:
        break
print('FIM')