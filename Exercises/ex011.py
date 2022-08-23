print('=== Desafio 11 ===')
a = float(input('Qual é a altura da sua parede: '))
b = float(input('Qual é a largura da sua parede: '))
t = (a*b) / 2
print('A sua parede é de {}x{}, tendo a área de {}m2. \n Para pintar sua parede você vai precisar de {}L de tinta'.format(a, b, a*b, t))
# a cada 2m de parede voce precisa de 1 litro de tinta