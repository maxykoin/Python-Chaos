print('=== Desafio 40 ===')
t = int(input('Escolha um número para ver a tabuada: '))
for n in range(1, 11):
    print('{} x {:2} = {}'.format(t, n, t*n))

# what i'm failing to grasp is that the range() is the variable we put in before for and that it counts up the range