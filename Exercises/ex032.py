print('=== Desafio 32 ===')

# mlk eu nem sei o que é ano bissexto
# aparentemente não acontece em anos múltiplos de 100 que não são múltiplos de 400?
# e o básico é que se o ano for divisivel for 4 ele é bissexto mas ai entra essa outra regra
# sei programar só não sei contar 2.0

from datetime import date

n = int(input('Que ano você quer analizar? Coloque 0 para saber do ano atual. '))

if n == 0:
    n = date.today().year

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('O ano de {} é bissexto'.format(n))
else:
    print('O ano de {} não é bissexto'.format(n))