print('=== Desafio 53 ===')

n = input('Digite uma frase: ').strip().lower()
s = n.split()
u = ''.join(s)
i = ''

# tried to grasp this thinking its like a variable that you add 1-50 shit in manually still don't get the -1 tho
                # start, stop, step / so it starts on the list compriment -1, then the other -1 means don't stop?
for c in range(len(u) - 1, -1, -1):
     i += u[c]
print('O inverso da frase {} é {}'.format(n, i))

if u == i:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')

# i hate text editing man