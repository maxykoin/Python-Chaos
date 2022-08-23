print('=== Desafio 26 ===')
n = input('Escreva uma frase: ').strip().lower()

print('''
    A letra A aparece {} vezes
    A primeira letra A aparece na posição {}
    A última letra A aparece na posição {}
'''.format(n.count('a'), n.find('a') + 1, n.rfind('a') + 1))
# rfind pra ver a última