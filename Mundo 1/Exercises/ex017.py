print('=== Desafio 17 ===')
from math import sqrt
from math import hypot
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
print('O valor da hipotenusa é de {:.2F}'.format(sqrt((co ** 2) + (ca ** 2))))
# esse math ai é foda mlk
print('O valor da hipotenusa é de {:.2F}'.format(hypot(co, ca)))

