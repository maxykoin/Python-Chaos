print('=== Desafio 34 ===')
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. -Para os inferiores ou iguais, o aumento é de 15%.
n = float(input('Sálario original: R$'))

if n > 1250:
    print('O salário de R${:.2F} aumenta para R${:.2F}'.format(n, n + (n * 10 / 100)))
else:
    print('O salário de R${:.2F} aumenta para R${:.2F}'.format(n, n + (n * 15 / 100)))
# odeio porcentagem