print('=== Desafio 34 ===')
n = float(input('Sálario original: R$'))

if n > 1250:
    print('O salário de R${:.2F} aumenta para R${:.2F}'.format(n, n + (n * 10 / 100)))
else:
    print('O salário de R${:.2F} aumenta para R${:.2F}'.format(n, n + (n * 15 / 100)))
# odeio porcentagem seu bosta