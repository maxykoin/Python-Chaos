print('=== Desafio 37 ===')
# 

n = int(input('Digite um número inteiro: '))
print('''
    [ 1 ] Binário
    [ 2 ] Octal
    [ 3 ] Hexadecimal
''')
i = int(input('Sua opção: '))

if i == 1:
    print('A conversão do número {} para binário é {}'.format(n, bin(n) [2:]))
elif i == 2:
    print('A conversão do número {} para octal é {}'.format(n, oct(n) [2:]))
elif i == 3:
    print('A conversão do número {} para octal é {}'.format(n, hex(n) [2:]))
else:
    print('Opção inválida')

# o python converte coisa uhull emoji de festa ade aniversário
# e elif também