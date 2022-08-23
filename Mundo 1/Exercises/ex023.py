print('=== Desafio 23 ===')
n = int(input('Digite um número: '))
print('''Análisando o número {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
'''.format(n, n // 1 % 10, n // 10 % 10, n // 100 % 10, n // 1000 % 10))
# arrumar solução matemática vai ser muito difícil pra mim e olha que eu to aprendendo pra análisar dados
# nem lembrava oq era milhar man