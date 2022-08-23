print('=== Desafio 27 ===')
n = input('Escreva uma frase: ').strip().split()
print('Seu primeiro nome é {} \n Seu último nome é {}'.format(n[0], n[len(n)-1]))
# wdym you can use len like this???? 
# what's the logic behind this?
# len() gives off the number of objects in the list, -1 sends it back to the last one?