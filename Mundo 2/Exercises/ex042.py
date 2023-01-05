print('=== Desafio 42 ===')
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 > n2 + n3 and n2 > n1 + n3 and n3 > n1 + n2:
    print('Esses segmentos não formam um triângulo')
elif n1 == n2 and n1 == n3 and n2 == n3:
    print('Esse segmento forma um triângulo equilátero')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Esse segmento forma um triângulo isósceles')
elif n1 != n2 and n1 != n3 and n2 != n3:
    print('Esse segmento forma um triângulo escaleno')
# easy breazy