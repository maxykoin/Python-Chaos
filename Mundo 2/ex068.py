print('=== Desafio 68 ===')
from random import randint
g = 0
        
while True:
    n = int(input('Digite um número: '))
    v = input('Par ou Ímpar? [P/I] ').upper()
        
    while v not in 'PI':
        v = input('Par ou Ímpar? [P/I] ').upper()
    nc = randint(0, 11)
    
    t = n + nc
    print (f'Você jogou {n} e o computador jogou {nc}, total: {t}')
    
    if v == 'P':
        if t % 2 == 0:
            print('Você venceu')
            g += 1
        else:
            print('Você perdeu')
            break
        
    if v == 'I':
        if t % 2 != 0:
            print('Você venceu')
            g += 1
        else:
            print('Você perdeu')
            break
print (f'Game over, você venceu {g} vezes')

# in unbelievable amounts of physical pain while doing this so 100 times slower than usual
    


    