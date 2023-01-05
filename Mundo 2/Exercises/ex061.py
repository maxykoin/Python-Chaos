print('=== Desafio 61 ===')

n1 = int(input('Primeiro Termo: '))
n2 = int(input('Razão: '))    
t = n1
c = 1

while c <= 10:
    print('{} -> '.format(t), end='')
    t += n2
    c += 1
print('FIM')