print('=== Desafio 12 ===')
n = float(input('Qual é o preço do produto: '))
d = int(input('Qual é disconto aplicado: '))
print('O produto no valor de R${:.2F}, com desconto de {}%, custará R${:.2F}'.format(n, d, n - (n * d / 100)))
# não sei mamtemática básica meu deus 